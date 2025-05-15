import tkinter as tk
from tkinter import ttk
import serial
import time

# Open Serial Connection
# Creates a serial connection using pyserial library, COM3 is the port.
# Baud rate is the speed of communication (bits per second).
# timeout=1 means it will wait up to 1 second for a response before moving on.
ser = serial.Serial('COM3', 115200, timeout=1)
time.sleep(2)  # Allows 2 seconds time for ESP32 to initialize serial connection.

# variables
relay_one_state = False
relay_two_state = False
relay_three_state = False
relay_four_state = False
relay_five_state = False
relay_six_state = False
relay_seven_state = False
relay_eight_state = False

# functions
def toggle_relay_one():
    global relay_one_state
    if relay_one_state == True: # if the relay is ON then
        ser.write(b"OneOFF\n") # send command over bytes to turn off
        print("Sent: Relay One OFF") # print to python terminal
        time.sleep(1)
        print(ser.readline().decode().strip())  # ser.readline() reads response from ESP32.
        # .decode() converts the received bytes to string. .strip() removes trailing whitespace and newline characters.
        # prints response.
        relay_one_state = False
    else:
        relay_one_state = False # if the relay is OFF then
        ser.write(b"OneON\n") # send the command over bytes to turn off
        print("Sent: Relay One ON")
        time.sleep(1)
        print(ser.readline().decode().strip())
        relay_one_state = True

def toggle_relay_two():
    global relay_two_state
    if relay_two_state == True:
        ser.write(b"TwoOFF\n")
        print("Sent: Relay Two OFF")
        time.sleep(1)
        print(ser.readline().decode().strip())
        relay_two_state = False
    else:
        relay_two_state = False
        ser.write(b"TwoON\n")
        print("Sent: Relay Two ON")
        time.sleep(1)
        print(ser.readline().decode().strip())
        relay_two_state = True

def toggle_relay_three():
    global relay_three_state
    if relay_three_state == True:
        ser.write(b"ThreeOFF\n")
        print("Sent: Relay Three OFF")
        time.sleep(1)
        print(ser.readline().decode().strip())
        relay_three_state = False
    else:
        relay_three_state = False
        ser.write(b"ThreeON\n")
        print("Sent: Relay Three ON")
        time.sleep(1)
        print(ser.readline().decode().strip())
        relay_three_state = True


def toggle_relay_four():
    global relay_four_state
    if relay_four_state == True:
        ser.write(b"FourOFF\n")
        print("Sent: Relay Four OFF")
        time.sleep(1)
        print(ser.readline().decode().strip())
        relay_four_state = False
    else:
        relay_four_state = False
        ser.write(b"FourON\n")
        print("Sent: Relay Four ON")
        time.sleep(1)
        print(ser.readline().decode().strip())
        relay_four_state = True

def toggle_relay_five():
    global relay_five_state
    if relay_five_state == True:
        ser.write(b"FiveOFF\n")
        print("Sent: Relay Five OFF")
        time.sleep(1)
        print(ser.readline().decode().strip())
        relay_five_state = False
    else:
        relay_five_state = False
        ser.write(b"FiveON\n")
        print("Sent: Relay Five ON")
        time.sleep(1)
        print(ser.readline().decode().strip())
        relay_five_state = True

def toggle_relay_six():
    global relay_six_state
    if relay_six_state == True:
        ser.write(b"SixOFF\n")
        print("Sent: Relay Six OFF")
        time.sleep(1)
        print(ser.readline().decode().strip())
        relay_six_state = False
    else:
        relay_six_state = False
        ser.write(b"SixON\n")
        print("Sent: Relay Six ON")
        time.sleep(1)
        print(ser.readline().decode().strip())
        relay_six_state = True

def toggle_relay_seven():
    global relay_seven_state
    if relay_seven_state == True:
        ser.write(b"SevenOFF\n")
        print("Sent: Relay Seven OFF")
        time.sleep(1)
        print(ser.readline().decode().strip())
        relay_seven_state = False
    else:
        relay_seven_state = False
        ser.write(b"SevenON\n")
        print("Sent: Relay Seven ON")
        time.sleep(1)
        print(ser.readline().decode().strip())
        relay_seven_state = True

def toggle_relay_eight():
    global relay_eight_state
    if relay_eight_state == True:
        ser.write(b"EightOFF\n")
        print("Sent: Relay Eight OFF")
        time.sleep(1)
        print(ser.readline().decode().strip())
        relay_eight_state = False
    else:
        relay_eight_state = False
        ser.write(b"EightON\n")
        print("Sent: Relay Eight ON")
        time.sleep(1)
        print(ser.readline().decode().strip())
        relay_eight_state = True

# list
toggle_functions = [
    toggle_relay_one,
    toggle_relay_two,
    toggle_relay_three,
    toggle_relay_four,
    toggle_relay_five,
    toggle_relay_six,
    toggle_relay_seven,
    toggle_relay_eight
]

# window
window = tk.Tk()
window.title("NCD")
window.geometry("300x400")

# title
title_label = ttk.Label(master = window, text = "Relay Lights", font = ("Calibri 24 bold")) # Font = (Font fontsize bold(if bold))
title_label.pack()

# input field
input_frame = ttk.Frame(master = window)
input_frame.pack(pady = 20)

# create button loop
for i in range(1, 9):
    button = ttk.Button(master = input_frame, text = f"R{i}", command = toggle_functions[i-1])
    button.pack(pady = 5)

# run
window.mainloop()

""" Arduino Script
#include <Adafruit_MCP23008.h>  // Adafruit library for MCP23008.

// This creates an object mcp of the Adafruit_MCP23008 class.
Adafruit_MCP23008 mcp;

// Setup runs once when the Arduino is turned on or reset. Initialize pins and libraries needed.
void setup() {
  Serial.begin(115200); // Starts serial communication, baud rate set at x.
  mcp.begin(); // Initialize the MCP23008.
  /* 
    This for loop starts at i = 0 and runs 8 times (i = 0 to i = 7), covering all 8 GPIO pins of the MCP23008. i++ increases the increment by 1.
    uint8_t, u = unsigned(cannot be negative), int = integer(whole number, no decimal values), 8_t = 8 bits in size(1 byte) can store values between 0-255, type definition. 
    The MCP23008 is an I2C GPIO expander, it has 8 general-purpose input/output (GPIO) pins, and we are configuring them as outputs to control relays.
    mcp.pinMode(i, OUTPUT); = sets each MCP23008 GPIO pin (0-7) to be an output.
    */
  for (uint8_t i = 0; i < 8; i++) {
      mcp.pinMode(i, OUTPUT);
      mcp.digitalWrite(i, LOW);  // LOW means Low Voltage (lights turn OFF).
    }
}

// Runs over a loop while Arduino is on. The main logic of your program.
void loop() {
    if (Serial.available()) {  // Checks if there is any data available in the serial buffer.
        String command = Serial.readStringUntil('\n'); // Reads the incoming serial data until it encounters a newline character (\n).
        
        if (command == "OneON") {
          mcp.digitalWrite(0, HIGH);  // Turn ON all relay lights (HIGH voltage).
          Serial.println("Relay One is ON");  // Send feedback to Python, it will print in the terminal.
        }

        else if (command == "OneOFF") {
          mcp.digitalWrite(0, LOW);  // Turn OFF all relay lights (LOW voltage).
          Serial.println("Relay One is OFF");  // Send feedback to Python, it will print in the terminal.
        }

        else if (command == "TwoON") {
          mcp.digitalWrite(1, HIGH);  // Turn ON all relay lights (HIGH voltage).
          Serial.println("Relay Two is ON");  // Send feedback to Python, it will print in the terminal.
        }

        else if (command == "TwoOFF") {
          mcp.digitalWrite(1, LOW);  // Turn OFF all relay lights (LOW voltage).
          Serial.println("Relay Two is OFF");  // Send feedback to Python, it will print in the terminal.
        }

        else if (command == "ThreeON") {
          mcp.digitalWrite(2, HIGH);  // Turn ON all relay lights (HIGH voltage).
          Serial.println("Relay Three is ON");  // Send feedback to Python, it will print in the terminal.
        }

        else if (command == "ThreeOFF") {
          mcp.digitalWrite(2, LOW);  // Turn OFF all relay lights (LOW voltage).
          Serial.println("Relay Three is OFF");  // Send feedback to Python, it will print in the terminal.
        }

        else if (command == "FourON") {
          mcp.digitalWrite(3, HIGH);  // Turn ON all relay lights (HIGH voltage).
          Serial.println("Relay Four is ON");  // Send feedback to Python, it will print in the terminal.
        }

        else if (command == "FourOFF") {
          mcp.digitalWrite(3, LOW);  // Turn OFF all relay lights (LOW voltage).
          Serial.println("Relay Four is OFF");  // Send feedback to Python, it will print in the terminal.
        }

        else if (command == "FiveON") {
          mcp.digitalWrite(4, HIGH);  // Turn ON all relay lights (HIGH voltage).
          Serial.println("Relay Five is ON");  // Send feedback to Python, it will print in the terminal.
        }

        else if (command == "FiveOFF") {
          mcp.digitalWrite(4, LOW);  // Turn OFF all relay lights (LOW voltage).
          Serial.println("Relay Five is OFF");  // Send feedback to Python, it will print in the terminal.
        }

        else if (command == "SixON") {
          mcp.digitalWrite(5, HIGH);  // Turn ON all relay lights (HIGH voltage).
          Serial.println("Relay Six is ON");  // Send feedback to Python, it will print in the terminal.
        }

        else if (command == "SixOFF") {
          mcp.digitalWrite(5, LOW);  // Turn OFF all relay lights (LOW voltage).
          Serial.println("Relay Six is OFF");  // Send feedback to Python, it will print in the terminal.
        }

        else if (command == "SevenON") {
          mcp.digitalWrite(6, HIGH);  // Turn ON all relay lights (HIGH voltage).
          Serial.println("Relay Seven is ON");  // Send feedback to Python, it will print in the terminal.
        }

        else if (command == "SevenOFF") {
          mcp.digitalWrite(6, LOW);  // Turn OFF all relay lights (LOW voltage).
          Serial.println("Relay Seven is OFF");  // Send feedback to Python, it will print in the terminal.
        }

        else if (command == "EightON") {
          mcp.digitalWrite(7, HIGH);  // Turn ON all relay lights (HIGH voltage).
          Serial.println("Relay Eight is ON");  // Send feedback to Python, it will print in the terminal.
        }

        else if (command == "EightOFF") {
          mcp.digitalWrite(7, LOW);  // Turn OFF all relay lights (LOW voltage).
          Serial.println("Relay Eight is OFF");  // Send feedback to Python, it will print in the terminal.
        }
    }
}

"""