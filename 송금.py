import jwt
import hashlib
import requests
import uuid
from urllib.parse import urlencode, unquote

ACCESS_KEY = "" #ACCESS_KEY 를 입력해주세요.
SECRET_KEY = '' #SECRET_KEY 를 입력해주세요.
SERVER_URL = 'https://api.upbit.com'

what = input("어떤 코인을 송금 하실건가요? ex.('TRX','SOL'): ")
amount = input("몇개 송금 하실건가요? :")
address = input("어느 주소로 송금 하실건가요? :")
params = {}
params['currency'] = what
params['amount'] = amount
params['address'] = address

print(params)
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



RESULT : 
  
어떤 코인을 송금 하실건가요? ex.('TRX','SOL'): WEMIX
몇개 송금 하실건가요? :2.72777777
어느 주소로 송금 하실건가요? :0x7b636C238fAe8EAD177e3A8601E47503C66a615d
  
{'currency': 'WEMIX', 'amount': '2.72777777', 'address': '0x7b636C238fAe8EAD177e3A8601E47503C66a615d'}
{'type': 'withdraw', 'uuid': '67d18d87-6e08-4e4b-8443-a1cb930760ee', 'currency': 'WEMIX', 'txid': None, 'state': 'WAITING', 
    'created_at': '2022-08-06T23:20:50+09:00', 'done_at': None, 'amount': '2.72777777', 'fee': '0.05', 'transaction_type': 'default'}
