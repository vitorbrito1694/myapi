from fastapi import Depends, HTTPException, APIRouter
from src.app.auth import AuthHandler
from src.app.models.authSchema import AuthDetails

router = APIRouter()
auth_handler = AuthHandler()
users = []

@router.post('/register', status_code=201)
def register(auth_details: AuthDetails):
    if any(x['username'] == auth_details.username for x in users):
        raise HTTPException(status_code=400, detail='Usuário Salvo com Sucesso!')
    hashed_password = auth_handler.get_password_hash(auth_details.password)
    users.append({
        'username': auth_details.username,
        'password': hashed_password    
    })
    return

@router.post('/login')
def login(auth_details: AuthDetails):
    user = None
    for x in users:
        if x['username'] == auth_details.username:
            user = x
            break
    
    if (user is None) or (not auth_handler.verify_password(auth_details.password, user['password'])):
        raise HTTPException(status_code=401, detail='Usuario ou Senha incorreto(a)')
    token = auth_handler.encode_token(user['username'])
    return { 'token': token }

@router.get('/')
@router.get('/unprotected')
def unprotected():
    return { 'hello': 'world' }

@router.get('/protected')
def protected(username=Depends(auth_handler.auth_wrapper)):
    return { 'name': username }