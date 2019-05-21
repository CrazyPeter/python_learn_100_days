# _*_ coding: utf-8 _*_

def main():
    str1 = 'hello,world!'
    # length
    print(len(str1))
    print(str1.find('or')) #8,找不到位置会返回-1
    #字符串的切片
    str2 = 'abc123456'
    # 从字符串中取出指定位置的字符(下标运算)
    print(str2[2])  # c
    # 字符串切片(从指定的开始索引到指定的结束索引)
    print(str2[2:5])  # c12
    print(str2[2:])  # c123456
    print(str2[2::2])  # c246
    print(str2[::2])  # ac246
    print(str2[::-1])  # 654321cba
    print(str2[-3:-1])  # 45

    list1 = [1, 3, 5, 7, 100]
  # 添加元素
    # list1.append(200)
    # list1.insert(1, 400)
    # list1 += [1000, 2000]
 # 删除元素
    list1.remove(3)
    # if 1234 in list1:
    #     list1.remove(1234)
    # del list1[0]
    print(list1)
    # 清空列表元素
    list1.clear()

# if __name__ == '__main__':
    # main();

fruits = ['grape', 'apple', 'strawberry', 'waxberry']
fruits += ['pitaya', 'pear', 'mango']
	# 循环遍历列表元素
for fruit in fruits:
    print(fruit.title(), end=' ')