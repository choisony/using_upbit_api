# import jwt
# import hashlib
# import os
# import requests
# import uuid
# from urllib.parse import urlencode, unquote
# ACCESS_KEY = "lkh1LjYfDtjrkERW1GntUbATbTKTYZQnEgp9IHUb"
# SECRET_KEY = 'gUlxoEwFwZHokIgXmsZXZZcjrlZIBQY0kwMEVwhQ'
# SERVER_URL = 'https://api.upbit.com'
#
# payload = {
#     'access_key': ACCESS_KEY,
#     'nonce': str(uuid.uuid4()),
# }
#
# jwt_token = jwt.encode(payload, SECRET_KEY)
# authorization = 'Bearer {}'.format(jwt_token)
# headers = {
#   'Authorization': authorization,
# }
#
# res = requests.get(SERVER_URL + '/v1/accounts', headers=headers)
# currency_data = res.json()
#
# print("보유 자본")
# print(f"{currency_data[0]['currency']}: {currency_data[0]['balance']}")
# # for i in currency_data:
# #     print(f"{i['currency'],i['balance']}")

import jwt
import hashlib
import os
import requests
import uuid
from urllib.parse import urlencode, unquote

ACCESS_KEY = ""
SECRET_KEY = ''
SERVER_URL = 'https://api.upbit.com'

params = {
  'currency': 'TRX',
  'amount': '15',
  'address': 'TP9ouEWav4j5KnzScpvL8Lt2CPNBvqABGn'  #내 트론 주소
}
query_string = unquote(urlencode(params, doseq=True)).encode("utf-8")

m = hashlib.sha512()
m.update(query_string)
query_hash = m.hexdigest()

payload = {
    'access_key': ACCESS_KEY,
    'nonce': str(uuid.uuid4()),
    'query_hash': query_hash,
    'query_hash_alg': 'SHA512',
}

jwt_token = jwt.encode(payload, SECRET_KEY)
authorization = 'Bearer {}'.format(jwt_token)
headers = {
  'Authorization': authorization,
}

res = requests.post(SERVER_URL + '/v1/withdraws/coin',json = params, headers=headers)
tt = res.json()

print(tt)
