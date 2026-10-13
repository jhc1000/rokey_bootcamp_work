# matplotlib1.py

import matplotlib.pyplot as plt

print('기본 플롯--------')
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]
plt.plot(x, y)
plt.title("Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

print('다양한 그래프 종류--------')
print('-Bar Chart (막대 그래프)------')
categories = ["A", "B", "C", "D"]
values = [3, 7, 8, 5]
plt.bar(categories, values)
plt.title("Bar Chart")
plt.show()

print('-Histogram (히스토그램)------')
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
plt.hist(data, bins=4, color="skyblue", edgecolor="black")
plt.title("Histogram")
plt.show()

print('-Scatter Plot (산점도)------')
x = [5, 7, 8, 7, 2, 17, 2, 9, 4, 11]
y = [99, 86, 87, 88, 100, 86, 103, 87, 94, 78]
plt.scatter(x, y, color="green")
plt.title("Scatter Plot")
plt.show()

print('-Pie Chart (파이 차트, 원 그래프)------')
sizes = [15, 30, 45, 10]
labels = ["Group A", "Group B", "Group C", "Group D"]
plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90)
plt.title("Pie Chart")
plt.show()

print('-Box Plot (박스 플롯)------')
data = [7, 8, 5, 6, 8, 9, 6, 7, 5, 8]
plt.boxplot(data)
plt.title("Box Plot")
plt.show()

print('그래프 커스터마이징------')
print('-색상, 선 스타일, 마커------')
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]
plt.plot(x, y, color="red", linestyle="--", marker="o")
plt.title("Customized Line Plot")
plt.show()

print('-축 범위와 눈금 설정------')
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]
plt.plot(x, y)
plt.xlim(0, 5)
plt.ylim(0, 40)
plt.xticks(range(1, 5))
plt.yticks(range(0, 41, 10))
plt.show()

print('-범례 추가 및 위치 설정------')
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]
x1 = [1, 2, 3, 4]
y2 = [3, 5, 9, 7]
plt.plot(x, y, label="Data 1")
plt.plot(x1, y2, label="Data 2")
plt.legend(loc="upper left")
plt.show()

print('고급 기능------')
print('-Subplot 활용------')
fig, axs = plt.subplots(2, 2)
axs[0, 0].plot(x, y)
axs[0, 1].bar(categories, values)
axs[1, 0].scatter(x, y)
axs[1, 1].hist(data)
plt.tight_layout()
plt.show()