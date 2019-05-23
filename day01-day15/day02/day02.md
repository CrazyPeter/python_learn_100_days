# day02

[原文地址](https://github.com/jackfrued/Python-100-Days/blob/master/Day01-15/Day02/%E8%AF%AD%E8%A8%80%E5%85%83%E7%B4%A0.md)

```
注意事项：
print写法和c语言相同
//和/不同的地方是：//是只取整数部分的。/会保留小数部分。
```

## 练习1：华氏温度转摄氏温度。

```python
"""
将华氏温度转换为摄氏温度
F = 1.8C + 32

Version: 0.1
Author: 骆昊
"""


f = float(input('请输入华氏温度: '))
c = (f - 32) / 1.8
print('%.1f华氏度 = %.1f摄氏度' % (f, c))
```

## 练习2：输入圆的半径计算计算周长和面积。
```python
"""
输入半径计算圆的周长和面积

Version: 0.1
Author: 骆昊
"""

import math

radius = float(input('请输入圆的半径: '))
perimeter = 2 * math.pi * radius
area = math.pi * radius * radius
print('周长: %.2f' % perimeter)
print('面积: %.2f' % area)
```

## 练习3：输入年份判断是不是闰年。
```python
"""
输入年份 如果是闰年输出True 否则输出False

Version: 0.1
Author: 骆昊
"""

year = int(input('请输入年份: '))
# 如果代码太长写成一行不便于阅读 可以使用\或()折行
is_leap = (year % 4 == 0 and year % 100 != 0 or
           year % 400 == 0)
print(is_leap)

```


