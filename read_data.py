import pandas as pd

# 1. 读文件（encoding 必写，否则 Windows 上中文会报错）
df = pd.read_csv('data/data.csv', encoding='utf-8')

# 2. 看一眼长什么样
print('=== 前 5 行 ===')
print(df.head())

# 3. 一共多少行
print('总行数 =', len(df))

# 4. 每种类型的数量
print('=== 按类型计数 ===')
type_counts = df['type'].value_counts()
print(type_counts[type_counts > 2])

# 5. 故意犯错的写法：try/except 抓住它
try:
    bad = pd.read_csv('data/none.csv', encoding='utf-8')
except Exception as e:
    print('抓到错误了：', e)
