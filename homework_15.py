# class Bot:
#    def __init__(self, name):
#        self.name = name
#    def send_message(self, message):
#        self.message = message
#        print(self.message)
#    def say_name(self):
#        print(self.name)

# borow = Bot("Xryak")
# borow.say_name()
#
# borow.send_message("Hello")

# class TelegramBot(Bot):
#     url = None
#     chat_id = None
#     # def __init__(self, url):
#     #     self.url = None
#     # def chat_id(self, chat_id):
#     #     self.chat_id = None
#     def set_url(self, url):
#         self.url = url
#     def set_chat_id(selfself, chat_id):
#         self.set_chat_id = chat_id
#     def send_message(self, message):
#         super().send_message()
#         print(f"{self.name} {self.message} {self.chat_id} {self.url}")


# borow = Bot("Xryak")
# borow.say_name()
#
# borow.send_message("Hello")

# class MyStr(str):
#     def __str__(self):
#         return super().__str__().upper()
#
#
# s = MyStr("Hello, World!")
# print(str(s))



# class User:
#     def __init__(self, name):
#         self.name = name
#
#     def __eq__(self, other):
#         if isinstance(other, User):
#             return self.name.lower() == other.name.lower()
#         return False
#
#
# user1 = User("John")
# user2 = User("joHN")
# print(user1 == user2)