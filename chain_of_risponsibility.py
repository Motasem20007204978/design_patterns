
from abc import ABC, abstractmethod

class Request:
    
    __request_val:int = None
    __request_description:str = None
    
    def __init__(self, value:int, description:str):
        Request.__request_val = value
        Request.__request_description = description

    def get_val() -> int:
        return Request.__request_val

    def get_desc() -> str:
        return Request.__request_description


class Handler(ABC):

    def __init__(self) -> None:
        self._successor = None               

    def set_successor(self, successor):
        self._successor = successor

    @abstractmethod
    def handleRequestClient(self, request:Request) -> bool:
        pass

    def handleRequest(self, request:Request):
        handledByThisNode = self.handleRequestClient(Request)
        
        if self._successor and not handledByThisNode:
            self._successor.handleRequest(request)


class Concrete_Handler_1(Handler):

    def __init__(self) -> None:
        super().__init__()

    def handleRequestClient(self, request: Request) -> bool:
        if request.get_val() < 0:
            print(f'negative integer is handled by {__class__.__name__}')
            return True
        else:
            return False


class Concrete_Handler_2(Handler):

    def __init__(self) -> None:
        super().__init__()

    def handleRequestClient(self, request: Request) -> bool:
        if request.get_val() > 0:
            print(f'positive integer is handled by {__class__.__name__}')
            return True
        else:
            return False


class Concrete_Handler_3(Handler):

    def __init__(self) -> None:
        super().__init__()

    def handleRequestClient(self, request: Request) -> bool:
        if request.get_val() == 0:
            print(f'zero value is handled by {__class__.__name__}')
            return True
        else:            
            return False


if __name__ == '__main__':

    h1 = Concrete_Handler_1()
    h2 = Concrete_Handler_2()
    h3 = Concrete_Handler_3()

    h1.set_successor(h2)
    h2.set_successor(h3)

    h1.handleRequest(Request(5, 'positive'))

    h1.handleRequest(Request(0, 'zero'))
