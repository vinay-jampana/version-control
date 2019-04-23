import os
from user import create_user


def add_func():
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
        print('yo')
        create_user()

        # create hidden directory with sub directories of heads, track, objects, users --> user(file)

        heads_dir = os.path.join(cwd, '.vcs/heads')
        os.mkdir(heads_dir)

        # set current user at every login



        # create a copy of single file present in the location -- take input from user
        # if there is no file then prompt user to create a file and then run add
        # create an object an objects folder with file name as hash of some parameter unique to the object
        # create a head to specify which user is operating
        # create a track file to notify previous commits -- no initial commits


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
