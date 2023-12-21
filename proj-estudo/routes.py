from fastapi import FastAPI, Body
from modules.createUser import Create_user_controller

def routes(app: FastAPI):
    @app.get('/')
    def hello():
        return {'Hello': 'World'}
    
    @app.post('/user/create')
    def createUser(user: dict = Body(None)):
        if user == None:
            return {'message': 'Body missing'}
        
        create_user = Create_user_controller()
        return create_user.handler(user)