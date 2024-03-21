import socket
from threading import Thread
import time

HOST = '127.0.0.1'
PORT = 8001


# 종료 플레그 올려야함
def chat_send(client_socket):
    try:
        while True:
            inputdata = input(">> input : ")
            client_socket.send(inputdata.encode())

            if inputdata == 'q':
                break
    except Exception as e:
        print("connection error(send)")
        print("chatting send function died")
        print(e)
    return


def chat_recv(client_socket):
    # 연결 초기 설정 하고 들어와야댐
    try:
        while True:
            recv_data = client_socket.recv(1024)

            decoded_data = recv_data.decode()

            print('>> Received From -> ', decoded_data)
            if decoded_data == 'q':
                break
    except Exception as e:
        print("connection error(recv)")
        print("chatting recv function died")
        print(e)
    return


def chat_handler(client_socket):
    send_thread = Thread(target=chat_send, args=(client_socket,))
    recv_thread = Thread(target=chat_recv, args=(client_socket,))

    send_thread.start()
    recv_thread.start()

    

def http_send(client_socket):
    print(" >> reciving Data <<  ")

    data = f"GET / HTTP/1.1\r\n"

    encoded_data = data.encode()

    client_socket.send(encoded_data)

    while True:
        recv_data = client_socket.recv(1024)
        if recv_data:
            break
    decoded_recv_data = recv_data.decode()

    print('>> recived data : ', decoded_recv_data)

    client_socket.close()

    return



def main():   
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((HOST, PORT))

    chat_handler(client_socket=client_socket)


if __name__ == "__main__":
    main()