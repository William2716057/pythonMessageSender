Socket Server and Client Communication

This repository contains a simple Python script for creating a socket server and sending messages to it using a client.

How to Use

Prerequisites

Make sure you have Python installed on your system.

Installation

Clone this repository to your local machine using:

git clone https://github.com/your-username/socket-server.git

Usage

Navigate to the cloned directory:

cd socket-server

Open the Python script socket_server.py in your preferred text editor.

Adjust the target IP address and port in the if __name__ == "__main__": block to match your configuration.

Run the Python script:


python socket_server.py

This will start the server, listening for incoming connections.

In another terminal window or a separate machine, run the Python script socket_client.py to send a message to the server:

python socket_client.py

Ensure that you have adjusted the target IP address and port in the client script accordingly.


