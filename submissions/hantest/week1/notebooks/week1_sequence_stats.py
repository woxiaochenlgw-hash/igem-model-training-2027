from Bio import SeqIO
import pandas as pd
from pathlib import Path

# 输入文件
input_fasta = Path("week1_environment_check/data/demo_sequences.fasta")

# 输出文件
output_csv = Path("submissions/hantest/week1/results/week1_sequence_stats.csv")

records = []

for record in SeqIO.parse(input_fasta, "fasta"):
    seq = str(record.seq).upper()
    length = len(seq)
    gc_count = seq.count("G") + seq.count("C")
    gc_percent = gc_count / length * 100 if length > 0 else 0

    records.append({
        "sequence_id": record.id,
        "length": length,
        "GC_count": gc_count,
        "GC_percent": round(gc_percent, 2)
    })

df = pd.DataFrame(records)

# 确保输出目录存在
output_csv.parent.mkdir(parents=True, exist_ok=True)

df.to_csv(output_csv, index=False)

print(df)
print(f"\nSaved to: {output_csv}")