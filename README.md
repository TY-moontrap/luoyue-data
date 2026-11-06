# luoyue-data

反诈数据分析练习仓库。每周产出入库，记录从「手工 Excel」到「用代码处理数据」的过程。

## 目录结构

```
luoyue-data/
├── data/
│   └── data.csv        10 条模拟涉诈网址拦截记录（url, type, channel, date）
├── read_data.py        练习①：读 CSV → 探查 → 按类型计数 → try/except 抓错
├── mytools.py          可复用函数：load_data() / count_by_type()
├── main.py             主脚本：调用 mytools，打印统计结果
└── .gitignore          排除 __pycache__、.vscode、*.db
```

## 怎么跑

```bash
cd D:/luoyue-data
python main.py
```

预期输出：

```
行数 = 10
type
钓鱼    4
诱导    3
仿冒    2
赌博    1
```

## 数据说明

`data/data.csv` 是自造的模拟数据，字段含义：

| 字段 | 含义 | 示例 |
|---|---|---|
| url | 涉诈网址 | pay-safe1.com |
| type | 诈骗类型 | 钓鱼 / 仿冒 / 诱导 / 赌博 |
| channel | 发现渠道 | 短信 / 浏览器 / 合作方 / 搜索引擎 |
| date | 拦截日期 | 2026-09-02 |

## 学习记录

- 2026-11-04 装好 Python 3.13 + pandas，跑通第一个读 CSV 的脚本
- 2026-11-04 把脚本拆成 mytools.py + main.py，学会 import
