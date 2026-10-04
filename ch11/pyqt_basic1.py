# pyqt_basic1.py

import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
# from PyQt6.QtWidgets import QApplication
# from PyQt6.QtWidgets import QWidget # 부모 윈도우 클래스
# import sys
# from PyQt6.QtWidgets import QPushButton # 자식 위젯 클래스
# from PyQt6.QtWidgets import QVBoxLayout


app = QApplication(sys.argv)

# 1.생성
win = QWidget()     # 부모 윈도우 객체
win.setGeometry(100, 100, 400, 300)
button = QPushButton("클릭", parent=win)

# 2.배치
layout = QVBoxLayout()
layout.addWidget(button)
win.setLayout(layout)

# 3.이벤트 처리
def on_click_event(self):
    print("버튼 클릭!")
button.clicked.connect(on_click_event)


# 4.윈도우 표시 및 이벤트 루프 실행
win.show()
sys.exit(app.exec())


print('-------------')
