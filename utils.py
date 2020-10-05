t#信息加密

from werkzeug.security import generate_password_hash, check_password_hash

def encrypt(pwd):
    return generate_password_hash(pwd)

def checkPwd(pwd, hashedPwd):
    return check_password_hash(hashedPwd,pwd)