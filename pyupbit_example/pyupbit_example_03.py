import pyupbit

orderbook = pyupbit.get_orderbook("KRW-ETH")
print(orderbook)

access = "##############################"
secret = "##############################"

upbit = pyupbit.Upbit(access,secret)
print(upbit.get_balances())
