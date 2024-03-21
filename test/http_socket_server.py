import socket
from threading import Thread
import time


def chat_send(client_socket):
    try:
        while True:
            inputdata = input(">> input : ")
            client_socket.sendall(inputdata.encode())

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


def handle_chat(client_socket):
    send_thread = Thread(target=chat_send, args=(client_socket,))
    recv_thread = Thread(target=chat_recv, args=(client_socket,))

    send_thread.start()
    recv_thread.start()


def handle_request(client_socket):
    request = client_socket.recv(1024).decode()

    # 요청을 파싱하여 요청 메서드와 URL을 가져옴
    method, url, _ = request.split(' ', 2)
    
    if method == 'GET' and url == '/':
        message = "Hello, World"

        # 루트 경로에 대한 GET 요청 처리
        response = f"HTTP/1.1 200 OK\r\nContent-Length: {len(message)}\r\n\r\n{message}"
    else:
        # 지원하지 않는 요청에 대한 응답
        response = 'HTTP/1.1 405 Method Not Allowed\r\n\r\nMethod Not Allowed'

    client_socket.sendall(response.encode())

    return
    
# ws로 접속을 대기
def waiting_client_ws(server_socket):
    print("Chat_System 구동, client 연결 대기 중")
    while True:
        client_socket, client_address = server_socket.accept()
        if client_socket:
            print(f"client 연결됨 ({client_address})")
            print(">>")
            client_thread = Thread(target=handle_chat, args=(client_socket,))
            client_thread.start()

# was로 접속을 대기
def waiting_client_was(server_socket:socket, client:list):
    print("WAS 구동, HTTP 프로토콜 연결 대기 중")
    while True:
        client_socket, client_address = server_socket.accept()
        if client_socket:
            print(f"HTTP 프로토콜 연결됨 ({client_address})")
            client_thread = Thread(target=handle_request, args=(client_socket,))
            client_thread.start()


def main():
    server_sockets = []
    ports = [8000, 8001]  # 8080 : WAS, 8081 : chat

    for port in ports:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(('localhost', port))
        server_socket.listen(5)
        server_sockets.append(server_socket)

    print('서버 시작: http://localhost:8000, 8001')
    was_client = []
    ws_client = []

    was_thread = Thread(target=waiting_client_was, args=(server_sockets[0], was_client,))
    ws_thread = Thread(target=waiting_client_ws, args=(server_sockets[1],))

    ws_thread.start()
    time.sleep(1)
    print("ws run")
    was_thread.start()


if __name__ == "__main__":
    main()


"""
http 프로토콜

요청 부분 (보편적인 예시) GET
GET /index.html HTTP/1.1\r\n
Host: localhost:8080\r\n
Connection: keep-alive\r\n
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36\r\n
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n
Accept-Encoding: gzip, deflate\r\n
Accept-Language: en-US,en;q=0.9\r\n
\r\n


요청 부분 (보편적인 예시) POST
POST /submit_form HTTP/1.1\r\n
Host: example.com\r\n
Connection: keep-alive\r\n
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36\r\n
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n
Accept-Encoding: gzip, deflate\r\n
Accept-Language: en-US,en;q=0.9\r\n
Content-Length: 12\r\n
Content-Type: application/x-www-form-urlencoded\r\n
\r\n
Hello, World!



응답 부분 (string 타입)
HTTP/1.1 200 OK\r\n  # 메타 데이터
Content-Length: 13\r\n  # 길이
Content-Type: text/plain\r\n  # 형태
\r\n
Hello, World!  # 본문


응답 부분 (json 타입)
HTTP/1.1 200 OK\r\n
Content-Length: 26\r\n  # 길이 명시
Content-Type: application/json\r\n  # json 타입 명시
\r\n
{"key": "value", "another_key": "another_value"} 본문 



"""