import os
from user import create_user
from user import create_obj_file
import hashlib
import base64


class main_func:

    def __init__(self):
        print('new Instance created')

    def init_func(self):
        cwd = os.getcwd()
        # print(cwd)
        if os.path.isdir('./.vcs'):
            print('Already a VCS Project')

            # check for user presence

            if os.listdir('./.vcs/users'):
                print('print user exists')
            else:
                # ask to add user or create new project
                print('user do not exit')
            # if no user -- create a user
            # if user --> check for heads and tracks and objects
        else:
            main_dir = os.path.join(cwd, '.vcs')
            os.mkdir(main_dir)

            # create objects dir

            obj_dir = os.path.join(cwd, '.vcs/objects')
            os.mkdir(obj_dir)

            # create tracks dir

            tracks_dir = os.path.join(cwd, '.vcs/tracks')
            os.mkdir(tracks_dir)

            # create heads dir

            heads_dir = os.path.join(cwd, '.vcs/heads')
            os.mkdir(heads_dir)

            create_user()

    def commit_func(self):

        # check username and password in heads and commit accordingly

        if os.listdir('.vcs/users/'):
            input_username = input('Enter The username :     ')
            input_password = input('Enter The Password :     ')

            with open('.vcs/users/' + input_username + '.txt') as f:
                fl = f.readline().replace('\n', '')
                lines = f.readlines()
                tl = lines[1].replace('\n', '')
                fourthl = lines[-1].replace('\n', '')

                input_password_hash = base64.b64encode(hashlib.sha512(str.encode(input_password)).digest()).decode()
                input_uid = base64.b64encode(hashlib.sha1(str.encode(input_username)).digest()).decode()

                if input_password_hash == tl and input_username == fl:

                    # get value of last committed file from heads --> track --> object --> value

                    track_file = open('./.vcs/tracks/' + input_uid + '.txt', 'r')
                    track_file_lines = track_file.readlines()
                    cur_obj_file_name = track_file_lines[-1].replace('\n', '')
                    previous_commit_file_name = open('./.vcs/objects/' + cur_obj_file_name + '.txt', 'r')

                    previous_commit_file_value = previous_commit_file_name.read()
                    current_commit_file_value = open(fourthl, 'r').read()

                    # check for changes in file

                    previous_commit_file_value_lines = self.convert_to_lines(self, previous_commit_file_value)
                    current_commit_file_value_lines = self.convert_to_lines(self, current_commit_file_value)

                    previous_commit_file_value_lines_hash = self.get_hash(self, previous_commit_file_value_lines)
                    current_commit_file_value_lines_hash = self.get_hash(self, current_commit_file_value_lines)

                    comparission_result = self.compare_lists(self, previous_commit_file_value_lines_hash, current_commit_file_value_lines_hash)

                    if comparission_result:
                        print('No Need For Commit, Track is upto date')
                    else:

                        # make entries to objects, track

                        temp_val = False
                        create_obj_file(input_username, input_uid, fourthl, temp_val)

                else:
                    print('Check User Name and Password Again')
                    self.commit_func()

        else:
            print('initialize vcs')

    def convert_to_lines(self, string):
        li = list(string.split('\n'))
        return li

    def get_hash(self, l):
        h = []
        for x in l:
            temp = base64.b64encode(hashlib.md5(str.encode(x)).digest())
            h.append(temp)
        return h

    def compare_lists(self, a, b):
        initial_status = False
        if len(a) != len(b):
            return False
        else:
            # check element vise
            for x in range(0, len(a)):
                if a[x] != b[x]:
                    break
                else:
                    initial_status = True
            return initial_status

    def push_func(self):
        print('Database is not included')
