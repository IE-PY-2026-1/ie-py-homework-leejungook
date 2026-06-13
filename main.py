# 파일이름 : 파이썬 코드 v3.0 - main.py  
# 작 성 자 : 60232303 이정욱 
portfolio_list = []


def calculate_profit(avg, current):
    return ((current - avg) / avg) * 100


def input_stock():
    global portfolio_list
    print("\n---[메뉴 1] 주식 정보 입력---")

    try: 
        name = input("종목명을 입력하세요: ")
        avg_price = float(input("매수 평단가를 입력하세요(원): "))
        qty = int(input("보유 수량을 입력하세요(주): "))
        current_price = float(input("현재가를 입력하세요(원): "))
        available_cash = float(input("현재 계좌의 여유 현금을 입력하세요(원): "))
        add_amount = float(input("물타기에 사용할 추가 매수 예산을 입력하세요(원): "))
    except ValueError:
        print("\n 오류: 가격이나 수량에는 숫자만 정확히 입력해야 합니다! 처음부터 다시 시도해주세요.")
        return  
    
    profit_rate = calculate_profit(avg_price, current_price)

    stock_data = [name, avg_price, qty, current_price, available_cash, add_amount, profit_rate]
    portfolio_list.append(stock_data)

    print(f"[{name}] 종목 데이터가 리스트에 성공적으로 등록되었습니다!")


def analyze_portfolio():
    if not portfolio_list:
        print("\n 등록된 주식 정보가 없습니다! 먼저 데이터를 입력하거나 파일에서 불러와주세요")
        return
    print("\n=============================================================")
    print("\n---[메뉴 2] 전체 포트폴리오 정밀 진단 결과 ---")
    print(f"{'종목명' : <8} | {'평단가' : <8} | {'수량' : <5} | {'현재가' : <8} | {'수익률' : <7} | {'진단 결과'}")
    print("\n=============================================================")

    for stock in portfolio_list:
        name = stock[0]
        avg_price = stock[1]
        qty = stock[2]
        current_price = stock[3]
        available_cash = stock[4]
        add_amount = stock[5]
        profit_rate = stock[6]

        if profit_rate >= 20.0:
            status = "적극 매도 ! 기분 좋게 수익을 실현할 타이밍입니다."
        elif profit_rate >= 0.0:
            status = "강력 홀딩 ! 아직은 빨간불, 든든하게 보유하세요."
        elif profit_rate > -15.0:
            status = "존버 필수 ! 약손실 구간입니다. 조금만 더 버텨보세요."
        elif profit_rate <= -15.0 and available_cash >= add_amount: 
            status = "[물타기 적기] 추가 매수로 평단가 낮추기 추천"
        else:
            status = "강제 장기투자... 본업에 집중하세요."
        print(f"{name:<8} | {avg_price:<9.0f} | {qty:<7d} | {current_price:<9.0f} | {profit_rate:<7.2f}% | {status}")
    print("===============================================================3")    


def save_to_file():
    if not portfolio_list:
        print("\n 저장할 데이터가 존재하지 않습니다")
        return
    
    with open("portfolio_data.txt", "w", encoding="utf-8") as f:
        for stock in portfolio_list:
            line = f"{stock[0]},{stock[1]},{stock[2]},{stock[3]},{stock[4]},{stock[5]},{stock[6]}\n"
            f.write(line)
    print("\n portfolio_data.txt 파일에 포트폴리오 데이터가 안전하게 저장 되었습니다!")

def load_from_file():
    global portfolio_list

    try:
        with open("portfolio_data.txt", "r", encoding="utf-8") as f:
            portfolio_list = []
            for line in f:
                data = line.strip().split(",")

                name = data[0]
                avg_price = float(data[1])
                qty = int(data[2])
                current_price = float(data[3])
                available_cash = float(data[4])
                add_amount = float(data[5])
                profit_rate = float(data[6])

                portfolio_list.append([name, avg_price, qty, current_price, available_cash, add_amount, profit_rate])
            print("\n 파일로부터 기존 포트폴리오 데이터를 성공적으로 불러왔습니다!")

    except FileNotFoundError:
        print("\n 오류: 저장된 파일(portfolio_data.txt)를 찾을 수 없습니다 ")
        print(" 먼저 1번 메뉴에서 데이터를 등록하고 3번 메뉴로 저장한 후에 불러와주세요.")






              
while True:
    print("\n=====================")
    print("주식 포트폴리오 진단 시스템 v3.0")
    print("=====================")
    print("1. 주식 정보 입력 및 추가")
    print("2. 전체 포트폴리오 정밀 진단")
    print("3. 포트폴리오 데이터 파일 저장")
    print("4. 저장된 데이터 파일 불러오기")
    print("5. 프로그램 종료")
    print("=====================")

    menu_choice = input("원하는 메뉴 번호를 선택하세요: ")

    if menu_choice == "1":
        input_stock()
    elif menu_choice == "2":
        analyze_portfolio()
    elif menu_choice == "3":
        save_to_file()
    elif menu_choice == "4":
        load_from_file()
    elif menu_choice == "5":
        print("\n 시스템을 종료합니다. 성투하세요!")
        break
    else:
        print("\n 잘못된 입력입니다. 1~5번 사이의 번호를 입력해주세요.")

