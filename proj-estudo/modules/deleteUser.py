from modules.usersInMemory import users_in_memory

class Delete_user_controller:
    def handle(self, id: str):
        user = next((us for us in users_in_memory if us['id'] == id), None)

        # userId = None
        # for user in users_in_memory:
        #     if user['id'] == id:
        #         userId = user
                
        if not user:
            return {'Message': 'User dont exists'}
        
        users_in_memory.remove(user)

        print(users_in_memory)
        return users_in_memory