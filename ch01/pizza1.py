import tkinter as tk
from tkinter import ttk, messagebox

class PizzaCartOrderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("조각 피자 & 음료 장바구니 주문 시스템")
        self.root.geometry("600x750")
        self.root.resizable(False, False)

        # 메뉴 데이터
        self.PIZZA_PRICES = {
            "페퍼로니": 4000,
            "치즈": 3500,
            "불고기": 4500,
            "콤비네이션": 4500
        }
        
        self.SIZE_PRICES = {
            "보통 (1x)": 0,
            "라지 (+1,000원)": 1000
        }

        self.TOPPING_PRICES = {
            "치즈 추가 (+500원)": 500,
            "올리브 추가 (+300원)": 300,
            "베이컨 추가 (+800원)": 800
        }

        self.DRINK_PRICES = {
            "선택 안 함": 0,
            "콜라 355ml (+1,500원)": 1500,
            "사이다 355ml (+1,500원)": 1500,
            "제로콜라 355ml (+1,500원)": 1500,
            "오렌지주스 (+2,000원)": 2000
        }

        # 상태 변수
        self.cart = []  # 장바구니 항목 담을 리스트
        
        self.selected_pizza = tk.StringVar(value="페퍼로니")
        self.selected_size = tk.StringVar(value="보통 (1x)")
        self.selected_drink = tk.StringVar(value="선택 안 함")
        self.quantity = tk.IntVar(value=1)
        self.topping_vars = {}

        self.create_widgets()

    def create_widgets(self):
        # -------------------------------------------------------------
        # 1. 메뉴 선택 구역 (상단)
        # -------------------------------------------------------------
        menu_container = tk.LabelFrame(self.root, text=" 메뉴 선택 ", font=("맑은 고딕", 11, "bold"), padx=10, pady=10)
        menu_container.pack(fill="x", padx=15, pady=5)

        # (1) 피자 종류
        p_frame = tk.LabelFrame(menu_container, text="1. 피자 종류")
        p_frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        for pizza, price in self.PIZZA_PRICES.items():
            tk.Radiobutton(p_frame, text=f"{pizza} ({price:,}원)", value=pizza, variable=self.selected_pizza).pack(anchor="w")

        # (2) 크기 선택
        s_frame = tk.LabelFrame(menu_container, text="2. 크기")
        s_frame.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
        for size in self.SIZE_PRICES.keys():
            tk.Radiobutton(s_frame, text=size, value=size, variable=self.selected_size).pack(anchor="w")

        # (3) 토핑 선택
        t_frame = tk.LabelFrame(menu_container, text="3. 토핑 추가")
        t_frame.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
        for topping in self.TOPPING_PRICES.keys():
            var = tk.BooleanVar()
            self.topping_vars[topping] = var
            tk.Checkbutton(t_frame, text=topping, variable=var).pack(anchor="w")

        # (4) 음료 선택
        d_frame = tk.LabelFrame(menu_container, text="4. 음료 선택")
        d_frame.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)
        for drink in self.DRINK_PRICES.keys():
            tk.Radiobutton(d_frame, text=drink, value=drink, variable=self.selected_drink).pack(anchor="w")

        # (5) 수량 선택 및 장바구니 담기 버튼
        action_frame = tk.Frame(menu_container)
        action_frame.grid(row=2, column=0, columnspan=2, sticky="ew", pady=10)

        tk.Label(action_frame, text="수량: ", font=("맑은 고딕", 10, "bold")).pack(side="left", padx=5)
        spinbox = tk.Spinbox(action_frame, from_=1, to=20, textvariable=self.quantity, width=5)
        spinbox.pack(side="left", padx=5)

        btn_add_cart = tk.Button(
            action_frame, 
            text="🛒 장바구니에 담기", 
            font=("맑은 고딕", 10, "bold"), 
            bg="#2196F3", 
            fg="white", 
            command=self.add_to_cart
        )
        btn_add_cart.pack(side="right", padx=5)

        # -------------------------------------------------------------
        # 2. 장바구니 구역 (하단)
        # -------------------------------------------------------------
        cart_container = tk.LabelFrame(self.root, text=" 장바구니 목록 ", font=("맑은 고딕", 11, "bold"), padx=10, pady=10)
        cart_container.pack(fill="both", expand=True, padx=15, pady=5)

        # Treeview (표) 형식의 장바구니
        columns = ("menu", "size", "toppings", "drink", "qty", "price")
        self.cart_tree = ttk.Treeview(cart_container, columns=columns, show="headings", height=8)
        
        self.cart_tree.heading("menu", text="피자")
        self.cart_tree.heading("size", text="크기")
        self.cart_tree.heading("toppings", text="토핑")
        self.cart_tree.heading("drink", text="음료")
        self.cart_tree.heading("qty", text="수량")
        self.cart_tree.heading("price", text="가격")

        self.cart_tree.column("menu", width=90, anchor="center")
        self.cart_tree.column("size", width=80, anchor="center")
        self.cart_tree.column("toppings", width=110, anchor="w")
        self.cart_tree.column("drink", width=110, anchor="w")
        self.cart_tree.column("qty", width=40, anchor="center")
        self.cart_tree.column("price", width=80, anchor="e")

        self.cart_tree.pack(fill="both", expand=True, side="left")

        # 스크롤바
        scrollbar = ttk.Scrollbar(cart_container, orient="vertical", command=self.cart_tree.yview)
        self.cart_tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

        # -------------------------------------------------------------
        # 3. 하단 금액 및 결제 버튼
        # -------------------------------------------------------------
        bottom_frame = tk.Frame(self.root, padx=15, pady=10)
        bottom_frame.pack(fill="x")

        btn_delete_item = tk.Button(
            bottom_frame, 
            text="선택 항목 삭제", 
            bg="#f44336", 
            fg="white", 
            command=self.delete_cart_item
        )
        btn_delete_item.pack(side="left")

        self.lbl_grand_total = tk.Label(
            bottom_frame, 
            text="총 결제 금액: 0원", 
            font=("맑은 고딕", 14, "bold"), 
            fg="#D32F2F"
        )
        self.lbl_grand_total.pack(side="left", expand=True)

        btn_checkout = tk.Button(
            bottom_frame, 
            text="전체 결제하기", 
            font=("맑은 고딕", 11, "bold"), 
            bg="#4CAF50", 
            fg="white", 
            padx=10, 
            command=self.checkout
        )
        btn_checkout.pack(side="right")

    def calculate_item_price(self):
        """현재 선택된 1개 메뉴 옵션의 조합 금액 계산"""
        base_price = self.PIZZA_PRICES[self.selected_pizza.get()]
        size_price = self.SIZE_PRICES[self.selected_size.get()]
        drink_price = self.DRINK_PRICES[self.selected_drink.get()]
        topping_price = sum(
            self.TOPPING_PRICES[topping] 
            for topping, var in self.topping_vars.items() 
            if var.get()
        )

        unit_price = base_price + size_price + topping_price + drink_price
        return unit_price * max(1, self.quantity.get())

    def add_to_cart(self):
        """장바구니 항목 추가"""
        pizza = self.selected_pizza.get()
        size = self.selected_size.get().split(" ")[0]
        qty = self.quantity.get()
        item_total = self.calculate_item_price()

        toppings = [t.split(" ")[0] for t, var in self.topping_vars.items() if var.get()]
        topping_str = ", ".join(toppings) if toppings else "없음"
        
        drink_str = self.selected_drink.get().split(" ")[0]

        # 데이터 구조
        item = {
            "pizza": pizza,
            "size": size,
            "toppings": topping_str,
            "drink": drink_str,
            "qty": qty,
            "price": item_total
        }
        
        self.cart.append(item)
        self.refresh_cart_view()

    def delete_cart_item(self):
        """장바구니에서 선택된 항목 삭제"""
        selected_item = self.cart_tree.selection()
        if not selected_item:
            messagebox.showwarning("선택 오류", "삭제할 항목을 장바구니에서 선택해주세요.")
            return
        
        # 선택된 인덱스 찾기 및 삭제
        for sel in selected_item:
            index = self.cart_tree.index(sel)
            del self.cart[index]

        self.refresh_cart_view()

    def refresh_cart_view(self):
        """장바구니 화면 업데이트 및 총 금액 다시 계산"""
        # 기존 항목 비우기
        for item in self.cart_tree.get_children():
            self.cart_tree.delete(item)

        # 새 데이터 채우기
        grand_total = 0
        for item in self.cart:
            self.cart_tree.insert("", "end", values=(
                item["pizza"],
                item["size"],
                item["toppings"],
                item["drink"],
                f"{item['qty']}개",
                f"{item['price']:,}원"
            ))
            grand_total += item["price"]

        self.lbl_grand_total.config(text=f"총 결제 금액: {grand_total:,}원")

    def checkout(self):
        """전체 장바구니 결제 진행"""
        if not self.cart:
            messagebox.showwarning("장바구니 비어있음", "장바구니에 담긴 상품이 없습니다.")
            return

        grand_total = sum(item["price"] for item in self.cart)
        
        summary = f"총 {len(self.cart)}개의 메뉴를 결제하시겠습니까?\n\n"
        summary += f"총 결제 금액: {grand_total:,}원"

        confirm = messagebox.askyesno("결제 확인", summary)
        if confirm:
            messagebox.showinfo("결제 완료", f"총 {grand_total:,}원 결제가 완료되었습니다!\n주문해 주셔서 감사합니다.")
            # 장바구니 초기화
            self.cart.clear()
            self.refresh_cart_view()

if __name__ == "__main__":
    root = tk.Tk()
    app = PizzaCartOrderApp(root)
    root.mainloop()