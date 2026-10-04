# pyqt_basic_event.py

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
# from PyQt6.QtWidgets import QApplication
# from PyQt6.QtWidgets import QWidget # 부모 윈도우 클래스
# import sys
# from PyQt6.QtWidgets import QPushButton # 자식 위젯 클래스
# from PyQt6.QtWidgets import QVBoxLayout

# 1.생성
app = QApplication(sys.argv)
win = QWidget()     # 부모 윈도우 객체
win.setGeometry(100, 100, 400, 300)
button = QPushButton("주문")    # 2. 버튼 위젯 생성

# 2.배치
layout = QVBoxLayout()
layout.addWidget(button)
win.setLayout(layout)

# 3.이벤트 처리
def order(self):        # 1. 실행할 슬롯 함수 정의
    print("주문하세요") 
button.clicked.connect(order)   # 3. 이멘트 연결


# 4.윈도우 표시 및 이벤트 루프 실행
win.show()
sys.exit(app.exec())


print('-------------')
