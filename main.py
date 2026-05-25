# 파일이름 : 파이썬 코드 v2.0 - main.py  
# 작 성 자 : 60232303 이정욱 
portfolio_info = []

def input_stock():
    global portfolio_info

    print("\n---[메뉴 1] 주식 정보 입력---")
    name = input("종목명을 입력하세요: ")
    avg_price = float(input("매수 평단가를 입력하세요(원): "))
    qty = int(input("보유 수량을 입력하세요(주): "))
    current_price = float(input("현재가를 입력하세요(원): "))

    available_cash = float(input("현재 계좌의 여유 현금을 입력하세요(원): "))
    add_amount = float(input("물타기에 사용할 추가 매수 예산을 입력하세요(원): "))

    profit_rate = calculate_profit(avg_price, current_price)

    portfolio_info = [name, avg_price, qty, current_price, available_cash, add_amount, profit_rate]
    print(f"[{name}] 종목 데이터가 리스트에 성공적으로 등록되었습니다!")

def calculate_profit(avg, current):
    rate = ((current - avg) / avg) * 100
    return rate

def analyze_portfolio():
    if not portfolio_info:
        print("\n 등록된 주식 정보가 없습니다! 먼저 1번 메뉴에서 데이터를 입력해주세요.")
        return
    
    print("\n---[메뉴 2] 포트폴리오 정밀 진단---")
    name = portfolio_info[0]
    available_cash = portfolio_info[4]
    add_amount = portfolio_info[5]
    profit_rate = portfolio_info[6]

    print(f"▶ 종목명 : {name}")
    print(f"▶현재 수익률: {profit_rate:.2f}%")

    if profit_rate >= 20.0:
        print("적극 매도 ! 기분 좋게 수익을 실현할 타이밍입니다.")
    elif profit_rate >= 0.0:
        print("강력 홀딩 ! 아직은 빨간불, 든든하게 보유하세요.")
    elif profit_rate > -15.0:
        print("존버 필수 ! 약손실 구간입니다. 조금만 더 버텨보세요.")
    elif profit_rate <= -15.0 and available_cash >= add_amount:
        print("[특별 진단 : 물타기 적기] 하락폭이 크지만 여유 자금이 출분합니다!")
        print(f"{add_amount}원을 추가 매수하여 평단가를 효과적으로 낮춰보세요.")
    else:
        print("강제 장기투자... 하락폭이 크고 물타기할 현금도 부족합니다.")
        print("주식 어플을 지우고 본업에 집중하시는 것을 권장합니다.")
              
while True:
    print("\n====================")
    print("주식 포트폴리오 진단 시스템 v2.0")
    print("=====================")
    print("1. 주식 정보 입력 및 등록")
    print("2. 포트폴리오 정밀 진단")
    print("3. 프로그램 종료")
    print("=====================")

    menu_choice = input("원하는 메뉴 번호를 선택하세요: ")

    if menu_choice == "1":
        input_stock()
    elif menu_choice == "2":
        analyze_portfolio()
    elif menu_choice == "3":
        print("\n 시스템을 종료합니다. 성투하세요!")
        break
    else:
        print("\n 잘못된 입력입니다. 1~3번 사이의 번호를 입력해주세요.")

