# combobox.py

# check_box.py

import sys
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtWidgets import QPushButton, QComboBox, QLabel
from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout

# 1.생성
app = QApplication(sys.argv)
win = QWidget()
win.resize(300,100)

# options_list = ["Option1", "Option2", "Option3"]
options_list = ["학생", "공무원", "전문직", "사무직"]
combo = QComboBox()
combo.addItems(options_list)
button = QPushButton("결정")
label = QLabel("현재 직업을 선택하세요")

# 2.배치
layout = QVBoxLayout()
layout.addWidget(label)
layout.addWidget(combo)
layout.addWidget(button)
win.setLayout(layout)

# 3.이벤트 처리
def job_changed():
    selected = combo.currentText()
    print(selected)
def decide():
    print(combo.currentText(), "(으)로 결정한다.")
combo.currentTextChanged.connect(job_changed)
button.clicked.connect(decide)

# 4.윈도우 표시 및 이벤트 루프 실행
win.show()
sys.exit(app.exec())


print('-------------')