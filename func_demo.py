import pandas as pd

df = pd.read_csv('data/data.csv', encoding='utf-8')

def count_by(df, col):
    """按某一列计数。df=表，col=列名"""
    s = df[col].value_counts()
    return s         # ← 这行删掉试试，外面会拿到 None

r = count_by(df, 'channel')     # 传参数
print(r)

# 局部变量演示
x = 99
def f():
    x = 1        # 这个 x 只活在 f 里面
    print('函数里 x =', x)
f()
print('函数外 x =', x)      # 还是 99，没被改
