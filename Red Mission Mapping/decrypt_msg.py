import hashlib
import base64

from cryptography.fernet import Fernet

keyword = b'TRUTH'
encode_string = b'gAAAAABaUXStIpjRWJTrbWGOB45IyRpbb8Zyl1sdktcSeOL0zpH-_Oxd2nXVjeph_fGybthCci75lTd0z5SycthFo-5uoFxZqeBTdDc_n9uq3FdZk75gYFAWIRSGlAqlBQlcqkNhVx3W3w7rTaCAhCrHijeyTtxq53S3ab6fLHUw3KPHx2LtdurISe5ArhrmG9IOepnzGzBBTaTgCfoAmbITCWbp_5cdQQ=='

hash_object = hashlib.sha3_256(keyword)
key = hash_object.digest()

fernet_key = base64.urlsafe_b64encode(key)
cipher = Fernet(fernet_key)
print(cipher.decrypt(encode_string))
