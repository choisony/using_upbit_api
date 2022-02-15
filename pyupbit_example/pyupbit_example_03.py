import pyupbit

orderbook = pyupbit.get_orderbook("KRW-ETH")
print(orderbook)

access = "yKbt3K7Zi3xVO07DypiyZDQLLXygzcy3tlVs5njC"
secret = "LGN1OKUAjbYy3eRgzXE4cD4EhuJZBSPxO5fge0aL"

upbit = pyupbit.Upbit(access,secret)
print(upbit.get_balances())