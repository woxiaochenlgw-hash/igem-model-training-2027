# Git 基础协作流程

本文档说明本培训仓库的基本 Git 使用方式。

## 1. 克隆仓库

```bash
git clone <repository_url>
cd igem-model-training-2027
```

## 2. 创建自己的分支

不要直接在 `main` 分支上提交。

示例：

```bash
git switch -c week1-yourname
```

其中 `yourname` 建议使用姓名拼音或英文名。

## 3. 只在自己的提交文件夹中工作

你的 Week 1 结果应放在：

```text
submissions/<your_name>/week1/
```

不要修改其他队员的文件夹。

## 4. 查看当前改动

```bash
git status
```

## 5. 添加并提交文件

```bash
git add submissions/<your_name>/week1
git commit -m "Complete week1 environment check - <your_name>"
```

## 6. 推送自己的分支

```bash
git push origin week1-yourname
```

## 7. 在 GitHub 网页端创建 Pull Request

推送成功后，打开 GitHub 仓库页面，从你的分支创建 Pull Request，目标分支选择 `main`。

## 8. 不要直接推送到 main

`main` 分支用于保存稳定版本。所有作业应通过 Pull Request 提交，经过检查后再合并。
