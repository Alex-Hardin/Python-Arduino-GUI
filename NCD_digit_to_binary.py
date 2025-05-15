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


def convert():
    number_input = entry_int.get()
    if number_input < 1 or number_input > 255:
        output_string.set("Enter a number between 1 and 255")
    elif number_input >= 1 and number_input <= 255:
        output_string.set(f"You've entered {number_input}")
        ser.write(
            f"{number_input}\n".encode())  # Sends the string to ESP32 in bytes over the serial connection through .encode().
        print(f"Sent: {number_input} to ESP32")  # prints message to python terminal.
        time.sleep(
            1)  # Allows 0.5 seconds time for ESP32 to initialize serial connection. (1 second was not giving ESP32 feedback strings)
        print(ser.readline().decode().strip())  # ser.readline() reads response from ESP32.
        # .decode() converts the received bytes to string. .strip() removes trailing whitespace and newline characters.
        # prints response.


# window
window = tk.Tk()
window.title("NCD")
window.geometry("400x200")

# title
title_label = ttk.Label(master=window, text="Digits to Binary",
                        font=("Calibri 24 bold"))  # Font = (Font fontsize bold(if bold))
title_label1 = ttk.Label(master=window, text="Enter a number between 1 - 255", font=("Calibri 16 bold"))
title_label.pack()
title_label1.pack()

# input field
input_frame = ttk.Frame(master=window)
entry_int = tk.IntVar()
entry = ttk.Entry(master=input_frame, textvariable=entry_int)
button = ttk.Button(master=input_frame, text="Convert",
                    command=convert)  # for command, only pass the function do not call the function.
entry.pack(side="left", padx=10)  # padx = 10 gives a space between the entry and button 10 pixels
button.pack(side="left")
input_frame.pack(pady=10)  # the space from title_label text to the input frame

# output
output_string = tk.StringVar()
output_label = ttk.Label(master=window, text="Output", font="Calibri 18", textvariable=output_string)
output_label.pack(pady=5)

# run
window.mainloop()

""" Arduino Script
#include <Wire.h>  // I2C (Inter-Integrated Circuit) communication library
#include <Adafruit_MCP23008.h> // Adafruit library for MCP23008

// This creates an object mcp of the Adafruit_MCP23008 class.
Adafruit_MCP23008 mcp; 

// Setup runs once when the Arduino is turned on or reset. Initialize pins and libraries needed.
void setup() {
    Serial.begin(115200); // Start serial communication at baud of x
    Wire.begin();  // Initialize the I2C communication between ESP32 and MCP23008
    mcp.begin();  // Initialize the MCP23008
    Serial.setTimeout(5000000); // Delays serial timer by 5 million milliseconds (was defaulting a 0 value every 2 seconds and spamming serial when trouble shooting)

     /* 
    This for loop starts at i = 0 and runs 8 times (i = 0 to i = 7), covering all 8 GPIO pins of the MCP23008. i++ increases the increment by 1.
    uint8_t, u = unsigned(cannot be negative), int = integer(whole number, no decimal values), 8_t = 8 bits in size(1 byte) can store values between 0-255. 
    The MCP23008 is an I2C GPIO expander, it has 8 general-purpose input/output (GPIO) pins, and we are configuring them as outputs to control relays.
    mcp.pinMode(i, OUTPUT); = sets each MCP23008 GPIO pin (0-7) to be an output.
    */
    for (uint8_t i = 0; i < 8; i++) {
        mcp.pinMode(i, OUTPUT);  // mcp.pinMode(i, OUTPUT); = sets each MCP23008 GPIO pin (0-7) to be an output
        mcp.digitalWrite(i, LOW);  // Starts with all relays OFF, LOW Voltage
    }

    //Serial.println("MCP23008 is ready!");
    //Serial.println("Type an integer between 1 - 255 in the Serial Monitor");
}

// Runs over a loop while Arduino is on. The main logic of your program.
void loop() {
  if (Serial.available()) {  // Checks if there is any data available in the serial buffer.
        String command = Serial.readStringUntil('\n'); // Reads the incoming serial data until it encounters a newline character (\n).
        int numberInput = command.toInt(); // Converts string to integer.

        Serial.println("Input received");
        Serial.flush(); // waits for outgoing serial data to finish before moving on. 

      /*
        // Safety perimeters set
        if (numberInput < 1 || numberInput > 255) { 
              Serial.println("Incorrect input! Please type a number between 1 - 255");
              return; 
        }

    Serial.println("==============================================="); // Seperator for text
    Serial.print("You entered ");
    Serial.println(numberInput);
      */
        // Turn all relays OFF before processing new input
        for (uint8_t i = 0; i < 8; i++) {
            mcp.digitalWrite(i, LOW);
        }

        // Binary conditional values
        if (numberInput >= 128) {
            mcp.digitalWrite(0, HIGH);
            //Serial.println("Turning on Relay 1: #128 is met");
            numberInput -= 128;
        }
        if (numberInput >= 64) {
            mcp.digitalWrite(1, HIGH);
            //Serial.println("Turning on Relay 2: #64 is met");
            numberInput -= 64;
        }
        if (numberInput >= 32) {
            mcp.digitalWrite(2, HIGH);
            //Serial.println("Turning on Relay 3: #32 is met");
            numberInput -= 32;
        }
        if (numberInput >= 16) {
            mcp.digitalWrite(3, HIGH);
            //Serial.println("Turning on Relay 4: #16 is met");
            numberInput -= 16;
        }
        if (numberInput >= 8) {
            mcp.digitalWrite(4, HIGH);
            //Serial.println("Turning on Relay 5: #8 is met");
            numberInput -= 8;
        }
        if (numberInput >= 4) {
            mcp.digitalWrite(5, HIGH);
            //Serial.println("Turning on Relay 6: #4 is met");
            numberInput -= 4;
        }
        if (numberInput >= 2) {
            mcp.digitalWrite(6, HIGH);
            //Serial.println("Turning on Relay 7: #2 is met");
            numberInput -= 2;
        }
        if (numberInput & 1) {
            mcp.digitalWrite(7, HIGH);
            //Serial.println("Turning on Relay 8: #1 is met");
        }
        // Serial.println("===============================================");
  }

}

"""