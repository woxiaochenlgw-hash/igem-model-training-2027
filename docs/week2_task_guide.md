# Week 2 任务指南：序列比对模型复现

本周主题是复现 Needleman-Wunsch 全局比对和 Smith-Waterman 局部比对。训练目标是理解动态规划如何用于生物序列比对。

主任务必须手写算法，不允许直接调用 Biopython 的 PairwiseAligner 完成主要任务。Biopython 只用于验证自己的实现。

## 一、获取任务文件

进入仓库后同步主分支：

    cd igem-model-training-2027
    git switch main
    git pull

任务文件：

    week2_sequence_alignment/README.md
    week2_sequence_alignment/data/demo_pairs.csv
    week2_sequence_alignment/data/expected_outputs.md
    week2_sequence_alignment/template/week2_sequence_alignment_template.py

不要修改 week2_sequence_alignment/data/ 中的原始数据。

## 二、创建自己的分支

    git switch main
    git pull
    git switch -c week2-yourname

请把 yourname 替换为自己的姓名拼音或英文名。

## 三、创建提交文件夹

    mkdir -p submissions/yourname/week2/notebooks
    mkdir -p submissions/yourname/week2/results
    mkdir -p submissions/yourname/week2/figures
    mkdir -p submissions/yourname/week2/docs

## 四、任务要求

默认参数：

    match    = +1
    mismatch = -1
    gap      = -2

本周使用 linear gap penalty，不区分 gap opening 和 gap extension。

需要完成：

1. 手写 Needleman-Wunsch；
2. 手写 Smith-Waterman；
3. 完成全局与局部比对比较；
4. 完成 4 组参数敏感性分析；
5. 输出至少两张 DP 矩阵图；
6. 用 Biopython 验证至少 2 对序列的 score；
7. 撰写 week2_alignment_notes.md；
8. 通过 Pull Request 提交。

## 五、最低提交结构

    submissions/yourname/week2/
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

## 六、提交到 GitHub

    git status
    git add submissions/yourname/week2
    git commit -m "Complete week2 sequence alignment - yourname"
    git push -u origin week2-yourname

然后创建 Pull Request：

    base: main
    compare: week2-yourname

## 七、提交前自查

1. 当前分支不是 main；
2. 只修改自己的 submissions/yourname/week2/；
3. 没有修改 week2_sequence_alignment/data/；
4. 三个 results 文件已生成；
5. 两张 DP 矩阵图能打开；
6. notes 已回答关键问题；
7. notebook 或脚本能从仓库根目录运行；
8. git status 中没有无关文件。
