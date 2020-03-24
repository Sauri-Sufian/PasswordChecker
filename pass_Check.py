# url = 'https://api.pwnedpasswords.com/range/' + query

import hashlib
import requests
import sys

def response_Check(sample):
    url = 'https://api.pwnedpasswords.com/range/'+ sample
    res = requests.get(url)
    if res.status_code !=200:
        raise RuntimeError(f'Fetching error : {res.status_code},check api again')
    return res

def check_pass(password):
    sha1_pass= hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first,rest=sha1_pass[:5],sha1_pass[5:]
    response =response_Check(first)
    return check_pwned(response,rest)

def check_pwned(hashes,hashes_remain):
    new_hashes=(line.split(':')for line in hashes.text.splitlines())
    for i,count  in new_hashes:
        if i== hashes_remain:
            return count
    return 0
def controller(args):
    for i in args:
        print(i)
        x=check_pass(i)
        if x:
            print(f'your password {i} was found {x} times')
        else:
            print('strong one')

# passwords=()
# with  open('passwords.txt','r') as file:
#     passwords=file.readlines()
#     print(passwords)
#     #controller(passwords)

controller(sys.argv[1:])