# layout_move.py

import sys
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtWidgets import QGridLayout
from PyQt6.QtWidgets import QPushButton
# 1.생성
app = QApplication(sys.argv)
win = QWidget()     # 부모 윈도우 객체
win.resize(300, 200)
button1 = QPushButton("PUSH1", parent=win)
button2 = QPushButton("PUSH2", parent=win)
button3 = QPushButton("PUSH3", parent=win)

# 2.배치
button1.move(10,60)
button2.move(140,60)
button3.move(80,10)

# 3.이벤트 처리
def on_click_event(self):
    print("버튼 클릭!")
button1.clicked.connect(on_click_event)
button2.clicked.connect(on_click_event)
button3.clicked.connect(on_click_event)

# 4.윈도우 표시 및 이벤트 루프 실행
win.show()
sys.exit(app.exec())


print('-------------')