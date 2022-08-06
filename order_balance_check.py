import pyupbit
from pyupbit import Upbit

access = ""
secret = ""
upbit = Upbit(access, secret)

# print(pyupbit.get_tickers(fiat="KRW"))  #원화 거래 가능한 종목들 출력

currency = "KRW"    # 조회하려는 화폐 정보
withdraw_list = upbit.get_withdraw_list(currency)
print("조회하려는 화폐 정보: ", withdraw_list)

chance = upbit.get_chance("KRW-TRX") #마켓별 주문 가능 정보를 확인한다.
print("마켓별 주문 가능 정보: ",chance)

balance = upbit.get_balances()
print("내 자산 정보: ",balance[0]['currency'])

CURRENT_TRX_VALUE = pyupbit.get_current_price("KRW-TRX")
print("현재 TRX 가격 :",CURRENT_TRX_VALUE,"원")

TRX_balance = upbit.get_balance("TRX") ## 내 지갑에 TRX 수량 출력
print("내 지갑에 있는 TRX 개수 :",TRX_balance)
#
# TRX_BUY = upbit.buy_market_order(ticker='KRW-TRX', price=10000)   #TRX, 1만원, 시장가 매수 => price
# TRX_SELL  = upbit.sell_market_order("KRW-TRX",volume=TRX_balance)         #TRX, 100개, 시장가 매도 => volume
# print(TRX_BUY)                                                    #매수 정보(uuid 등)
# print(TRX_SELL)                                                   #매도 정보(uuid 등)
#
# SOL_BUY  = upbit.buy_market_order("KRW-SOL",price=10000)         #SOL, 1만원, 시장가 매수
# print(SOL_BUY)
#
# WEMIX_BUY  = upbit.buy_market_order("KRW-WEMIX",price=10000)         #WEMIX, 1만원, 시장가 매수
# print(WEMIX_BUY)
print("TRX 보유 금액 :",upbit.get_amount("TRX"),"원")
print("SOLANA 보유 금액 :",upbit.get_amount("SOL"),"원")
print("WEMIX 보유 금액 :",upbit.get_amount("WEMIX"),"원")

TICKER = input("어떤 코인을 구매하실건가요?: ex.(`TRX`,`SOL`,`WEMIX`)")
HOW_MUCH = input("얼마나 구매하실건가요?: ex.(10000,100000)")

print(upbit.buy_market_order(f'KRW-{TICKER}',price=HOW_MUCH))



# print(upbit.withdraw_coin("SOL",0.1,"CkRXNdYQYH5wCpG9zxV1HLyZaY5XLQDUz3uLD59a7Kd2"))      # 팬텀 지갑으로 송금
# print(upbit.withdraw_coin("TRX",15,"TP9ouEWav4j5KnzScpvL8Lt2CPNBvqABGn"))                 # 바이낸스 트론 지갑으로 송금
# print(upbit.withdraw_coin("WEMIX",1.5,"0x7b636C238fAe8EAD177e3A8601E47503C66a615d"))      # 카이카스 지갑으로 송금
