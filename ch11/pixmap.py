# pixmap.py

import sys
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtWidgets import QPushButton, QCheckBox
from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout
from PyQt6.QtWidgets import QLabel
from PyQt6.QtGui import QPixmap

# 1.생성
app = QApplication(sys.argv)
win = QWidget()
win.resize(400,300)
pixmap = QPixmap(r"ch11\apples.jpg")
label = QLabel(win)
label.setFixedSize(400, 300)
label.setScaledContents(True)
label.setPixmap(pixmap)


button1 = QPushButton("PUSH1", parent=win)
button2 = QPushButton("PUSH2", parent=win)
button3 = QPushButton("PUSH3", parent=win)

# 2.배치
label.move(-20, -20)
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