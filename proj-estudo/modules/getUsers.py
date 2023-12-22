from modules.usersInMemory import users_in_memory

class Get_users_controller:
    def handle(self):
        print(users_in_memory)
        return users_in_memory
