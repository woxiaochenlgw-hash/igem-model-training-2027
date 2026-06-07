# week2_alignment_notes.md

## 1. 本周阅读的两篇文献

文献一: Needleman, S. B., & Wunsch, C. D. (1970). A general method applicable to the search for similarities in the amino acid sequence of two proteins. *Journal of Molecular Biology*.
  主要内容：提出了基于动态规划的**全局序列比对算法**，可以对两条序列全长进行最优对齐，用于判断整体同源性。
文献二: Smith, T. F., & Waterman, M. S. (1981). Identification of common molecular subsequences. *Journal of Molecular Biology*.
  主要内容：在全局比对基础上改进，提出**局部序列比对算法**，专门寻找两条序列中最相似的局部保守区域。

---

## 2. Needleman‑Wunsch 与 Smith‑Waterman 在初始化和递推式上的具体差别
1、矩阵初始化
    Needleman-Wunsch（全局比对）：
        第一列和第一行需要按 gap * k 赋值（k 为当前行 / 列的索引），表示在序列开头连续插入空位的累计惩罚，保证算法会对两条序列的全长进行对齐。
    Smith-Waterman（局部比对）：
        第一行和第一列全部初始化为 0，不允许在局部比对的两端引入空位，确保只关注序列内部的高相似片段。
2、递推公式
    Needleman-Wunsch（全局比对）：
        递推式为 max(对角+得分, 上方+gap, 左方+gap)，没有 0 下限，允许得分持续累积，保证最终会得到覆盖两条序列全长的对齐结果。
    Smith-Waterman（局部比对）：
        递推式为 max(0, 对角+得分, 上方+gap, 左方+gap)，额外加入 0 作为下限：当当前位置的所有可能得分都为负时，直接重置为 0，表示放弃之前的比对、从当前位置重新开始，从而只保留得分最高的局部相似区域。
3、回溯逻辑
    Needleman-Wunsch（全局比对）：
        回溯起点固定为矩阵右下角（两条序列的末尾位置），必须一直回溯到矩阵左上角（序列起点），强制完成全长序列的对齐。
    Smith-Waterman（局部比对）：
        回溯起点是矩阵中得分最大的位置，当回溯过程中遇到 0 时立即停止，只保留中间得分最高的局部片段，不要求对齐全长。

## 3. 默认参数下至少两对序列的比对结果展示

默认参数：`match = 1, mismatch = -1, gap = -2`

### 序列对 1：GATTACA vs GCATGCU
- **全局比对（NW）**
  - 得分：-1
  - 对齐序列 1：`GATTACA`
  - 对齐序列 2：`GCATGCU`
  - 对齐长度：7
  - 匹配数：3
  - gap 数量：0
- **局部比对（SW）**
  - 得分：2
  - 对齐序列 1：`AT`
  - 对齐序列 2：`AT`
  - 对齐长度：2
  - 匹配数：2
  - gap 数量：0

### 序列对 2：TTACGTAA vs GGACGTCC
- **全局比对（NW）**
  - 得分：0
  - 对齐序列 1：`TTACGTAA`
  - 对齐序列 2：`GGACGTCC`
  - 对齐长度：8
  - 匹配数：4
  - gap 数量：0
- **局部比对（SW）**
  - 得分：4
  - 对齐序列 1：`ACGT`
  - 对齐序列 2：`ACGT`
  - 对齐长度：4
  - 匹配数：4
  - gap 数量：0

---

### 结果分析
1. **两种算法对同一对序列的 alignment 结果有什么不同？**
Needleman-Wunsch（NW）全局比对致力于**强行对齐整条序列**，例如在 pair_003 中，尽管两条序列差异较大，NW 依然输出全长 8 bp 的比对，为此承受了较多错配代价，最终得分仅为 0；Smith-Waterman（SW）局部比对不追求全长对齐，而是**精准抓取局部相似度最高的片段**，丢弃两端不相关区域，在 pair_003 中敏锐识别出完全一致的 4 bp 保守片段 `ACGT`，得到 4 分的局部高分。

2. **哪种算法更适合判断两条序列整体上是否相似？**
NW 算法更适合。全局比对会完整考虑序列全长的同源性，不遗漏任何区域，适合评估进化距离较近的同源基因、同一物种的亚型，或蛋白质全局结构的相似性，能反映序列整体的亲缘关系。

3. **哪种算法更适合在长序列中找局部保守片段？**
SW 算法更适合。生物学中，非功能区（如内含子、无规卷曲）变异快，而核心功能区（如启动子 TATA-box、蛋白质催化中心）高度保守；SW 能自动过滤两翼变异大的噪声区域，精准定位并提取局部保守的结构域或基序，是功能元件分析的核心工具。

4. **为什么 Smith-Waterman 递推式中要加上 0？**
在 SW 递推公式 `H(i, j) = max(0, diagonal, up, left)` 中，`0` 是**“负分熔断机制”**：
- 阻断累积惩罚：若某一段序列相似度极低，mismatch 和 gap 惩罚会让得分持续走低，不加 0 会导致“负分负债”持续传递，抹杀后续保守片段的得分；
- 允许重新开始：`0` 意味着算法可随时重置糟糕的过往比对，在当前坐标 `(i, j)` 开启全新比对，这是局部比对能从任意位置开始/结束、精准提取保守片段的数学基础。


## 4. 参数敏感性问题

### （1）gap penalty 变强时，gap 数变多还是变少？

变少。
因为 gap 惩罚越重，插入空位带来的得分下降越明显，算法会尽量避免开 gap，转而接受错配或缩短对齐长度，因此最终 alignment 中空位数量减少。

### （2）mismatch penalty 变强时，更倾向 mismatch 还是 gap？

更倾向插入 gap。
错配惩罚变大后，出现不匹配碱基的代价高于插入空位，算法会选择用 gap 避开高代价的错配。

### （3）为什么相同序列在不同参数下会得到完全不同的 alignment？

因为参数直接决定了每一步动态规划的最优选择：
- match 奖励高 → 倾向更长匹配
- mismatch 惩罚高 → 更愿意开 gap
- gap 惩罚高 → 尽量少开 gap
不同参数组合会让最优路径完全不同，最终对齐结果差异很大。

---

## 5. Biopython 验证结果

- 验证序列：pair_001、pair_002
- 参数：match=1, mismatch=-1, gap=-2
- Biopython 使用 `open_gap_score=-2, extend_gap_score=-2` 模拟线性空位罚分

| 序列对 | 模式 | Biopython 得分 | 手写实现得分 | 是否一致 |
|--------|------|----------------|---------------|-----------|
| pair_001 | global | 0.0 | 0 | 一致 |
| pair_001 | local | 3.0 | 3 | 一致 |
| pair_002 | global | 1.0 | 1 | 一致 |
| pair_002 | local | 3.0 | 3 | 一致 |

结论：手写实现的得分与 Biopython 完全一致，算法逻辑正确。

---

## 6. 遇到的 bug / 困难及解决方法

1. **IndentationError 缩进错误**
   - 原因：`max()` 内部多行表达式缩进不一致
   - 解决：统一使用 4 空格缩进，保证同一层级对齐

2. **NameError: name 'a' is not defined**
   - 原因：统计第二条序列 gap 时误用变量 `a`，应该用 `b`
   - 解决：修正为 `sum(1 for b in align2 if b == '-')`

3. **FileNotFoundError: demo_pairs.csv**
   - 原因：文件路径写错，没有使用项目真实路径
   - 解决：改为 `week2_sequence_alignment/data/demo_pairs.csv`

4. **FileNotFoundError：Notebook 中多一层 submissions 目录**
   - 原因：Notebook 工作目录与终端不一致，输出路径写成 `submissions/...` 导致嵌套生成 `submissions/submissions/...`
   - 解决：使用 `../submissions/dujiayi/week2/...` 或 `os.path.abspath()` 明确锚定项目根目录，避免环境差异导致路径偏移

## 7. 当前实现的局限性

1. 只支持**线性空位罚分**，不支持更符合生物学实际的仿射空位罚分（affine gap）。
2. 只使用简单匹配/错配分值，未使用 BLOSUM、PAM 等进化替换矩阵。
3. 只返回**一条最优比对**，存在多条最优路径时无法全部展示。
4. 时间与空间复杂度均为 O(nm)，长序列运行效率低。
5. 仅支持双序列比对，无法做多序列比对（MSA）。

---
