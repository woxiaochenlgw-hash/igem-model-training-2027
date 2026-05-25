# iGEM Model 组 2027 预备队培训仓库

本仓库用于 2027 届 iGEM Model 组预备队员的入门训练。

训练目标包括：

1. 配置可复现的数据分析环境；
2. 学习基础生物数据读取与处理；
3. 熟悉 Git / GitHub 协作流程；
4. 按统一规范提交 notebook、结果表、图片和说明文档；
5. 形成“输入数据 → 分析脚本 → 输出结果 → 结果解释”的基本科研工作流。

## 仓库结构

```text
igem-model-training-2027/
├── README.md
├── environment.yml
├── requirements.txt
├── week1_environment_check/
│   ├── README.md
│   ├── data/
│   │   ├── demo_sequences.fasta
│   │   └── demo_measurements.csv
│   ├── expected_outputs.md
│   └── template/
│       └── week1_environment_check_template.py
├── submissions/
│   └── <your_name>/
└── docs/
    ├── git_basic_workflow.md
    └── submission_rules.md
```

## 环境配置

推荐使用 conda：

```bash
conda env create -f environment.yml
conda activate igem_model_training
```

也可以使用 pip：

```bash
pip install -r requirements.txt
```

## 提交规则

不要修改原始数据文件：

```text
week1_environment_check/data/
```

每位队员应创建自己的分支，并将结果提交到：

```text
submissions/<your_name>/week1/
```

示例：

```bash
git switch -c week1-yourname
```

完成任务后：

```bash
git add submissions/<your_name>/week1
git commit -m "Complete week1 environment check - <your_name>"
git push origin week1-yourname
```

然后在 GitHub 网页端创建 Pull Request。

## 注意事项

请使用相对路径，不要使用个人电脑上的绝对路径。

推荐写法：

```python
data_path = "week1_environment_check/data/demo_measurements.csv"
```

不推荐写法：

```python
data_path = "C:/Users/yourname/Desktop/demo_measurements.csv"
```
