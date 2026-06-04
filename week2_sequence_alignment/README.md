# Week 2：序列比对模型复现

本周主题是复现两个经典 pairwise sequence alignment 算法：

1. Needleman-Wunsch：全局比对；
2. Smith-Waterman：局部比对。

训练目标是理解动态规划如何用于生物序列比对。主任务必须手写算法，不允许直接调用 Biopython 的 PairwiseAligner 完成主要任务。Biopython 只用于验证自己的实现。

## 1. 任务文件

输入数据：

    week2_sequence_alignment/data/demo_pairs.csv

预期输出说明：

    week2_sequence_alignment/data/expected_outputs.md

代码框架：

    week2_sequence_alignment/template/week2_sequence_alignment_template.py

## 2. 文献阅读

本周阅读两篇经典原始论文：

1. Needleman, S.B. and Wunsch, C.D. (1970). A general method applicable to the search for similarities in the amino acid sequence of two proteins. Journal of Molecular Biology, 48(3), 443–453. DOI: 10.1016/0022-2836(70)90057-4.
2. Smith, T.F. and Waterman, M.S. (1981). Identification of common molecular subsequences. Journal of Molecular Biology, 147(1), 195–197. DOI: 10.1016/0022-2836(81)90087-5.

不要求完全复现原文的所有打分细节。本周只要求基于核心动态规划思想，实现使用 match / mismatch / linear gap penalty 的入门版 NW 和 SW。

## 3. 默认打分参数

    match    = +1
    mismatch = -1
    gap      = -2

本周手写实现使用 linear gap penalty，即每个 gap 字符 '-' 扣同样的分数，不区分 open gap 和 extend gap。Affine gap penalty 属于进阶内容，本周不要求实现。

## 4. Needleman-Wunsch 全局比对

函数建议：

    def needleman_wunsch(seq1, seq2, match=1, mismatch=-1, gap=-2):
        ...

要求输出：

1. score_matrix；
2. aligned_seq1；
3. aligned_seq2；
4. final_score。

初始化规则：

    F(0, 0) = 0
    F(i, 0) = i × gap
    F(0, j) = j × gap

递推公式：

    F(i, j) = max(
        F(i-1, j-1) + s(a_i, b_j),
        F(i-1, j)   + gap,
        F(i,   j-1) + gap
    )

## 5. Smith-Waterman 局部比对

函数建议：

    def smith_waterman(seq1, seq2, match=1, mismatch=-1, gap=-2):
        ...

要求输出：

1. score_matrix；
2. aligned_seq1；
3. aligned_seq2；
4. best_local_score；
5. best_end_position。

初始化规则：

    H(0, 0) = 0
    H(i, 0) = 0
    H(0, j) = 0

递推公式：

    H(i, j) = max(
        0,
        H(i-1, j-1) + s(a_i, b_j),
        H(i-1, j)   + gap,
        H(i,   j-1) + gap
    )

## 6. 参数敏感性分析

对 4 对序列分别用以下 4 组参数运行 NW 和 SW：

| param_set | match | mismatch | gap |
|---|---:|---:|---:|
| A | 1 | -1 | -1 |
| B | 1 | -1 | -2 |
| C | 2 | -1 | -2 |
| D | 2 | -2 | -3 |

输出：

    submissions/<yourname>/week2/results/week2_parameter_sensitivity.csv

## 7. DP 矩阵图

至少输出：

    submissions/<yourname>/week2/figures/week2_global_dp_matrix.png
    submissions/<yourname>/week2/figures/week2_local_dp_matrix.png

图片中应标出每个格子的分数。

## 8. Biopython 验证

使用 Bio.Align.PairwiseAligner 对至少 2 对序列进行 score 验证。

建议示例：

    from Bio import Align

    aligner = Align.PairwiseAligner()
    aligner.mode = "global"
    aligner.match_score = 1
    aligner.mismatch_score = -1
    aligner.gap_score = -2

    alignments = aligner.align("GATTACA", "GCATGCU")
    print(alignments.score)

如果本地 Biopython 版本不支持 gap_score，可以临时使用：

    aligner.open_gap_score = -2
    aligner.extend_gap_score = -2

但需要在 notes 中说明使用了这种设置方式。Biopython 只用于验证，不可代替手写实现。

## 9. 个人提交位置

所有个人结果提交到：

    submissions/<yourname>/week2/

最低结构：

    submissions/<yourname>/week2/
    ├── notebooks/
    │   └── week2_sequence_alignment.ipynb
    ├── results/
    │   ├── week2_global_alignment_results.csv
    │   ├── week2_local_alignment_results.csv
    │   └── week2_parameter_sensitivity.csv
    ├── figures/
    │   ├── week2_global_dp_matrix.png
    │   └── week2_local_dp_matrix.png
    └── docs/
        └── week2_alignment_notes.md

## 10. GitHub 提交流程

    git switch main
    git pull
    git switch -c week2-yourname

完成任务后：

    git status
    git add submissions/yourname/week2
    git commit -m "Complete week2 sequence alignment - yourname"
    git push -u origin week2-yourname

然后在 GitHub 网页端创建 Pull Request：

    base: main
    compare: week2-yourname
