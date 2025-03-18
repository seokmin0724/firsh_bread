
stock = {
    "팥붕어빵" : 10,  
    "슈크림붕어빵" : 8,
    "초코붕어빵" : 5  
}

sales = {
    "팥붕어빵" : 0,  
    "슈크림붕어빵" : 0,
    "초코붕어빵" : 0  
}


#붕어빵 가격이 필요해요
price = {
    "팥붕어빵" : 1000,  # 10개 * 1000 =>
    "슈크림붕어빵" : 1200, # 5개 * 1200 =>
    "초코붕어빵" : 1500 # 6개 * 1500 => 
}

def calculate_sales():
    total_sales = 0
    for key in sales: #팥붕어빵
       total_sales += (price[key] * sales[key])
    print(f"오늘의 총 매출은 {total_sales}원 입니다.")

while True:
    mode = input("원하는 모드를 선택하세요 (주문, 관리자 , 종료) : ") #주문
    if mode ==  "종료":
        print("시스템을 종료합니다.")
        break   
    elif mode == "주문":
        order_bread()
    elif mode == "관리자":
        admin_mode()

calculate_sales()

