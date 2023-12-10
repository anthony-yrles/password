import hashlib

def hashing(password):
    password_bytes = password.encode('utf-8')
    hash_password = hashlib.sha256()
    hash_password.update(password_bytes)
    hashed_password = hash_password.hexdigest()
    return(hashed_password)