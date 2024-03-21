from model import Test_Model

class Master_Controller():
    def __init__(self) -> None:
        self.model = Master_Model()

    def sign(self, data, type):
        user_controller = User_Controller(self.model.get_user_model())
        user_controller.set_data(data)
        result = user_controller.process(type)
        return result


class User_Controller():
    def __init__(self, model) -> None:
        self.model =model
        pass

    def set_data(self, data):
        self.model.set_data(data)
        return 

    def process(self, type):
        if type == "sign_in":
            sign_in = Sign_In()
            result = sign_in.login()
        elif type == "sign_up":
            sign_up = Sign_Up()
            result = sign_in.sign_up()

        return result
    

"""
result = {uid : 0, detail : "default"}


"""

class Sign_Up():
    def __init__(self) -> None:
        pass
    def sign_up(self):
        #  비지니스 로직을 수행
        # 회원가입 할꺼임
        result = { "uid" : 0, "detail" : "default"}
        return result


class Sign_In():
    def __init__(self) -> None:
        pass
    def login(self):
        return


class Data_Add_Controller():
    def __init__(self):
        self.test_model = Test_Model()

    def get_data(self):
        self.__add_data()
        return self.test_model.get_data()
    
    def __add_data(self):
        sum = self.test_model.get_data()
        sum += 10
        self.test_model.set_data(sum)
        return