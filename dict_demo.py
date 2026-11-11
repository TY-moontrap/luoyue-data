rows = ['钓鱼','仿冒','钓鱼','诱导','钓鱼','仿冒']

# ===== 1. dict 计数核心 4 行（必须会默写）=====
d = {}
for k in rows:
    d[k] = d.get(k, 0) + 1      # get 带默认值：键不存在返回 0，不报错
print(d)                        # {'钓鱼': 3, '仿冒': 2, '诱导': 1}

# ===== 2. 从多到少排序 =====
top = sorted(d.items(), key=lambda kv: kv[1], reverse=True)
print(top)                      # [('钓鱼', 3), ('仿冒', 2), ('诱导', 1)]

# ===== 3. 列表推导式（筛选写一行）=====
only = [x for x in rows if x == '钓鱼']
print(only)                     # ['钓鱼', '钓鱼', '钓鱼']

# ===== 4. 和 pandas 的答案对照 =====
import pandas as pd
print(pd.Series(rows).value_counts())
