# 파일이름 : 파이썬 코드 v1.0 - main.py  
# 작 성 자 : 60232303 이정욱
print("=== 주식 포트폴리오 진단 시스템 v1.0 ===")
stock_name = input("종목명을 입력하세요: ")
avg_price = int(input("매수 평단가를 입력하세요(원): "))
qty = int(input("보유 수량을 입력하세요(주): "))
current_price = int(input("현재가를 입력하세요(원): "))

available_cash = int(input("현재 계좌의 여유 현금을 입력하세요(원): "))
add_amount = int(input("물타기에 사용할 추가 매수 예산을 입력하세요(원): "))

stock_info = [stock_name, avg_price, qty, current_price]

profit_rate = ((stock_info[3] - stock_info[1]) / stock_info[1]) * 100

print("\n================================")
print(f"[{stock_info[0]}] 진단 결과")
print(f"현재 수익율: {profit_rate:.2f}%")

if profit_rate >= 20.0:
  print("[등급: S] 적극 매도! 기분 좋게 수익을 실현할 타이밍 입니다.")

elif profit_rate >= 0.0:
  print("[등급: A] 강력 홀딩! 아직은 빨간불, 든든하게 보유하세요.")

elif profit_rate > -15.0:
  print("[등급 B] 존버 필수! 약손실 구간입니다. 조금만 더 버텨보세요.")

elif profit_rate <= -15.0 and available_cash >= add_amount:
  print("[특별 칭호: 물타기 마스터] 하락폭이 크지만 여유자금이 충분합니다!")
  print(f" 조언:{add_amount}원을 추가 매수하여 평단가를 효과적으로 낮춰보세요.")

else:
  print("[등급: F] 강제 장기투자.. 하락폭이 크고 물타기할 현금도 부족합니다.")
  print("조언: 주식 어플을 지우고 본업에 집중하시는 것을 권장합니다.")

print("=================================")
