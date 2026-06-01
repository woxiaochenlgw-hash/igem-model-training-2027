import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# =========================
# 路径设置
# =========================
measurement_file = Path("week1_environment_check/data/demo_measurements.csv")
sequence_stats_file = Path("submissions/hantest/week1/results/week1_sequence_stats.csv")

results_dir = Path("submissions/hantest/week1/results")
figures_dir = Path("submissions/hantest/week1/figures")

results_dir.mkdir(parents=True, exist_ok=True)
figures_dir.mkdir(parents=True, exist_ok=True)

normalized_output = results_dir / "week1_measurements_normalized.csv"
merged_output = results_dir / "week1_merged_table.csv"

# =========================
# 任务 2：读取 CSV 并计算标准化荧光
# normalized_fluorescence = fluorescence / od600
# =========================
measurements = pd.read_csv(measurement_file)

measurements["normalized_fluorescence"] = (
    measurements["fluorescence"] / measurements["od600"]
)

measurements.to_csv(normalized_output, index=False)

print("Task 2 finished:")
print(measurements.head())
print(f"Saved to: {normalized_output}")

# =========================
# 任务 3：按照 sequence_id 合并表格
# =========================
sequence_stats = pd.read_csv(sequence_stats_file)

merged = pd.merge(
    measurements,
    sequence_stats,
    on="sequence_id",
    how="left"
)

merged.to_csv(merged_output, index=False)

print("\nTask 3 finished:")
print(merged.head())
print(f"Saved to: {merged_output}")

# =========================
# 任务 4-1：每个样本的 normalized fluorescence 柱状图
# =========================
plt.figure(figsize=(8, 5))
plt.bar(merged["sample_id"], merged["normalized_fluorescence"])
plt.xlabel("Sample ID")
plt.ylabel("Normalized Fluorescence")
plt.title("Normalized Fluorescence of Each Sample")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig(figures_dir / "week1_normalized_fluorescence_bar.png", dpi=300)
plt.close()

# =========================
# 任务 4-2：control 和 treatment 分组比较
# =========================
group_mean = merged.groupby("group")["normalized_fluorescence"].mean()

plt.figure(figsize=(6, 5))
plt.bar(group_mean.index, group_mean.values)
plt.xlabel("Group")
plt.ylabel("Mean Normalized Fluorescence")
plt.title("Group Comparison")
plt.tight_layout()
plt.savefig(figures_dir / "week1_group_comparison.png", dpi=300)
plt.close()

# =========================
# 任务 4-3：GC_percent 和 normalized_fluorescence 散点图
# =========================
plt.figure(figsize=(6, 5))
plt.scatter(merged["GC_percent"], merged["normalized_fluorescence"])
plt.xlabel("GC Percent")
plt.ylabel("Normalized Fluorescence")
plt.title("GC Percent vs Normalized Fluorescence")
plt.tight_layout()
plt.savefig(figures_dir / "week1_gc_vs_expression.png", dpi=300)
plt.close()

print("\nTask 4 finished:")
print(f"Figures saved to: {figures_dir}")