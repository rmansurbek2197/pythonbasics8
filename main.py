class User:
    def __init__(self, id, username):
        self.id = id
        self.username = username

class Message:
    def __init__(self, id, text, user):
        self.id = id
        self.text = text
        self.user = user

class ChatRoom:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.users = []
        self.messages = []

    def add_user(self, user):
        self.users.append(user)

    def remove_user(self, user):
        self.users.remove(user)

    def add_message(self, message):
        self.messages.append(message)

    def get_messages(self):
        return self.messages

class ChatApplication:
    def __init__(self):
        self.users = []
        self.chat_rooms = []

    def add_user(self, user):
        self.users.append(user)

    def remove_user(self, user):
        self.users.remove(user)

    def add_chat_room(self, chat_room):
        self.chat_rooms.append(chat_room)

    def remove_chat_room(self, chat_room):
        self.chat_rooms.remove(chat_room)

    def get_user(self, id):
        for user in self.users:
            if user.id == id:
                return user
        return None

    def get_chat_room(self, id):
        for chat_room in self.chat_rooms:
            if chat_room.id == id:
                return chat_room
        return None

app = ChatApplication()

user1 = User(1, "John")
user2 = User(2, "Jane")

app.add_user(user1)
app.add_user(user2)

chat_room = ChatRoom(1, "General")
app.add_chat_room(chat_room)

chat_room.add_user(user1)
chat_room.add_user(user2)

message1 = Message(1, "Hello", user1)
message2 = Message(2, "Hi", user2)

chat_room.add_message(message1)
chat_room.add_message(message2)

for message in chat_room.get_messages():
    print(message.text)

for user in chat_room.users:
    print(user.username)