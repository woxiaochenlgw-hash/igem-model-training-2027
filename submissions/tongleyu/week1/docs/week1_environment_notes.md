你完成了哪些步骤？
 重新安装了Anaconda并按照文件步骤完成任务
1环境配置与准备
    - 安装并配置了 Anaconda 环境，创建了专属虚拟环境 `igem_model_training`
    - 安装了任务所需的依赖库：`biopython`、`pandas`、`matplotlib` 等
    - 从 GitHub 克隆了项目仓库，并按要求从仓库根目录启动 Jupyter Notebook
    - 创建了个人专属的提交目录结构：`submissions/tongleyu/week1/` 下的 `notebooks`、  `results`、`figures`、`docs` 文件夹
 2任务1：FASTA 序列统计
    - 使用 `Bio.SeqIO` 读取 `demo_sequences.fasta` 文件
    - 计算了每条序列的长度、GC 碱基计数和 GC 百分比
    - 将统计结果保存为 `week1_sequence_stats.csv`，存入 `results` 目录
 3任务2：标准化荧光计算
    - 使用 `pandas` 读取 `demo_measurements.csv` 文件
    - 根据公式 `normalized_fluorescence = fluorescence / od600` 计算了标准化荧光强度
    - 将新增列后的结果保存为 `week1_measurements_normalized.csv`
 4任务3：表格合并
    - 按 `sequence_id` 对序列统计表和测量数据表进行了左连接合并
    - 确保合并后的数据行数与样本数一致（共8行）
    - 将合并结果保存为 `week1_merged_table.csv`
5任务4：可视化绘图
    - 绘制了三张任务要求的图片：
      - 每个样本的标准化荧光柱状图
      - control 与 treatment 组的标准化荧光箱线比较图
      - GC 含量与标准化荧光的散点关系图
    - 所有图片均以指定文件名保存到 `figures` 目录
6任务5：撰写说明文档
    - 整理了任务完成过程，撰写了本说明文档
    - 按要求回答了所有问题，记录了遇到的错误与解决方法
你的 FASTA 统计结果是否与 expected_outputs.md 一致？
 是
你运行时遇到了哪些错误？
 最开始jupyter没在根目录启动，导致文件没读取成功
 jupyter启动麻烦，后续改在vscode上用jupyter插件
 Windows 下 `mkdir` 命令语法错误，`-p` 参数是 Linux/Mac 系统的用法，Windows 系统的 `mkdir`  不支持该参数，将/改成\
你如何解决这些错误？
 询问AI