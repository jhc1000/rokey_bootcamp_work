# test12-1.py

# 치즈피자 (3200원) x 3 9600원
# 사이다 (1500원) x 2 3000원

class PizzaOrder:
    def __init__(self):
        self.order_list = []
        self.path = "ch12/order.txt"
        
    def order(self):
        order_str = input("주문을 입력하시오. (ex.제품 가격 개수):")
        order_str
        
        mode = 'w'
        if order_str:
            with open(self.path, mode, encoding='utf-8') as file:
                file.write("주문 내역:\n")
                item_list = order_str.split()
                data =" - "+item_list[0]+" ("+item_list[1]+"원)"+" x "+item_list[2]+" "+str(int(item_list[1])*int(item_list[2]))+"원\n"
                file.write(data)
                    
    def orderInfo(self):
        mode = 'r'
        with open(self.path, mode, encoding='utf-8') as file:
            order_lines = file.readlines()
            for line in order_lines:
                print(line, end='')
    
    def orderExtra(self):
            order_str = input("주문을 입력하시오. (ex.제품 가격 개수):")
            
            mode = 'a'
            if order_str:
                with open(self.path, mode, encoding='utf-8') as file:
                    item_list = order_str.split()
                    data =" - "+item_list[0]+" ("+item_list[1]+"원)"+" x "+item_list[2]+" "+str(int(item_list[1])*int(item_list[2]))+"원\n"
                    file.write(data)
    

order1 = PizzaOrder()
order1.order()
order1.orderInfo()
order1.orderExtra()
order1.orderInfo()