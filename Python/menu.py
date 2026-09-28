import plateloader

def main():
    print("Serial Menu")
    loader = plateloader.PlateLoader("COM5")
    loader.connect()
    print("0. Exit")
    print("1. RESET")
    print("2. X-AXIS")
    print("3. GRIPPER")
    print("4. Z-AXIS")
    print("5. MOVE")
    print("6. Status")

    while True:
        selection = int(input("Selection: "))
        
        if selection == 0:
            break
        elif selection == 1:
            loader.send_command("RESET")
        elif selection == 2:
            loader.send_command("X-AXIS")
        elif selection == 3:
            loader.send_command("GRIPPER")
        elif selection == 4:
            loader.send_command("Z-AXIS")
        elif selection == 5:
            loader.send_command("MOVE")
        elif selection == 6:
            loader.send_command("Status")
        else:
            print("Invalid selection")

    loader.disconnect()
    print("Goodbye!")

main()