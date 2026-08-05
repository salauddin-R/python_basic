class class_mate:
    def __init__(self,name,groups):
        self.__name=name
        self.__groups=groups

    def __Print_data(self):
        print(f"He is {self.__name} and his group is {self.__groups}")

    def printCall(self):
        self.__Print_data()

ob = class_mate("Rony","A")
ob.printCall()