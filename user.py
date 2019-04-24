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

        if os.path.isfile('.vcs/users/' + username + '.txt'):
            print('username is already taken')
            create_user()
        else:

            if os.path.isdir('.vcs/users'):
                pass
            else:
                user_dir = os.path.join(cwd, '.vcs/users')
                os.mkdir(user_dir)

            # if username == true --> create uid

            uid = base64.b64encode(hashlib.sha1(str.encode(username)).digest())
            password_hash = base64.b64encode(hashlib.sha512(str.encode(password)).digest())

            # store it in users/uid

            create_user_file(username, uid.decode(), password_hash.decode())

            # print(uid.decode())


def create_user_file(username, uid, password_hash):
    Path('.vcs/users/' + username + '.txt').touch()

    # line1: username
    # line2: uid
    # line3: passwordHash
    # line4: selected file

    vcs_file_include = input('Enter The Filename you want to add to version control :     ')

    u_file = open('./.vcs/users/' + username + '.txt', 'w')
    user_details = [username, uid, password_hash, vcs_file_include]
    u_file.write('\n'.join(user_details))

    temp_val = True

    create_obj_file(username, uid, vcs_file_include, temp_val)


def create_obj_file(username, uid, vcs_file_include, temp_val):

    # file to include
    # check if file is already added <--

    if os.path.isfile(vcs_file_include):

        # proceed to create object
        # set obj_id as md5(username, first few bits of sha1(selected file value))

        with open(vcs_file_include, encoding='utf8') as f:
            obj_file_value = f.read().strip()
            obj_file_value_hash = base64.b64encode(hashlib.md5(str.encode(obj_file_value)).digest())
            temp1 = obj_file_value_hash
            obj_id = (base64.b64encode(hashlib.md5(str.encode(temp1.decode() + username)).digest())).decode()
            print(obj_id)

            # set obj file value as contents of the file

            Path('.vcs/objects/' + obj_id + '.txt').touch()
            if os.path.isfile('.vcs/objects/' + obj_id + '.txt'):
                with open('.vcs/objects/' + obj_id + '.txt', 'w') as of:
                    of.write(obj_file_value)

                # send the obj_id to track_file to set user_obj
                create_track_file(username, uid, obj_id, temp_val)
            else:
                print('Please Try Again')
                create_obj_file(username, uid, vcs_file_include, temp_val)

    else:
        print('No File Present with that filename in the current directory')
        create_obj_file(username, uid, vcs_file_include, temp_val)
    pass


def create_track_file(username, uid, obj_id, a):

    # create a track file specific to a user

    if os.path.isdir('.vcs/tracks'):
        track_file_id = uid

        # create append obj_id to track_file
        if os.path.isfile('.vcs/tracks/' + uid + '.txt'):
            pass
        else:
            Path('.vcs/tracks/' + uid + '.txt').touch()
        with open('.vcs/tracks/' + uid + '.txt', 'a') as tf:
            tf.write(obj_id)
            tf.write('\n')

            # send track_file details to head

            if a:
                val = True
                create_head_file(username, uid, track_file_id, val)
            else:
                val = False
                create_head_file(username, uid, track_file_id, val)

    else:
        print('No Such Directory')


def create_head_file(username, uid, track_file_id, val):

    # line1: username
    # line2: uid
    # line3: track file

    if os.path.isfile('.vcs/heads/' + uid + '.txt'):
        pass
    else:
        Path('.vcs/heads/' + uid + '.txt').touch()

    if val:
        head_file = open('./.vcs/heads/' + uid + '.txt', 'a')
        head_details = [username, uid, track_file_id]
        head_file.write('\n'.join(head_details))
    else:
        pass


