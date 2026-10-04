# radio.py

import sys
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtWidgets import QPushButton, QRadioButton
from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout
from PyQt6.QtWidgets import QLabel

# 1.생성
app = QApplication(sys.argv)
win = QWidget()
r_btn1 = QRadioButton("A런치")
r_btn2 = QRadioButton("B런치")
r_btn3 = QRadioButton("C런치")
r_btn1.setChecked(True)
p_btn1 = QPushButton("주문")

# 2.배치
layout = QVBoxLayout()
layout.addWidget(r_btn1)
layout.addWidget(r_btn2)
layout.addWidget(r_btn3)
layout.addWidget(p_btn1)
win.setLayout(layout)

# 3.이벤트 처리
def order():
    if r_btn1.isChecked():
        print("A런치 주문")
    elif r_btn2.isChecked():
        print("B런치 주문")
    elif r_btn3.isChecked():
        print("C런치 주문")
p_btn1.clicked.connect(order)



# 4.윈도우 표시 및 이벤트 루프 실행
win.show()
sys.exit(app.exec())


print('-------------')