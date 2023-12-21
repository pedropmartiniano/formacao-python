from modules.usersInMemory import users_db

class Create_user_controller:
    def handler(self, user):
        if not any(user.get(key) for key in ['username', 'email', 'password']):
            return {'message': 'Informações incompletas'}
        
        user = {'id': len(users_db) + 1,
                'username': user['username'],
                'email': user['email'],
                'password': user['password']}
        
        users_db.append(user)

        print(users_db)

        return user