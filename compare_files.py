import hashlib
import base64
filepath = 'app.py'
filepath2 = 'app.py'

with open(filepath) as fp:
    line = fp.readline()
    lines_list1 = []
    cnt = 1
    while line:
        lines_list1.append(line.strip())
        line = fp.readline()
        print(lines_list1[cnt - 1])
        cnt += 1
hashed_lines_list1 = []
print (len(lines_list1))
n = len(lines_list1)
i = 1
for i in range(n):
    hashed_lines_list1.append(base64.b64encode(hashlib.sha1(str.encode(lines_list1[i-1])).digest()))
    print(hashed_lines_list1[i-1])
    i +=1

with open(filepath2) as fp2:
    line = fp2.readline()
    lines_list2 = []
    cnt = 1
    while line:
        lines_list2.append(line.strip())
        line = fp2.readline()
        print(lines_list2[cnt - 1])
        cnt += 1
hashed_lines_list2 = []
print (len(lines_list2))
n2 = len(lines_list2)

i = 1
for i in range(n2):
    hashed_lines_list2.append(base64.b64encode(hashlib.sha1(str.encode(lines_list2[i-1])).digest()))
    print(hashed_lines_list2[i-1])
    i +=1

if hashed_lines_list1 == hashed_lines_list2:
        print('same file. commit is unnecessary')




