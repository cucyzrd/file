# python函数

## global 修改全局变量
```python
g = 123

def f1():
    global g
    g = 345
    print(g)

print(g) # 123
f1() # 345
print(g) # 345
```

**f1函数执行时,会gloabl声明修改变量**

```PYTHON
pi = 3.141592653
e = 2.718281828459045

def my_func():
    global pi # 全局变量,与前面的全局变量pi指向相同的对象
    pi = 3.14
    print('global pi = ', pi)

    e = 2.718 # 局部变量, 与前面的全局变量e指向不一样
    print('local e = ', e)

print('module pi = ', pi)
print('module e = ', e)
print('#' * 20)
my_func()
print('module pi=', pi)  # global关键字指向全局变量, 函数中修改了 隐式将全局变量进行修改
print('module e=', e)

'''
module pi =  3.141592653
module e =  2.718281828459045
####################
global pi =  3.14
local e =  2.718
module pi= 3.14
module e= 2.718281828459045
'''
```

## nonlocal局部变量
```PYTHON
def outer_func():
    tax_rate =0.17
    print('outerfunc tax_rate =', tax_rate)
    def inner_func():
        nonlocal tax_rate
        tax_rate = 0.05
        print('inner func tax_rate =', tax_rate)
    inner_func()
    print('outer func tax_rate = ', tax_rate)

outer_func()
```
```
outerfunc tax_rate = 0.17
inner func tax_rate = 0.05
outer func tax_rate =  0.05
```

## 装饰器

- 语法糖
```python
@foo
@sparm
def bar():
    pass

等价于:
    
    def bar():
        pass
bar = foo(sparm(bar))
```
- 例子
```PYTHON
def foo(f):
    """ foo 函数文档 """
    def wrapper(*args, **kwargs):
        print("调用函数:", f.__name__)
        return f(*args, **kwargs)  # 相当于执行函数

    return wrapper

@foo
def bar(x):
    ''' bar 函数文档'''
    return x ** 2

if __name__ == '__main__':
    print(bar(2))
    print(bar.__name__)
    print(bar.__doc__)
```

```python
调用函数: bar
4
wrapper
None
```

- 例子记录函数运行时间
```PYTHON
import time, functools

def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        func(*args, **kwargs)
        end = time.perf_counter()
        print("运行时间", end - start)

    return wrapper

@timeit
def my_sum(n):
    sum = 0
    for i in range(n):
        sum += 1
    print(sum)

if __name__ == '__main__':
    my_sum(100000000)
```
```PYTHON
100000000
运行时间 7.71794459101056
```

- html标签
```PYTHON
def makebold(fn):
    def wrapper(*args):
        return "<b>" + fn(*args) + "</b>"
    return wrapper

def makeitalic(fn):
    def wrapper(*args):
        return "<i>" + fn(*args) + "</i>"
    return wrapper

@makebold
@makeitalic
def htmltags(strl):
    return strl
if __name__ == '__main__':
    print(htmltags('Hello'))

# <b><i>Hello</i></b>
```