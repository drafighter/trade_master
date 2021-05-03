import pyupbit
import datetime


tickers = pyupbit.get_tickers("KRW")
# print(tickers, len(tickers))

# while True:
price = pyupbit.get_current_price("KRW-DKA")
print(f'현재가는 {price} 입니다.')    # f-string 출력
# time.sleep(1)

# get_market_detail

orderbook = pyupbit.get_orderbook("KRW-DKA")
print(type(orderbook))

for k in orderbook[0]:
    print(k)
    
# 시간 표시 format 변경
order_time = int(orderbook[0]['timestamp'])
dt = datetime.datetime.fromtimestamp(order_time/1000)
print(dt)
print(f'매도총량은 {orderbook[0]["total_ask_size"]}, 매수총량은 {orderbook[0]["total_bid_size"]}')
if (orderbook[0]['total_ask_size'] >= orderbook[0]['total_bid_size']):
    print('상승 가능성이 있습니다.')
else:
    print('하락 가능성이 있습니다.')
    

# 호가 표시
orderbook_units = orderbook[0]['orderbook_units']
print(type(orderbook_units))
print(orderbook_units)

# 매수1호가
for k,v in orderbook_units[0].items():
    print(k,v)

