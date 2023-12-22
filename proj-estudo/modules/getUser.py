from modules.usersInMemory import users_in_memory

class Get_user_by_id_controller:
    def handle(self, id):
        user = next((userId for userId in users_in_memory if userId['id'] == id), None)
        
        print(user)
        return user
        # userId = None
        # for user in users_in_memory:
        #     if user['id'] == id:
        #         userId = user


        # print(userId)
        # return userId