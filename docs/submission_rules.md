# 提交规范

## 1. 不要修改原始任务文件

请不要修改以下目录中的原始数据：

```text
week1_environment_check/data/
```

这些文件是统一测试数据。修改后会导致不同队员的结果不可比较。

## 2. 使用相对路径

推荐写法：

```python
data_path = "week1_environment_check/data/demo_measurements.csv"
```

不推荐写法：

```python
data_path = "C:/Users/yourname/Desktop/demo_measurements.csv"
```

原因：绝对路径只在你自己的电脑上有效，其他人无法复现。

## 3. 不要提交无关文件

不要提交：

```text
.ipynb_checkpoints/
__pycache__/
.DS_Store
大型原始数据
账号密码
token
个人隐私信息
```

## 4. Week 1 最低提交结构

```text
submissions/<your_name>/week1/
├── notebooks/
│   └── week1_environment_check.ipynb
├── results/
│   ├── week1_sequence_stats.csv
│   └── week1_merged_table.csv
├── figures/
│   ├── week1_normalized_fluorescence_bar.png
│   ├── week1_group_comparison.png
│   └── week1_gc_vs_expression.png
└── docs/
    └── week1_environment_notes.md
```

## 5. Pull Request 检查标准

提交后，组长会重点检查：

1. notebook 是否能从头运行；
2. 路径是否为相对路径；
3. FASTA 统计结果是否与 `expected_outputs.md` 一致；
4. 图片是否能正常打开；
5. 说明文档是否解释了分析步骤；
6. 是否误提交缓存文件、大文件或隐私信息。
