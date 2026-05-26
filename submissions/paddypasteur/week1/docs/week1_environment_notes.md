# Week 1 Environment Notes - paddypasteur（周梓渔）

## 1. 你完成了哪些步骤？

我成功完成了以下步骤，建立了自己的开发与运行环境，并顺利跑通了第一周的数据分析全流程：
* **环境准备**：在 WSL (Ubuntu 24.04) 中测试并运行了 Git 以及 Miniconda 环境。
* **仓库克隆与配置**：克隆了本地培训仓库，并通过 `environment.yml` 文件一键创建并激活了 `igem_model_training` 专属虚拟环境，成功通过了依赖包的导入验证。
* **个人开发分支建立**：从主分支 `main` 同步并创建了自己的个人开发分支 `week1-paddypasteur`，确保后续提交不污染主分支。
* **新建个人工作区**：在 `submissions/paddypasteur/week1/` 目录下创建了 `notebooks/`, `results/`, `figures/`, `docs/` 四个标准规范文件夹。
* **数据分析（Task 1~3）**：
  * **FASTA 序列统计**：用 Biopython 模块解析 `demo_sequences.fasta` 文件，严格统计了序列 ID、长度、GC 数量，并将 GC 比例转换为了保留 1 位小数的百分比（如 `50.0`），输出至 `week1_sequence_stats.csv`。
  * **标准化荧光值计算**：读取 `demo_measurements.csv` 测量表，计算了每个细胞的平均表达量：`normalized_fluorescence = fluorescence / od600`。
  * **表格多对一合并**：按 `sequence_id` 将上述两表融合成一张 8 行的最终表，并保存至 `week1_merged_table.csv`。
* **数据可视化（Task 4）**：使用 `matplotlib` 绘制并导出了 3 张 300 DPI 高清分析图：样本荧光柱状图、Control vs Treatment 对比箱线图、GC 含量与表达量的散点图。

---

## 2. 你的 FASTA 统计结果是否与 expected_outputs.md 一致？

是的，经过比对，我计算出的 FASTA 统计结果与 `expected_outputs.md` 中的预期数据**完全一致**。

---

## 3. 你运行时遇到了哪些错误？

在首次尝试跑通代码的过程中，我遇到了三个非常经典、极具代表性的小问题：
1. **`NotADirectoryError` 路径报错**：
   在 Jupyter 里读取相对路径 `week1_environment_check/data/...` 时报错。因为 Jupyter 运行时的“当前工作目录”默认会切换到笔记本所在的子文件夹（`notebooks/`），导致直接写相对路径找不到根目录的文件。
2. **`FileNotFoundError` 路径无限往上跳**：
   为了解决第 1 个问题，我尝试用 `os.chdir("../../../..")`（向上跳 4 级）来回到根目录。但在调试中重复运行该格子时，工作路径不断往上级退，最终退到了 Linux 系统的最顶层根目录 `/`，导致再次报错找不到文件。
3. **Jupyter 笔记本打开变成乱码 JSON 源码**：
   在重命名笔记本文件时，不小心把后缀 `.ipynb` 连同名字一起覆盖删除了。导致 Jupyter 无法识别它是个笔记本，默认用纯文本编辑器打开了它，看到了一大坨 Base64 格式的图片数据乱码。

---

## 4. 你如何解决这些错误？

在AI的协助下，我用非常科学、规范的方法解决了上述所有问题：
1. **针对路径报错和目录无限乱跳**：
   * 首先，点击 **`Kernel` -> `Restart`** 重置 Jupyter 的运行状态，把工作路径拉回它的“出生点”：`notebooks/` 文件夹。
   * 随后，我写了一个**“动态自动导航防护罩”**代码：通过 `while` 循环不断向上级寻找，只有当文件夹内包含 `week1_environment_check` 文件夹（即仓库根目录的标志）时才停止并切换。这样无论重复运行格子多少次，工作目录都会稳稳地锁死在仓库根目录，一劳永逸。
2. **针对重命名丢失后缀导致乱码**：
   * 在 Jupyter 文件管理器页面中勾选该文件，点击 `Rename`，手动将后缀名补回为 **`week1_environment_check.ipynb`**。重新双击打开后，所有的代码格式、运行结果和图片瞬间完美变回原样。