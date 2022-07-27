import threading
from typing import ClassVar


class Singleton:

    __instance__: ClassVar = None  # we use this static variable

    __lock = threading.Lock()

    def __repr__(self) -> str:  # represent object Singleton() as string when print
        return '♣♥ ---- instantiated singleton object is returned in a method and printed ♣☺☻♥'

    def __instantiate():
        with __class__.__lock:
            print('-->instantiate for first time<--')
            __class__.__instance__ = __class__()

    # @classmethod
    @staticmethod
    def getInstance():  # protected called from class and object in same package

        if not __class__.__instance__:
            __class__.__instantiate()

        return __class__.__instance__

    def makeAction(self):
        print('make action')


if __name__ == '__main__':

    print(Singleton.getInstance())

    # overwrite static var (__instance__) manually
    Singleton.__instance__ = 8
    print(Singleton.getInstance())
