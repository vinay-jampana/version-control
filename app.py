import argparse
from main import init_func
from main import commit_func
from main import push_func
from user import create_user

parser = argparse.ArgumentParser()
parser.add_argument("--init", help='add file to the database', action="store_true")
parser.add_argument("--commit", help='commit file to the database', action="store_true")
parser.add_argument("--push", help='push file to the database', action="store_true")
parser.add_argument("--newUser", help='add new user', action="store_true")


args = parser.parse_args()
if args.init:
    init_func()
if args.commit:
    commit_func()
if args.push:
    push_func()
if args.newUser:
    create_user()

