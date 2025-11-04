
from sqlalchemy.orm import Session
from schema import UserSchema
from model import User
from security import get_password_hash


def criar_usuario_db(db: Session, user: UserSchema):
    db_user = User(name=user.name, email=user.email,password = get_password_hash(user.password))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_usuario_db(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_email(db: Session, email:str):
    return db.query(User).filter(User.email == email).first
    
def get_users(db:Session):
    return db.query(User)
