# hw11.py

# 5
import sys
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtWidgets import QVBoxLayout
from PyQt6.QtWidgets import QCheckBox, QPushButton
from PyQt6.QtWidgets import QLabel

pizza_list = ["치즈 피자","콤비네이션 피자","포테이토 피자"]
price_list = [20000, 25000, 30000]

app = QApplication(sys.argv)
window = QWidget()
window.resize(400, 300)
window.setWindowTitle("조각 피자 주문 프로그램")
layout = QVBoxLayout()
label = QLabel("피자")
checkboxes = [QCheckBox(text) for text in pizza_list]
push_button = QPushButton("주문")

layout.addWidget(label)
[layout.addWidget(cb) for cb in checkboxes]
layout.addWidget(push_button)
window.setLayout(layout)

def order():
    order_list = [pizza_list for cb, pizza_list in zip(checkboxes, pizza_list) if cb.isChecked()]
    total_price = sum([price_list for cb, price_list in zip(checkboxes, price_list) if cb.isChecked()])
    if order_list:
        print("주문 내역:", order_list)
        print("총 가격:", total_price)
    else:
        print("주문 내역이 없습니다")
push_button.clicked.connect(order)

window.show()
sys.exit(app.exec())