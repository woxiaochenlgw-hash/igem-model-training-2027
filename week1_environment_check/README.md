# Week 1：环境配置与基础数据处理验收

## 任务目标

本周任务用于检查你是否能够完成一个最小可复现分析流程。

你需要做到：

1. 读取 FASTA 文件；
2. 统计每条序列的长度、GC 数量和 GC 百分比；
3. 使用 pandas 读取 CSV 表格；
4. 计算标准化荧光值；
5. 将序列统计结果与测量表格合并；
6. 绘制基础图表；
7. 按规范提交 notebook、结果表、图片和说明文档。

## 输入文件

```text
week1_environment_check/data/demo_sequences.fasta
week1_environment_check/data/demo_measurements.csv
```

请不要修改这两个原始数据文件。

## 任务 1：FASTA 序列统计

对每条序列计算：

```text
sequence_id
length
GC_count
GC_percent
```

输出文件：

```text
submissions/<your_name>/week1/results/week1_sequence_stats.csv
```

## 任务 2：CSV 表格处理

读取文件：

```text
week1_environment_check/data/demo_measurements.csv
```

新增一列：

```text
normalized_fluorescence = fluorescence / od600
```

## 任务 3：合并数据表

按照 `sequence_id` 将测量表与 FASTA 统计表合并。

输出文件：

```text
submissions/<your_name>/week1/results/week1_merged_table.csv
```

## 任务 4：绘图

至少生成以下三张图：

```text
submissions/<your_name>/week1/figures/week1_normalized_fluorescence_bar.png
submissions/<your_name>/week1/figures/week1_group_comparison.png
submissions/<your_name>/week1/figures/week1_gc_vs_expression.png
```

三张图分别建议为：

1. 每个样本的 normalized fluorescence 柱状图；
2. control 与 treatment 的 normalized fluorescence 分组比较图；
3. GC_percent 与 normalized fluorescence 的散点图。

## 任务 5：结果说明

撰写简短说明，回答：

1. 你完成了哪些步骤？
2. 你的 FASTA 统计结果是否与 `expected_outputs.md` 一致？
3. 你遇到了什么错误？
4. 你如何解决这些错误？

输出文件：

```text
submissions/<your_name>/week1/docs/week1_environment_notes.md
```

## 最低提交结构

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
