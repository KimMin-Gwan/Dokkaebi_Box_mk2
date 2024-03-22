
# 경로와 함수를 매핑하기 위한 딕셔너리
route_mapping = {}
# 경로와 함수를 매핑하는 데코레이터 함수
def route_decorator(route):
    def decorator(func):
        route_mapping[route] = func
        return func
    return decorator

# 경로에 해당하는 함수를 실행하는 함수
def execute_function(route):
    if route in route_mapping:
        return route_mapping[route]()
    else:
        print("Invalid route")

# 사용 예시
@route_decorator('/home')
def home_page():
    print('home')
    return "Welcome to the home page!"

@route_decorator('/about')
def about_page():
    return "This is the about page!"

if __name__ == "__main__":
    route = "/home"
    result = execute_function(route)
    print(result)






