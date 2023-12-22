from modules.getUser import Get_user_by_id_controller
from modules.usersInMemory import users_in_memory

class Edit_user_controller:
    def handle(self, id: str, userEdited: dict):
        get_user = Get_user_by_id_controller()
        user = get_user.handle(id)

        if user is None:
            return {'Message': 'User not found.'}
        
        index = users_in_memory.index(user)

        new_user = {'id': id, **userEdited}

        users_in_memory[index] = new_user

        print(users_in_memory)
        return new_user