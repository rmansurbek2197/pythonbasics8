class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Message:
    def __init__(self, id, text, user_id):
        self.id = id
        self.text = text
        self.user_id = user_id

class ChatRoom:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.users = []
        self.messages = []

    def add_user(self, user):
        self.users.append(user)

    def add_message(self, message):
        self.messages.append(message)

class ChatApplication:
    def __init__(self):
        self.users = []
        self.chat_rooms = []
        self.messages = []

    def create_user(self, id, name):
        user = User(id, name)
        self.users.append(user)
        return user

    def create_chat_room(self, id, name):
        chat_room = ChatRoom(id, name)
        self.chat_rooms.append(chat_room)
        return chat_room

    def send_message(self, chat_room_id, user_id, text):
        chat_room = next((cr for cr in self.chat_rooms if cr.id == chat_room_id), None)
        user = next((u for u in self.users if u.id == user_id), None)
        if chat_room and user:
            message = Message(len(self.messages), text, user_id)
            self.messages.append(message)
            chat_room.add_message(message)
            return message
        else:
            return None

    def get_messages(self, chat_room_id):
        chat_room = next((cr for cr in self.chat_rooms if cr.id == chat_room_id), None)
        if chat_room:
            return chat_room.messages
        else:
            return []

    def get_users(self, chat_room_id):
        chat_room = next((cr for cr in self.chat_rooms if cr.id == chat_room_id), None)
        if chat_room:
            return chat_room.users
        else:
            return []

app = ChatApplication()
user1 = app.create_user(1, 'John')
user2 = app.create_user(2, 'Jane')
chat_room = app.create_chat_room(1, 'General')
chat_room.add_user(user1)
chat_room.add_user(user2)
app.send_message(1, 1, 'Hello')
app.send_message(1, 2, 'Hi')
print([m.text for m in app.get_messages(1)])
print([u.name for u in app.get_users(1)])