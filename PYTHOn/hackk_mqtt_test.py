import Python.Exam3JackJenniges.mqtt as mh
import time 



def mqtt_callback(message_type, message_payload):
    print("The message type is ", message_type)
    print("The message payload is ", message_payload)
    


def main():
    print("Hacky MQTT Test")
    mqtt_client = mh.MqttClient()
    mqtt_client.connect(subscription_topic_name = "jennigja", publish_topic_name = "jennigja")
    mqtt_client.callback = mqtt_callback

    counter = 0
    while True:
        mqtt_client.send_message("counter", counter)
        time.sleep(2)
        counter += 1



main()
