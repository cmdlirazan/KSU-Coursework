"""
Class: MTRE 4410
Section: W01
Term: Summer 2026
Instructor: Razvan Voicu
Name: Christine Marie Lirazan
Project: Software Project
File: client.py

Description:
Captures an Employee ID and PIN from the user,
sends the credentials to the server using a TCP socket,
and displays the authentication result.
"""

import socket

# Real-World Mapping:
# This program simulates a building security door keypad.
# An employee enters an Employee ID and PIN, which are
# sent to the building's access control server.

HOST = "127.0.0.1"
PORT = 5055

# Extra Feature: Welcome screen.
print("✿" * 55)
print("         SECURITY DOOR ACCESS SYSTEM")
print("✿" * 55)
print("Welcome ૮๑ᵔ ᵕ ᵔ๑ა!")
print("Please enter your credentials below.\n")

# Requirement: Input Acquisition - Read data from a simulated or real source
# (keyboard, file, sensor).
employee = input("Employee ID: ")

# Requirement: Input Acquisition - Read data from a simulated or real source
# (keyboard, file, sensor).
pin = input("PIN: ")

# Requirement: Communication Layer - Package and send the input over a
# communication channel. (Recommend Sockets)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Requirement: Client/Server Architecture - Demonstrate separation of
# concerns—client process vs. server process.
client.connect((HOST, PORT))

# Requirement: Client - Sends the data in a structured frame.
message = employee + "," + pin

# Requirement: Communication Layer - Package and send the input over a
# communication channel. (Recommend Sockets)
client.send(message.encode())

# Requirement: Receiver Processing - Unpack the message and act on it
# (display, save, control a mock actuator).
response = client.recv(1024).decode()

print("\n" + "✿" * 55)
print("Authentication Result")
print("-" * 55)
print(response)
print("✿" * 55)

client.close()

print("\nConnection closed.")