import os
from user import create_user


def init_func():
    cwd = os.getcwd()
    print(cwd)
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


def commit_func():
    print('commit is working')

    # check username and password in heads and commit accordingly
    # give option to login as new user -- if new user logged in then recreate heads and track
    # check for changes in each file line vise
    # create a hash to specify object name
    # add object to objects folder
    # add object name to track to notify previous commits


def push_func():
    print('push is working')
