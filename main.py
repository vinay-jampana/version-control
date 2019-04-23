import os
def add_func():
    cwd = os.getcwd()
    final_dir = os.path.join(cwd,'.user')
    os.mkdir(final_dir)
    print('new directory is created')
def commit_func():
     print('commit is working')
def push_func():
     print('push is working')
