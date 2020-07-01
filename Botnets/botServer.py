import socket
import time
from threading import Thread

clients[]
#threads will be used to store bots
threads[]


def bot_listener(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("", port))
    sock.listen()
    bot, bot_address = sock.accept()
    clients.append(bot)

def main():
    print("The bot server is waiting for connections...")

    starting_port = 8085

    bots = 3

    for i in range(bots):
        t = Thread(target=bot_listener, args=(i+starting_port,), daemon=True)
        threads.append(i)
        run_nc = True
        while run_nc:
            if len(clients) != 0:
                for i, c in enumerate(clients):
                    print("\t\t", i, "\t", c.getpeername()) #getpeername basicallt gets the name of connected peer socket
                selected_client = int(input("Choose an index of the client: "))
                bot = clients[selected_client]
                run_bot = True
                while run_bot:
                    msg = input("Message: ")
                    msg = msg.encode()
                    bot.send(msg)
                    #not finished