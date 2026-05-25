"""
Week 1 环境验收示例模板

说明：
1. 队员可以复制本文件，也可以将其改写为 Jupyter Notebook。
2. 请将 YOUR_NAME 修改为自己的姓名拼音或英文名。
3. 请尽量理解每一步代码，而不是只运行模板。
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from Bio import SeqIO

ROOT = Path(".")
FASTA_PATH = ROOT / "week1_environment_check" / "data" / "demo_sequences.fasta"
CSV_PATH = ROOT / "week1_environment_check" / "data" / "demo_measurements.csv"

YOUR_NAME = "your_name"  # 请修改为自己的姓名拼音或英文名

OUT_DIR = ROOT / "submissions" / YOUR_NAME / "week1"
NOTEBOOK_DIR = OUT_DIR / "notebooks"
RESULTS_DIR = OUT_DIR / "results"
FIGURES_DIR = OUT_DIR / "figures"
DOCS_DIR = OUT_DIR / "docs"

for directory in [NOTEBOOK_DIR, RESULTS_DIR, FIGURES_DIR, DOCS_DIR]:
    directory.mkdir(parents=True, exist_ok=True)


def calculate_gc_stats(seq: str) -> dict:
    """计算序列长度、GC 数量和 GC 百分比。"""
    seq = seq.upper()
    gc_count = seq.count("G") + seq.count("C")
    length = len(seq)
    gc_percent = gc_count / length * 100 if length > 0 else 0

    return {
        "length": length,
        "GC_count": gc_count,
        "GC_percent": round(gc_percent, 2),
    }


# 1. 读取 FASTA 并统计序列信息
records = []

for record in SeqIO.parse(FASTA_PATH, "fasta"):
    stats = calculate_gc_stats(str(record.seq))
    records.append(
        {
            "sequence_id": record.id,
            **stats,
        }
    )

seq_df = pd.DataFrame(records)
seq_df.to_csv(RESULTS_DIR / "week1_sequence_stats.csv", index=False)

# 2. 读取测量表并计算标准化荧光
measure_df = pd.read_csv(CSV_PATH)

measure_df["normalized_fluorescence"] = (
    measure_df["fluorescence"] / measure_df["od600"]
)

# 3. 合并序列统计表和测量表
merged_df = measure_df.merge(seq_df, on="sequence_id", how="left")
merged_df.to_csv(RESULTS_DIR / "week1_merged_table.csv", index=False)

# 4. 绘制每个样本的标准化荧光柱状图
plt.figure(figsize=(8, 4))
plt.bar(merged_df["sample_id"], merged_df["normalized_fluorescence"])
plt.xlabel("Sample ID")
plt.ylabel("Normalized fluorescence")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(FIGURES_DIR / "week1_normalized_fluorescence_bar.png", dpi=300)
plt.close()

# 5. 绘制 control 与 treatment 的分组比较图
plt.figure(figsize=(5, 4))
groups = [
    merged_df.loc[merged_df["group"] == "control", "normalized_fluorescence"],
    merged_df.loc[merged_df["group"] == "treatment", "normalized_fluorescence"],
]
plt.boxplot(groups, labels=["control", "treatment"])
plt.ylabel("Normalized fluorescence")
plt.tight_layout()
plt.savefig(FIGURES_DIR / "week1_group_comparison.png", dpi=300)
plt.close()

# 6. 绘制 GC 百分比与标准化荧光散点图
plt.figure(figsize=(5, 4))
plt.scatter(merged_df["GC_percent"], merged_df["normalized_fluorescence"])
plt.xlabel("GC percent")
plt.ylabel("Normalized fluorescence")
plt.tight_layout()
plt.savefig(FIGURES_DIR / "week1_gc_vs_expression.png", dpi=300)
plt.close()

# 7. 写入说明文档
with open(DOCS_DIR / "week1_environment_notes.md", "w", encoding="utf-8") as f:
    f.write("# Week 1 环境验收说明\n\n")
    f.write("## 我完成了什么\n\n")
    f.write("1. 读取 FASTA 文件并计算序列统计信息。\n")
    f.write("2. 读取 CSV 文件并计算 normalized_fluorescence。\n")
    f.write("3. 按 sequence_id 合并序列统计表与测量表。\n")
    f.write("4. 生成三张基础图表。\n\n")
    f.write("## 结果核对\n\n")
    f.write("请将 week1_sequence_stats.csv 与 expected_outputs.md 中的预期结果进行比较。\n\n")
    f.write("## 遇到的问题与解决方法\n\n")
    f.write("请在这里记录运行过程中遇到的错误，以及你如何解决。\n")

print("Week 1 环境验收已完成。")
print(f"输出目录：{OUT_DIR}")
