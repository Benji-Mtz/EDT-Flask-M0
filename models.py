from flask_login import UserMixin

db_user = []

class User(UserMixin):
    def __init__(self, id, firstname, lastname, email, password) -> None:
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password
        
    def verify_password(self, password):
        if self.password == password:
            return True
        else:
            return False

  
def get_user(email):
    for user in db_user:
        if user.email == email:
            return user
        return None