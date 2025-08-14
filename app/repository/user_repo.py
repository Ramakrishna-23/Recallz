from sqlalchemy.orm import Session 
from app.db import models

# all the possbile actions for users

# create new user
def create_new_user(db:Session, name:str, email:str, password:str):
    new_user = models.User(
        name=name,
        email=email,
        password=password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
    
# 1. get_user_id => user.py => get
def get_user_by_id(db:Session, user_id:str):
    return db.query(models.Users).filter(models.User.id == user_id).first()


# 3. put_user_name => user.py => put
def put_user_name(db:Session, user_id:str, name:str ):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        return None

    user.name = name
    db.commit()
    db.refresh(user)
    return user



# 4. put_email_id => user.py => put
def put_email_id(db:Session, user_id:str, email:str):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        return None
    
    user.email = email
    db.commit()
    db.refresh(user)
    return user

# 5. put_password => user.py => put
def put_password(db:Session, user_id:str, password:str):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        return None
    
    user.password = password
    db.commit()
    db.refresh(user)
    return user

# 6. delete_user => user.py => del
def delete_user(db:Session, user_id:str):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        return None
    
    db.delete(user) 
    db.commit()
    return {"message": f"User with ID {user_id} has been deleted successfully."}


