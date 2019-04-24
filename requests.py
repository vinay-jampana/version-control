from flask import Flask
from flask_cors import CORS
from flask_restful import Resource, Api
from flask import request
from main import commit_func_alt
import os
import hashlib
import base64
from pathlib import Path


app = Flask(__name__)
CORS(app)
api = Api(app)


class getCode(Resource):
    username = ''
    password = ''

    def post(self):
        # verify uid and password and send file data accordingly
        recv_data = request.get_json()
        self.username = recv_data['username']
        self.password = recv_data['password']
        print(self.username, self.password)
        if os.path.isfile('.vcs/users/' + self.username + '.txt'):
            with open('.vcs/users/' + self.username + '.txt') as f:
                lines = f.readlines()
                fl = f.readline().replace('\n', '')
                pl = lines[1].replace('\n', '')
                ll = lines[-1]
                with open('test.js', 'r') as rf:
                    rf_lines = rf.readlines()
                    print(rf_lines)
                    return rf_lines


class saveCode(Resource):

    def post(self):
        saved_code = request.get_json()
        print(saved_code['savedCode'])
        self.change_code(saved_code['savedCode'])


    def change_code(self, a):
        with open('test.js', 'w') as f:
            f.write(a)


class commitCode( getCode):

    def post(self):
        data_recv = request.get_json()
        commit_code = data_recv['commitedCode']
        usser = data_recv['username']
        with open('test.js', 'w') as f:
            f.write(commit_code)
        commit_func_alt(usser, getCode.password)

api.add_resource(getCode, '/')
api.add_resource(saveCode, '/saveCode')
api.add_resource(commitCode, '/commitCode')

if __name__ == '__main__':
    app.run(debug=True)
