import os


os.makedirs(r'C:\Users\16874\OneDrive\Рабочий стол\target')
os.chdir(r'C:\Users\16874\OneDrive\Рабочий стол\target')
for i in range(1, 11):
    os.mkdir(f'{i}')