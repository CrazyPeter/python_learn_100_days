# python_learn_100_days


计划已经完成6/100

## 学习补缺记录

* 不确定的多参数
```python
# 在参数名前面的*表示args是一个可变参数
# 即在调用add函数时可以传入0个或多个参数
def add(*args):
    total = 0
    for val in args:
        total += val
    return total
```

* python支持提供参数默认值，同ES6
* 模块不需要特别导出，即可在其他文件中引用
* __name__是Python中一个隐含的变量它代表了模块的名字，只有被Python解释器直接执行的模块的名字才是__main__
* python3支持内嵌函数，同ES6
* 字符串方法补全

```python
#字符串的切片
    str2 = 'abc123456'
    # 字符串首字母大写
    str2.title()
    # 从字符串中取出指定位置的字符(下标运算)
    print(str2[2])  # c
    # 字符串切片(从指定的开始索引到指定的结束索引)
    print(str2[2::2])  # c246 [start,end,step]
    # 获得字符串修剪左右两侧空格的拷贝
    print(str3.strip())
```

* 数组方法补全

```python
    list1 = [1, 3, 5, 7, 100]
# 添加元素
    list1.append(200)
    list1.insert(1, 400)
    list1 += [1000, 2000]
 # 删除元素
    list1.remove(3)
    if 1234 in list1:
        list1.remove(1234)
    del list1[0] #效果等同remove
    print(list1)
    # 清空列表元素
    list1.clear()
 #切片
    # 可以通过反向切片操作来获得倒转后的列表的拷贝
    fruits = ['grape', 'apple', 'strawberry', 'waxberry']
	fruits += ['pitaya', 'pear', 'mango']
    fruits5 = fruits[::-1]
 #排序
    # sorted函数返回列表排序后的拷贝不会修改传入的列表
    list3 = sorted(list1, reverse=True)
    # 通过key关键字参数指定根据字符串长度进行排序而不是默认的字母表顺序
    list4 = sorted(list1, key=len)
```

* 数组的列表生成法
```python
import sys


def main():
    f = [x for x in range(1, 10)]
    print(f)
    f = [x + y for x in 'ABCDE' for y in '1234567']
    print(f)
    # 用列表的生成表达式语法创建列表容器
    # 用这种语法创建列表之后元素已经准备就绪所以需要耗费较多的内存空间
    f = [x ** 2 for x in range(1, 1000)]
    print(sys.getsizeof(f))  # 查看对象占用内存的字节数
    print(f)
    # 请注意下面的代码创建的不是一个列表而是一个生成器对象
    # 通过生成器可以获取到数据但它不占用额外的空间存储数据
    # 每次需要数据的时候就通过内部的运算得到数据(需要花费额外的时间)
    f = (x ** 2 for x in range(1, 1000))
    print(sys.getsizeof(f))  # 相比生成式生成器不占用存储数据的空间
    print(f)
    for val in f:
        print(val)


if __name__ == '__main__':
    main()
```

* 打印星号的小技巧 ：print("*"*20)
* yield最主要可以节省大量内存
* 元组和列表相互转换的函数
```python
 # 将列表转换成元组
    fruits_list = ['apple', 'banana', 'orange']
    fruits_tuple = tuple(fruits_list)
# 将元组转换成列表
    t = ('王大锤', 20, True, '云南昆明')
    print(t)
    person = list(t)
```

* 关于字典的常用方法
```python
def main():
    scores = {'骆昊': 95, '白元芳': 78, '狄仁杰': 82}
    # 通过键可以获取字典中对应的值
    print(scores['骆昊'])
    print(scores['狄仁杰'])
    # 对字典进行遍历(遍历的其实是键再通过键取对应的值)
    for elem in scores:
        print('%s\t--->\t%d' % (elem, scores[elem]))
    # 更新字典中的元素
    scores['白元芳'] = 65
    scores['诸葛王朗'] = 71
    scores.update(冷面=67, 方启鹤=85)
    print(scores)
    if '武则天' in scores:
        print(scores['武则天'])
    print(scores.get('武则天'))
    # get方法也是通过键获取对应的值但是可以设置默认值
    print(scores.get('武则天', 60))
    # 删除字典中的元素
    print(scores.popitem())
    print(scores.popitem())
    print(scores.pop('骆昊', 100))
    # 清空字典
    scores.clear()
    print(scores)


if __name__ == '__main__':
    main()
```

* 有趣的例子，可以给老婆做练习用
```python
# _*_ coding: utf-8 _*_

import os
import time

def main():
    content='北京欢迎你为你开天辟地…………'
    while True:
        # 清理屏幕输出
        os.system('clear')
        print(content)
        # 休眠200毫秒
        time.sleep(0.2)
        content = content[1:] + content[0]

if __name__ == '__main__':
    main()
```