class Singleton:
    __instance = None

    def __init__(self):
        if Singleton.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Singleton.__instance = self

    @staticmethod
    def get_instance():
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance

s1 = Singleton.get_instance()
s2 = Singleton.get_instance()

print(s1 == s2)  # Output: True
