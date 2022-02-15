import pyupbit

## 업비트의 모든 티커 목록
tickers = pyupbit.get_tickers()
print(tickers)

## 원화 시장의 티커 목록
krw_tickers = pyupbit.get_tickers(fiat = 'KRW')
print(krw_tickers)
print(len(krw_tickers))

## USDT 시장의 티커 목록
## BTC 시장의 티커 목록
usdt_tickers = pyupbit.get_tickers("USDT")
btc_tickers = pyupbit.get_tickers("BTC")

print(usdt_tickers)
print(btc_tickers)