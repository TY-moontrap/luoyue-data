import pandas as pd

df = pd.read_csv('data/data.csv', encoding='utf-8')

# 按 channel 计数，从多到少
result = df['channel'].value_counts().reset_index()
result.columns = ['channel', 'count']

# 写出去。index=False 表示不要行号那一列
result.to_csv('result.csv', index=False, encoding='utf-8-sig')

print(result)
print('合计 =', result['count'].sum())
