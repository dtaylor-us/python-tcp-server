# TCP Echo Server and Client README

This document provides a detailed overview of a TCP echo server and client application implemented in Python. The application facilitates a basic communication channel where a client can send a message to the server, and the server echoes back a predefined response. This setup demonstrates the use of TCP sockets for reliable, stream-oriented communication between a client and a server.

## Overview

The application is split into two scripts: the client script and the server script. It demonstrates a fundamental TCP communication pattern, where the client initiates a connection to the server, sends a message, receives a response, and finally closes the connection. The server listens for incoming connections, receives messages, sends responses, and closes connections after interaction.

### Server Script

The server script sets up a TCP socket, binds it to a specified host and port, and listens for incoming connections. For each connection, it receives a message of a predefined length from the client, prints it, sends back a fixed response, and then closes the connection.

Key Features:
- Creates a listening TCP socket bound to a specified hostname and port.
- Accepts incoming client connections.
- Receives messages from clients and sends a fixed response.
- Closes client connections after sending the response.

### Client Script

The client script establishes a connection to the server, sends a greeting message, waits for the server's response, prints it, and then closes the connection.

Key Features:
- Connects to a TCP server.
- Sends a greeting message to the server.
- Receives a response from the server and prints it.
- Closes the connection.

## Requirements

- Python 3.x

## Usage

### Server

1. Start the server script on the desired machine to listen for incoming connections.

### Client

1. Run the client script from any machine to connect to the server and send a message.

## Running the Application

To run the server, open a terminal and execute:

```bash
python server_script.py
```

To run the client, open another terminal and execute:

```bash
python client_script.py
```

## Example Interaction

- Server Terminal:

```
Listening at ('127.0.0.1', 3000)
Waiting for a new connection
Connection from ('127.0.0.1', random_client_port)
  Socket name: ('127.0.0.1', 3000)
  Socket peer: ('127.0.0.1', random_client_port)
  message from client: b'Greetings, server'
  Closing socket
```

- Client Terminal:

```
Client has been assigned the socket:  ('127.0.0.1', random_client_port)
Server:  b'Goodbye, client!'
```

## Closing the Application

The server runs indefinitely until manually interrupted. Press `CTRL+C` in the server's terminal to stop it. The client automatically closes its connection after receiving the server's response.

## Note

This application serves as a basic example of TCP communication in Python and is intended for educational purposes. TCP ensures the delivery, ordering, and integrity of the messages, making it suitable for applications where reliable communication is necessary.