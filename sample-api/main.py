from flask import Flask
import users

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/all_users')
def all_users():
    return users.get_users()

@app.route('/get_user/<int:user_id>/')
def get_user(user_id):
    u = users.get_user(user_id)
    if u is None:
        return 'User not found'
    return u

@app.route('/create_user/', methods=['POST'])
def create_user():
    json_data = '' # TODO
    user_id = users.create_user(json_data)
    return users.get_user(user_id)

@app.route('/update_user/<int:user_id>/', methods=['POST'])
def update_user(user_id):
    json_data = '' # TODO
    users.update_user(user_id, json_data)
    return users.get_user(user_id)

@app.route('/delete_user/<int:user_id>/', methods=['DELETE'])
def delete_user(user_id):
    users.delete_user(user_id)
    return 'User deleted'

# Use `flask run` instead. Also, see `make dev`.
if __name__ == '__main__':
    app.run(port=5000)