from fastapi import FastAPI,status,Depends,HTTPException
from schema import UserSchema,UserPublic
from sqlalchemy.orm import Session
import crud
from .database import  get_db
import sqlite3


app = FastAPI()
conn = sqlite3.connect('mydatabase.db',check_same_thread=False)
cursor = conn.cursor()

@app.post('/users/', status_code=status.HTTP_201_CREATED,response_model=UserPublic)
def create_user(user: UserSchema,db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)

    if db_user:
        raise HTTPException(status_code=400, detail="Email já cadastrado")
    
    return crud.criar_usuario_db(db=db, user=user)

@app.get("/users/{user_id}", response_model=UserPublic)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_usuario_db(db, user_id=user_id)

    if db_user is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    
    return db_user

@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_usuario_db(db, user_id=user_id)

    if db_user is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    
    crud.delete_user(db=db, user_id=user_id)

    return {"message": "Usuário deletado com sucesso"}

@app.post("/login")
def login(db: Session = Depends(get_db)):
    pass