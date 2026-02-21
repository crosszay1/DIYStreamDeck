import serial
import serial.tools.list_ports
import subprocess
import webbrowser
import os

def find_arduino_ports():
    arduino_ports = []

    for port in serial.tools.list_ports.comports():
        if (
            "Arduino" in port.description     # official boards
            or "CH340" in port.description    # common Uno clones
            or port.vid == 0x2341             # Arduino vendor ID
            or port.vid == 0x1A86             # CH340 vendor ID
        ):
            arduino_ports.append(port.device)

    return arduino_ports


ports = find_arduino_ports()

if ports:
    print("Arduino found:", ports)
    ser = serial.Serial(ports[0], 9600)
    print("Connected to:", ports[0])
else:
    print("No Arduino detected")
    print("-" * 60)
    print("Please connect an Arduino and restart the program.")
    print("If you have an Arduino connected but it's not detected, please manually select it from the list below:\n")

    # show ALL available ports
    all_ports = list(serial.tools.list_ports.comports())

    if not all_ports:
        print("No serial devices found.")
        exit()

    for i, port in enumerate(all_ports):
        print(f"{i}: {port.device} — {port.description}")

    try:
        selection = int(input("\nEnter port number: "))
        chosen_port = all_ports[selection].device
        ser = serial.Serial(chosen_port, 9600)
        print("Listening to:", chosen_port,"| Note, if this is not your Arduino, you may get garbage data or no data at all.")

    except (ValueError, IndexError):
        print("Invalid selection. Exiting.")
        exit()

    except serial.SerialException as e:
        print("Could not open port:", e)
        exit()


while True:
    key = ser.readline().decode().strip()
    print("Pressed:", key)

    if key == "1":
        subprocess.Popen(r"code", shell=True) #Just to test, we'll add more functios later

    if key == "2":
        webbrowser.open("https://mail.google.com")
    if key == "3": 
        os.startfile("discord://") #discord