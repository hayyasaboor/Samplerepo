class Ship:
    __slots__ = ["__name", "__capacity"]
    def __init__(self, name, capacity):
        self.__name = name
        self.__capacity = capacity
    def get_name(self):
        return self.__name
    def get_capacity(self):
        return self.__capacity  
    def set_capacity(self, capacity):
        if capacity > 0:
            self.__capacity = capacity
        else:
            print("Invalid: Capacity must be postive")
    def print_ship(self):
        print (f"Ship's Name: {self.__name} | Capacity: {self.__capacity} tons")
def main():
    ship1= Ship ('Titanic', 800)
    ship2 = Ship ('NadineUltra', 1800)
    ship1.print_ship()
    ship2.print_ship()
    ship1.set_capacity(5000)
    ship2.set_capacity(9500)
    print("After Upgrade: ")
    ship1.print_ship()
    ship2.print_ship()

if __name__ == "__main__":
    main()
# class Ship:
#     __slots__= ['__name', '__capacity']
#     def __init__(self, name, capacity):
#         self.__name = name
#         self.__capacity = capacity
#     def get_name(self):
#         return self.__name
#     def get_capacity(self):
#         return self.__capacity
#     def set_capacity(self, capacity):
#         if capacity >= 0:
#             self.__capacity = capacity
#         else:
#             print("Capacity cannot be negative.")
#     def print_ship(self):
#         print(f"Ship Name: {self.__name}, Capacity: {self.__capacity} tons")
# def main():
#     ship1= Ship("Titanic", 52310)
#     ship2= Ship("Queen Mary 2", 76000)
#     ship1.print_ship()
#     ship2.print_ship()
#     ship1.set_capacity(54000)
#     ship2.set_capacity(-100)
#     print("After updating capacity:")
#     ship1.print_ship()
#     ship2.print_ship()
# if __name__ == "__main__":
#     main()