import pandas as pd
from pathlib import Path

# ===== 第 1 步：多文件合并 =====
rows = []
for p in sorted(Path('data').glob('*.csv')):
    if p.name == 'result.csv':
        continue
    rows.append(pd.read_csv(p, encoding='utf-8'))
    print('读入', p.name)
df = pd.concat(rows, ignore_index=True)
print('合并后行数 =', len(df))

# ===== 第 2 步：按 url 去重（保留首次出现）=====
before = len(df)
df = df.drop_duplicates(subset=['url'], keep='first')
print('去重前 =', before, ' 去重后 =', len(df))

# ===== 第 3 步：二级统计 =====
report = (df.groupby(['type', 'channel'])
            .size()
            .reset_index(name='count')
            .sort_values('count', ascending=False))
print(report)

report.to_csv('report.csv', index=False, encoding='utf-8-sig')
print('已写出 report.csv')
