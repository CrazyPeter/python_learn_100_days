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