# Week 1 预期输出

## FASTA 统计结果

预期序列数量：5 条。

预期统计结果如下：

| sequence_id | length | GC_count | GC_percent |
|---|---:|---:|---:|
| seq_001_promoter_like | 14 | 7 | 50.0 |
| seq_002_AT_rich | 10 | 0 | 0.0 |
| seq_003_GC_rich | 8 | 8 | 100.0 |
| seq_004_mixed | 10 | 6 | 60.0 |
| seq_005_short | 4 | 2 | 50.0 |

## CSV 处理要求

输入文件中应有 8 个样本。

必须新增以下列：

```text
normalized_fluorescence = fluorescence / od600
```

## 必需输出图片

每位队员至少应输出：

```text
figures/week1_normalized_fluorescence_bar.png
figures/week1_group_comparison.png
figures/week1_gc_vs_expression.png
```

## 必需提交文件

每位队员应将结果提交到：

```text
submissions/<your_name>/week1/
```

最低提交结构：

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
