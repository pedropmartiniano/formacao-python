from fastapi import FastAPI, Body, params
from modules.createUser import Create_user_controller
from modules.getUsers import Get_users_controller
from modules.deleteUser import Delete_user_controller
from modules.getUser import Get_user_by_id_controller
from modules.editUser import Edit_user_controller

def routes(app: FastAPI):
    @app.get('/')
    def hello():
        return {'Hello': 'World'}
    
    @app.post('/user/create')
    def createUser(user: dict = Body(None)):
        if user == None:
            return {'Message': 'Body missing'}
        
        create_user = Create_user_controller()
        return create_user.handler(user)
    
    @app.get('/user/get-all')
    def getAllUsers():
        get_users = Get_users_controller()
        return get_users.handle()
    
    @app.delete('/user/delete/{id}')
    def deleteUser(id: str = None):
        if id == None:
            return {'Message': 'User id param missing'}
        
        deleteUser = Delete_user_controller()
        return deleteUser.handle(id)

    @app.get('/user/get/{id}')
    def getUserById(id: str = None):
        if id == None:
            return {'Message': 'User id param missing'}
        
        get_user = Get_user_by_id_controller()
        return get_user.handle(id)
    
    @app.put('/user/update/{id}')
    def updateUser(id: str, user: dict = Body(...)):
        if any((id, user)) is None:
            return {'Message': 'Informações incompletas.'}
        
        edit_user = Edit_user_controller()
        return edit_user.handle(id, user)