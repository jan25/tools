from dataclasses import dataclass

@dataclass
class _User:
    id_: int
    first_name: int
    last_name: int
    email: str = ''
    phone: str = ''

_data = [
    _User(1, 'Lewis', 'Hamilton'),
    _User(2, 'Valterri', 'Bottas'),
    _User(3, 'Max', 'Verstappen'),
    _User(4, 'Alex', 'Albon'),
    _User(5, 'Sebastian', 'Vettel'),
    _User(6, 'Daniel', 'Ricciardo'),
    _User(7, 'George', 'Russell')
]

def get_users():
    pass

def get_user(user_id):
    pass

def update_user(user_id, json_data):
    pass

def create_user(json_data):
    pass

def delete_user(user_id):
    pass