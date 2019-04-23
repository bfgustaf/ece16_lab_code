"""
Send commands to the BLE module
"""

import serial
from time import sleep

ble_peripheral_MAC = "D8A98BC2D4BA"                 # Use the MAC address of your peripheral HM-10

serial_port = 'COM27'

# Read from serial ser and return the string that was read
def read_BLE(ser):
    msg = ""
    if ser.in_waiting > 0:
        try:
            msg = msg + ser.readline(ser.in_waiting).decode('utf-8')
        except UnicodeDecodeError:
            msg = msg
    return msg


# Write the string, command, to serial ser; return nothing
def write_BLE(command, ser):
    ser.write(command.encode("utf-8"))
    return


# Open the serial port and when successful, execute the code that follows
with serial.Serial(port=serial_port, baudrate=9600, timeout=1) as ser:

    setup_commands = ["AT", "AT+IMME1", "AT+NOTI1", "AT+ROLE1"]

    connect_command = "AT+CON" + ble_peripheral_MAC

    # Send the setup commands
    for command in setup_commands:
        write_BLE(command, ser)
        print("Sent: " + command)
        sleep(0.5)
        response = read_BLE(ser)
        print("Response: " + response)

    # Keep sending the connect command until connection is established
    response = ""
    while not ("OK+CONNAOK+CONN" in response):
        write_BLE(connect_command, ser)
        print("Sent: " + connect_command)
        sleep(0.5)
        response = read_BLE(ser)
        print("Response: " + response)

    # Notify the Arduino we are connected
    sleep(1)
    write_BLE("Connected",ser)
    print("Connected")
    
    # Monitor for any text received over BLE
    count = 0
    while True:
        response = read_BLE(ser)
        if response:
            print(response)
            if (response == '*'):
                write_BLE("Number: " + str(count), ser)
                print("Sent: " + str(count))
                count = count + 1
