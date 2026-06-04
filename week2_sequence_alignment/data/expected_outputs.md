# Week 2 Expected Outputs

本文件说明 Week 2 的最低输出要求。这里不提供完整标准答案，队员需要自行实现 Needleman-Wunsch 和 Smith-Waterman 算法。

## 1. 输入数据

输入文件：

    week2_sequence_alignment/data/demo_pairs.csv

共 4 对序列：

| pair_id | seq1 | seq2 | 说明 |
|---|---|---|---|
| pair_001 | GATTACA | GCATGCU | 经典教学例子；U 仅作为普通字符参与比对 |
| pair_002 | ACCGT | ACG | 短序列插入/缺失例子 |
| pair_003 | TTACGTAA | GGACGTCC | 中间局部保守区域明显 |
| pair_004 | ATGCGTAC | ATGACGTC | 同时包含 mismatch 和 gap 的例子 |

## 2. 默认打分参数

    match    = +1
    mismatch = -1
    gap      = -2

本周使用 linear gap penalty。每出现一个 gap 字符 '-'，就扣同样的 gap 分数。本周不区分 gap opening penalty 和 gap extension penalty。

例如 gap = -2 时：

    长度 1 的 gap：-2
    长度 2 的 gap：-4
    长度 3 的 gap：-6

区分 open gap 和 extend gap 的 affine gap penalty 属于进阶模型，本周不要求实现。

## 3. 必需结果表

每位队员应输出：

    submissions/<yourname>/week2/results/week2_global_alignment_results.csv
    submissions/<yourname>/week2/results/week2_local_alignment_results.csv
    submissions/<yourname>/week2/results/week2_parameter_sensitivity.csv

week2_global_alignment_results.csv 和 week2_local_alignment_results.csv 至少包含：

    pair_id
    algorithm
    match
    mismatch
    gap
    score
    aligned_seq1
    aligned_seq2

week2_parameter_sensitivity.csv 至少包含：

    pair_id
    algorithm
    param_set
    match
    mismatch
    gap
    score
    aligned_seq1
    aligned_seq2
    alignment_length
    number_of_matches
    number_of_gaps

## 4. 必需图片

至少输出：

    submissions/<yourname>/week2/figures/week2_global_dp_matrix.png
    submissions/<yourname>/week2/figures/week2_local_dp_matrix.png

图片要求：

1. 能看出 DP 矩阵每个格子的分数；
2. 推荐使用 pair_001；
3. 推荐用 ax.text() 标出每格具体分数；
4. 如果能标出 traceback 路径更好，但不强制。

## 5. 必需说明文档

说明文档保存为：

    submissions/<yourname>/week2/docs/week2_alignment_notes.md

至少回答：

1. Needleman-Wunsch 和 Smith-Waterman 分别解决什么问题；
2. 两个算法在初始化和递推公式上有什么差别；
3. 默认参数下至少两对序列的比对结果；
4. 参数敏感性分析中观察到什么；
5. Biopython 验证的 score 是否一致；
6. 遇到的 bug 或困难，以及如何解决；
7. 当前实现的局限性。

## 6. 自查标准

提交前请确认：

1. 当前分支不是 main；
2. 没有修改 week2_sequence_alignment/data/ 中的原始数据；
3. 所有输出都在 submissions/<yourname>/week2/；
4. notebook 或脚本能从仓库根目录运行；
5. Biopython 验证分数与自己实现的分数一致，或已解释差异；
6. git status 中没有无关文件。
