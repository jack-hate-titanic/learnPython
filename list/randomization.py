'''
Author: 悦者生存 1002783067@qq.com
Date: 2024-10-19 15:40:57
LastEditors: 悦者生存 1002783067@qq.com
LastEditTime: 2024-10-19 21:04:37
FilePath: /learnPython/randomization.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import random;
names = input("what's your friends name?");
names_list = names.split(',');
number = random.randint(0, len(names_list));
print(f"today, {names_list[number]} is going to pay meal");

