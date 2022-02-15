import pyupbit

## 1분봉 데이터 (최대 200개)
minute1 = pyupbit.get_ohlcv("KRW-BTC","minute1")
print(minute1)
print(type(minute1),minute1.shape)
print("----------------------------------------------------------------------------")

## 3분봉 데이터 (최대 200개)
minute3 = pyupbit.get_ohlcv("KRW-ETH","minute3")
print(minute3)
print(type(minute3),minute3.shape)
print("----------------------------------------------------------------------------")

## 5분봉 데이터 (최대 200개)
minute5 = pyupbit.get_ohlcv("KRW-SOL","minute5")
print(minute5)
print(type(minute5),minute5.shape)
print("----------------------------------------------------------------------------")


## 10분봉 데이터 (최대 200개)
minute10 = pyupbit.get_ohlcv("KRW-ETC","minute10")
print(minute10)
print(type(minute10),minute10.shape)
print("----------------------------------------------------------------------------")

## 30분봉 ,60분봉 동일 minute30, minute60


## Day 요청
df = pyupbit.get_ohlcv("KRW-BTC","day")
print(df)

## Day 요청 5개만
df = pyupbit.get_ohlcv("KRW-BTC","day",count=5)
print(df)

## day, week , month 가능

## 원하는 시간 지정 (일별로 밖에 안됨)
print(pyupbit.get_daily_ohlcv_from_base("KRW-BTC",base=15))
