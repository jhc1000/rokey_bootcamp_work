# label.py

import sys
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout
from PyQt6.QtWidgets import QPushButton
from PyQt6.QtWidgets import QLabel

# 1.생성
app = QApplication(sys.argv)
win = QWidget()         # 부모 윈도우 객체
win.resize(400, 300)
layout = QVBoxLayout()  # 수직 레이아웃 생성

label1 = QLabel("적")   # 레이블 위젯 객체
label1.setStyleSheet("background-color:red; color:white;")  # 배경 및 글자색 설정
label2 = QLabel("녹")
label2.setStyleSheet("background-color:green; color:white;")
label3 = QLabel("파")
label3.setStyleSheet("background-color:blue; color:white;")
button1 = QPushButton("PUSH1", parent=win)

# 2.배치
layout.addWidget(label1)    # 레이아웃에 레이블 배치
layout.addWidget(label2)
layout.addWidget(label3)
layout.addWidget(button1)
win.setLayout(layout)       # 윈도우에 레이아웃 설정

# 3.이벤트 처리
def on_click_event(self):
    print("버튼 클릭!")
button1.clicked.connect(on_click_event)

# 4.윈도우 표시 및 이벤트 루프 실행
win.show()
sys.exit(app.exec())


print('-------------')