import hashlib
import base64

from cryptography.fernet import Fernet

keyword = b'65537'
encode_string = b'gAAAAABaSsmdCFRxbqA6n-L0CMIMuhn26uGiIk5Wtx-V7wEPLBZYA67nGbNWyZziGyorwIlHqp3M5xrtzQj5tCab8XfBRCmdJXZYD1Fwp68AtD8WEMhblQ4I2DKDNFzqULH1DDETry3ptZnGZUgVo5gdDlnihqu1_oX-KboNpyRQ6J0DmeWTsm3L31btF_O6sX81rj3rBVI0qVuT7QdRT2burisQRnw5htA05llYgc1_fMkN_PSxCwY='

hash_object = hashlib.sha3_256(keyword)
key = hash_object.digest()
# print(key)

fernet_key = base64.urlsafe_b64encode(key)
# print(fernet_key)
cipher = Fernet(fernet_key)
print(cipher.decrypt(encode_string))
