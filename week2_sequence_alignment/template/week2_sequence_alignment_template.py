"""
Week 2 Sequence Alignment Template

请将本文件复制到自己的 submissions/<yourname>/week2/ 下再修改。
主任务需要自己实现 Needleman-Wunsch 和 Smith-Waterman。
Biopython 只用于验证 score，不可代替手写实现。
请从仓库根目录运行本脚本。
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


ROOT = Path(".")
DATA_PATH = ROOT / "week2_sequence_alignment" / "data" / "demo_pairs.csv"

YOUR_NAME = "yourname"

OUT_DIR = ROOT / "submissions" / YOUR_NAME / "week2"
RESULTS_DIR = OUT_DIR / "results"
FIGURES_DIR = OUT_DIR / "figures"
DOCS_DIR = OUT_DIR / "docs"

for directory in [RESULTS_DIR, FIGURES_DIR, DOCS_DIR]:
    directory.mkdir(parents=True, exist_ok=True)


def substitution_score(a: str, b: str, match: int, mismatch: int) -> int:
    return match if a == b else mismatch


def alignment_summary(aligned_seq1: str, aligned_seq2: str) -> dict:
    if len(aligned_seq1) != len(aligned_seq2):
        raise ValueError("Aligned sequences must have the same length.")

    number_of_matches = sum(
        a == b and a != "-" and b != "-"
        for a, b in zip(aligned_seq1, aligned_seq2)
    )

    number_of_gaps = sum(
        a == "-" or b == "-"
        for a, b in zip(aligned_seq1, aligned_seq2)
    )

    return {
        "alignment_length": len(aligned_seq1),
        "number_of_matches": number_of_matches,
        "number_of_gaps": number_of_gaps,
    }


def needleman_wunsch(seq1: str, seq2: str, match: int = 1, mismatch: int = -1, gap: int = -2):
    """
    TODO:
    1. 初始化 score_matrix；
    2. 填充 DP 矩阵；
    3. 从右下角 traceback 到左上角；
    4. 返回 score_matrix, aligned_seq1, aligned_seq2, final_score。
    """
    m, n = len(seq1), len(seq2)
    score_matrix = np.zeros((m + 1, n + 1), dtype=int)

    aligned_seq1 = ""
    aligned_seq2 = ""
    final_score = int(score_matrix[m, n])

    raise NotImplementedError("Please implement Needleman-Wunsch yourself.")

    return score_matrix, aligned_seq1, aligned_seq2, final_score


def smith_waterman(seq1: str, seq2: str, match: int = 1, mismatch: int = -1, gap: int = -2):
    """
    TODO:
    1. 初始化 score_matrix 为 0；
    2. 递推时使用 max(0, diagonal, up, left)；
    3. 记录最高分位置；
    4. 从最高分位置 traceback 到 0；
    5. 返回 score_matrix, aligned_seq1, aligned_seq2, best_local_score, best_end_position。
    """
    m, n = len(seq1), len(seq2)
    score_matrix = np.zeros((m + 1, n + 1), dtype=int)

    best_local_score = 0
    best_end_position = (0, 0)

    aligned_seq1 = ""
    aligned_seq2 = ""

    raise NotImplementedError("Please implement Smith-Waterman yourself.")

    return score_matrix, aligned_seq1, aligned_seq2, best_local_score, best_end_position


def plot_score_matrix(score_matrix, seq1: str, seq2: str, output_path: Path, title: str):
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.imshow(score_matrix)

    ax.set_title(title)
    ax.set_xlabel("seq2")
    ax.set_ylabel("seq1")

    ax.set_xticks(range(len(seq2) + 1))
    ax.set_yticks(range(len(seq1) + 1))

    ax.set_xticklabels(["-"] + list(seq2))
    ax.set_yticklabels(["-"] + list(seq1))

    for i in range(score_matrix.shape[0]):
        for j in range(score_matrix.shape[1]):
            ax.text(j, i, str(score_matrix[i, j]), ha="center", va="center")

    fig.tight_layout()
    fig.savefig(output_path, dpi=300)
    plt.close(fig)


def biopython_score_example(seq1: str, seq2: str, mode: str = "global"):
    from Bio import Align

    aligner = Align.PairwiseAligner()
    aligner.mode = mode
    aligner.match_score = 1
    aligner.mismatch_score = -1

    try:
        aligner.gap_score = -2
    except Exception:
        aligner.open_gap_score = -2
        aligner.extend_gap_score = -2

    alignments = aligner.align(seq1, seq2)
    return alignments.score


def main():
    pairs = pd.read_csv(DATA_PATH)
    print("Loaded pairs:")
    print(pairs)
    print("Template loaded. Please implement the TODO sections.")


if __name__ == "__main__":
    main()
