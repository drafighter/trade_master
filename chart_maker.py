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

# for k in orderbook[0]:
    # print(k)


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
orderbook_units = orderbook[0]['orderbook_units']    # 15호가 리스트
# print(type(orderbook_units))
# print(orderbook_units)

# 매수1호가
# for k, v in orderbook_units[0].items():
    # print(k, v)

# 매수호가와 수량 구하기
for bid_value in orderbook_units:
    hoga = orderbook_units.index(bid_value)+1
    bid_price = bid_value['bid_price']
    bid_size = bid_value['bid_size']

    print(f'{hoga}호가 가격은 {bid_price}이고, 수량은 {bid_size} 입니다.')
    
# 차트데이터 조회
df = pyupbit.get_ohlcv("KRW-DKA")
close = df['close']
print(close)

# 최근 5일 이동평균 계산 (함수버전)
def cal_ma(day):
    sum = 0
    mday = day * -1
    for i in range(mday, 0):
        # print(f'close[{i}]은 {close[i]} 입니다.')
        sum = sum + close[i]

    # print(f'평균은 {sum / day} 입니다.')
    return sum / day

# 일자별 5일 이동평균 계산
print(f'일자수는 {len(close)}')
    
ma = cal_ma(10)
print(ma)

for i in range(-5, 0):
    print(i)



# rolling 이용 (졸라 쉬움)
ma5 = close.rolling(10).mean()
print(ma5)
