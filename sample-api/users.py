from dataclasses import dataclass
import json

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
    return json.dumps(_data)

def get_user(user_id):
    for user in _data:
        if user.id_ == user_id:
            return json.dumps(user)

def update_user(user_id, json_data):
    for i, user in enumerate(_data):
        if user.id_ == user_id:
            data[i] = old_user.__dict__.update(json_data)
            return True
    return False

def _next_id():
    return 1 + max(u.id_ for u in data)

def create_user(json_data):
    if 'first_name' not in json_data:
        return None
    if 'second_name' not in json_data:
        return None

    json_data['id_'] = _next_id()
    u = _User(id_, '', '')
    u.__dict__.update(json_data)
    data.append(u)

def delete_user(user_id):
    i = 0
    while i < len(data):
        if data[i].id_ == user_id:
            break
        i += 1
    if i == len(data): return False

    data = data[:i] + data[i + 1:]
    return True