"""
Class: MTRE 4410
Section: W01
Term: Summer 2026
Instructor: Razvan Voicu
Name: Christine Marie Lirazan
Project: Software Project
File: server.py

Description:
Receives employee credentials from the client, verifies access,
sends the authentication result back to the client, and logs
each login attempt.
"""

import socket
import json
import time
from datetime import datetime

# Real-World Mapping:
# This program simulates a building security door access server.
# The server receives an Employee ID and PIN from the client,
# verifies the credentials, and grants or denies access.

HOST = "127.0.0.1"
PORT = 5055

# Requirement: Receiver Processing - Unpack the message and act on it
# (display, save, control a mock actuator).
# Load employee database.
with open("users.json", "r") as file:
    users = json.load(file)

# Extra Feature: Store failed login attempts for each employee.
failed_attempts = {}

# Requirement: Communication Layer - Package and send the input over a
# communication channel. (Recommend Sockets)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Requirement: Client/Server Architecture - Demonstrate separation of
# concerns—client process vs. server process.
server.bind((HOST, PORT))
server.listen()

print("✿" * 50)
print("          SECURITY DOOR ACCESS SERVER")
print("✿" * 50)
print("Server is running...")
print("Waiting for client connection...\n")

while True:

    # Requirement: Server - Listens on a port.
    client, address = server.accept()

    print(f"Client connected from {address}")

    # Requirement: Server - Receives and parses the incoming frame.
    data = client.recv(1024).decode()

    employee, pin = data.split(",")

    # Create login counter for new employees
    if employee not in failed_attempts:
        failed_attempts[employee] = 0

    # Extra Feature: Lock account after three failed login attempts.
    if failed_attempts[employee] >= 3:

        response = (
            "ACCOUNT LOCKED ૮๑ˊᯅˋ๑ა\n"
            "Too many failed login attempts.\n"
            "Please contact the administrator."
        )

    # Requirement: Receiver Processing - Unpack the message and act on it
    # (display, save, control a mock actuator).
    elif employee in users and users[employee] == pin:

        failed_attempts[employee] = 0

        response = (
            "ACCESS GRANTED ૮๑ˆᗜˆ๑ა\n"
            "Door Unlocked"
        )

        print(f"Employee {employee} authenticated.")
        print("Door Unlocked")

        # Extra Feature: Automatically lock the door after 3 seconds.
        time.sleep(3)

        print("Door Locked\n")

    else:

        failed_attempts[employee] += 1

        remaining = 3 - failed_attempts[employee]

        if remaining == 0:

            response = (
                "ACCOUNT LOCKED ૮๑ˊᯅˋ๑ა\n"
                "Too many failed login attempts."
            )

        else:

            response = (
                f"ACCESS DENIED ૮๑ó﹏ò๑ა\n"
                f"Attempts Remaining: {remaining}"
            )

    # Requirement: Receiver Processing - Unpack the message and act on it
    # (display, save, control a mock actuator).
    client.send(response.encode())

    # Extra Feature: Record every login attempt with a timestamp.
    with open("access_log.txt", "a") as log:

        log.write(
            f"{datetime.now()} | "
            f"Employee: {employee} | "
            f"{response.replace(chr(10), ' ')}\n"
        )

    client.close()
