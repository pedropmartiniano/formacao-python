from modules.usersInMemory import users_in_memory

class Create_user_controller:
    def handler(self, user):
        if not any(user.get(key) for key in ['username', 'email', 'password']):
            return {'message': 'Informações incompletas'}
        
        user = {'id': len(users_in_memory) + 1, **user}
                # 'username': user['username'],
                # 'email': user['email'],
                # 'password': user['password']}
        
        users_in_memory.append(user)

        print(users_in_memory)

        return user