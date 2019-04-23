import os
import hashlib
import base64
from pathlib import Path


def create_user():
    username = input('Please select a username :     ')
    password = input('please select a password :     ')
    check_user_exists(username, password)


def check_user_exists(username, password):

    cwd = os.getcwd()

    if username != '' and password != '':

        # check if username is already taken

        if os.path.isfile('.vcs/users/username.txt'):
            print('username is already taken')
            create_user()
        else:
            user_dir = os.path.join(cwd, '.vcs/users')
            os.mkdir(user_dir)

            # if username == true --> create uid

            uid = base64.b64encode(hashlib.sha1(str.encode(username)).digest())
            password_hash = base64.b64encode(hashlib.sha512(str.encode(password)).digest())

            # store it in users/uid

            create_user_file(username, uid.decode(), password_hash.decode())

            print(uid.decode())


def create_user_file(username, uid, password_hash):
    Path('.vcs/users/' + username + '.txt').touch()

    # write to file --> username , password hash
    # line1: username
    # line2: uid
    # line3: passwordHash

    u_file = open('./.vcs/users/' + username + '.txt', 'w')
    user_details = [username, uid, password_hash]
    u_file.write('\n'.join(user_details))
