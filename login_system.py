# archivo-entrada.py
u = open('user.txt', 'r')
usr = u.read()
p = open('pass.txt', 'r')
psw = p.read()
# f.close()
user = input('User name: ')
password = input('Password:')
if user == usr and password == psw:
    print('Your user name and password are corrects.')
else:
    print('User name and/or password incorrect. Try again.')

"""
IMPORTANT FOR CUMMING PROJECTS
FOR WRITE IN A TXT FILE
# archivo-salida.py
f = open('write_file.txt', 'w')
f.write('hola mundo')
f.close()
"""
