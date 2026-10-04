# check_box.py

import sys
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtWidgets import QPushButton, QCheckBox
from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout
from PyQt6.QtWidgets import QLabel

drink_list = ["아메리카노", "라떼", "카푸치노", "에스프레소"]

# 1.생성
app = QApplication(sys.argv)
win = QWidget()
chk1 = QCheckBox("아메리카노")
chk2 = QCheckBox("라떼")
chk3 = QCheckBox("카푸치노")
chk4 = QCheckBox("에스프레소")
chk_btn = [QCheckBox(drink_list[i]) for i in range(len(drink_list))]
p_btn1 = QPushButton("주문")

# 2.배치
layout = QVBoxLayout()
layout.addWidget(chk1)
layout.addWidget(chk2)
layout.addWidget(chk3)
layout.addWidget(chk4)
layout.addWidget(p_btn1)
win.setLayout(layout)

# 3.이벤트 처리
def order():
    selected_item = []
    if chk1.isChecked():
        selected_item.append("아메리카노")
    if chk2.isChecked():
        selected_item.append("라떼")
    if chk3.isChecked():
        selected_item.append("카푸치노")
    if chk4.isChecked():
        selected_item.append("에스프레소")
    if selected_item:
        # print(f"주문 항목: {', '.join(selected_item)}")
        print("주문 항목:", selected_item)
        
    else:
        print("선택된 주문이 없습니다.")
p_btn1.clicked.connect(order)


# 4.윈도우 표시 및 이벤트 루프 실행
win.show()
sys.exit(app.exec())


print('-------------')