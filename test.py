"""from termcolor import colored

print(colored('Hello, world!', 'yellow'))

import turtle

turtle.forward(100)
turtle.right(90)
turtle.forward(100)
turtle.done()
import emoji

print(emoji.emojize("Python is :thumbs_up:"))


import hello
import emoji

print(hello.hello(hello.infor["name"]), "❤️", emoji.emojize(':thumbs_up:')) 

import pandas as pd

# Tạo DataFrame từ dữ liệu
data = {
    'Tên': ['Thái', 'Trí', 'Ly', 'Việt'],
    'Tuổi': [21, 21, 21, 21],
    'Điểm': [79, 80, 90, 100]
}

df = pd.DataFrame(data)

# Hiển thị dữ liệu
print("Bảng điểm:")
print(df)
#print("\nThống kê mô tả:")
#print(df.describe())

# Thêm cột mới
df['Kết quả'] = ['Đậu' if x >= 80 else 'Rớt' for x in df['Điểm']]
selected_columns = ['Tên', 'Kết quả']
# Hiển thị DataFrame sau khi thêm cột mới
print("\nXét kết quả:")
print(df[selected_columns])

import hello 
from emoji import emojize as ji
from colorama import Fore
from termcolor import colored

print(Fore.RED +hello.hello(hello.infor["age"]), "❤️", ji(':thumbs_up:')) 
"""
import math
print(math.sqrt(9))

