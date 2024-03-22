import time 
from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread

BUFFER_SIZE = 1024


class Client:
    def __init__(self, client_socket, client_address):
        self.__socket = client_socket
        self.__address = client_address
        #self.time = datetime.now()
    
    def __call__(self):
        print("client address : ", self.__address)
        return self.get_client_address()

    def get_client_socket(self):
        return self.__socket

    def get_client_address(self):
        return self.__address
    
    def destroy_client(self):
        print(f"destory client : {self.__address}")
        self.__address = None
        self.__socket = None
        return

# 소켓으로 서버 만들기
class DIY_Socket():
    def __init__(self):
        self.__server_socket = socket(AF_INET, SOCK_STREAM)

    def open_server(self):
        client_socket, client_address = self.__server_socket.accept()
        return client_socket, client_address

    # 소켓 실행시키는 함수
    def execute_socket_platform(self, host:str, port:int, asgi = False):
        self.__server_socket.bind((host, port))
        self.__server_socket.listen(5)
        if asgi:
            print("Asynchronous Server open")
        else:
            print("synchronous Server open")

    # binary data return
    def __recv_data(self, client:Client):
        try:
            socket = client.get_client_socket()
            request = socket.recv(1024)
            return request
        except Exception as e:
            print(e)
            return "error".encode()
    
    # just send
    def __send_data(self, client:Client, data):
        try:
            socket = client.get_client_socket()
            socket.sendall(data)
        except Exception as e:
            print(e)
        return

class HTTP_POTOCOL():
    def __init__(self):
        self.__now_status = ""
        self.__init_status()

    def __init_status(self):
        self.__now_status = "HTTP/1.1 "
        return

    def __recv_data(self, client_socket):
        request = client_socket.recv(1024).decode()
        method, url, protocol = request.split(' ', 2)
        self.__check_protocol(protocol)
        self.__check_url(url)
    
    def __check_protocol(self, protocol):
        if protocol != 'HTTP/1.1':
            self.__init_status()
            raise("This is not HTTP") # 여기서 죽여서 오류를 띄우자
        self.__now_status += "200 OK\r\n"
        return
    
    def __check_url(self, url):
        if '/' not in url:
            self.__init_status()
            raise("Endpoint Error")




# fast_API 따라하기
class mingxn_API(HTTP_POTOCOL):
    def __init__(self):
        self.get_route_map = {}
        super().__init__()

    def get(self, route):
        def decorator(func):
            self.get_route_map[route] = func
            return func
        return decorator
    
    def execute_get(self, route):
        if route in self.get_route_map:
            return self.get_route_map[route]()
        else:
            print("Invalid route")

        


# 진행 상황#
# 대체 어디에다가 HTTP 프로토콜을 넣어야 하는가?
# 당장에는 DIY_Socket을 상속하지말고 내부 멤버로 받는게 좋겠다
# 왜냐하면 포트 갯수에 따라 소켓을 따로 생성해야되기 때문


class mingcorn():
    def __init__(self):
        pass

    # app , host : 127.0.0.1, port :5000
    # run server
    def run(self, app:mingxn_API, host:str, port:int):
        self.__num_client = 0
        self.__client_socket = []
        self.__service_thread = []
        self.__port_thread = []
        for pt in port:
            app.execute_get
        app.execute_socket_platform(host, port, asgi = True)
        self.__asyc_server(app=app)

    def __asyc_server(self, app:mingxn_API):
        while True:
            client_socket, client_address = app.open_server_async()
            if client_socket:
                client_thread = Thread(target=app.execute_service, )

                self.__service_thread




app = mingxn_API()

#uvicorn.run(app, host, port)

@app.get("/")
def home():
    print("hello world")
    return

for i in range(3):
    time.sleep(1)

route = "/"
app.execute_function(route)

