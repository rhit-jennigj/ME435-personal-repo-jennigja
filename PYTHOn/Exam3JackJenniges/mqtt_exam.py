import json
import time
import mqtt as mh
from gpiozero import Motor

# Define your broker and topic
BROKER = "mosquitso.csse.rose-hulman.edu" # or whatever your broker address is
TOPIC = "jennigja"

# --- Initialize your motors with your actual GPIO pin numbers ---
# Example: Motor(forward_pin, backward_pin)
left_motor = Motor(forward=4, backward=14)
right_motor = Motor(forward=17, backward=18)

def message_received(topic, message):
    try:
        data = json.loads(message)
        msg_type = data.get("type")
        payload = data.get("payload")
        
        if msg_type == 'left':
            direction = payload[0]  # 1 = forward, 0 = reverse
            duration = payload[1]   # time_slider_value
            pwm = payload[2] / 100.0 # scale 0-100 down to 0.0-1.0 for gpiozero
            
            print(f"Left Wheel -> Dir: {direction}, Time: {duration}s, Speed: {pwm}")
            
            if direction == 1:
                left_motor.forward(speed=pwm)
            else:
                left_motor.backward(speed=pwm)
                
            time.sleep(duration)
            left_motor.stop()
            
        elif msg_type == 'right':
            direction = payload[0]  # 1 = forward, 0 = reverse
            duration = payload[1]   # time_slider_value
            pwm = payload[2] / 100.0 # scale 0-100 down to 0.0-1.0
            
            print(f"Right Wheel -> Dir: {direction}, Time: {duration}s, Speed: {pwm}")
            
            if direction == 1:
                right_motor.forward(speed=pwm)
            else:
                right_motor.backward(speed=pwm)
                
            time.sleep(duration)
            right_motor.stop()
            
        elif msg_type == 'both':
            direction = payload[0]  # 1 = forward, 0 = reverse
            duration = payload[1]   # time_slider_value
            left_pwm = payload[2] / 100.0   # left sent first, scaled
            right_pwm = payload[3] / 100.0  # right sent second, scaled
            
            print(f"Both Wheels -> Dir: {direction}, Time: {duration}s, Left Speed: {left_pwm}, Right Speed: {right_pwm}")
            
            if direction == 1:
                left_motor.forward(speed=left_pwm)
                right_motor.forward(speed=right_pwm)
            else:
                left_motor.backward(speed=left_pwm)
                right_motor.backward(speed=right_pwm)
                
            time.sleep(duration)
            left_motor.stop()
            right_motor.stop()
            
    except Exception as e:
        print(f"Error processing message: {e}")

# Register the message callback and connect using your helper module
mh.set_callback(message_received)
mh.connect(BROKER, TOPIC)

try:
    while True:
        # 1. Read your actual ultrasonic sensor distance in cm (Replace with your actual sensor code)
        current_distance = 25.0  
        
        # 2. Package it into the schema expected by MATLAB
        sensor_data = {
            "type": "ultra",
            "payload": current_distance
        }
        
        # 3. Publish sensor data back to MATLAB
        mh.publish(TOPIC, json.dumps(sensor_data))
        
        # Send an update every 0.5 seconds
        time.sleep(0.5)

except KeyboardInterrupt:
    print("Exiting program...")
    left_motor.stop()
    right_motor.stop()
    mh.disconnect()