# myStudy

## NEW
```
echo "# myStudy" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin git@github.com:demonsen/myStudy.git
git push -u origin main
```

### 添加
git add .

### 删除
git rm file

### 提交
git commit -m 'message'


## 分支
### 列出分支
git branch

### 新建分支
git branch name
### 新建分支并切换
git checkout -b name

### 切换分支 
git checkout name

### 合并指定分支到当前分支
git merge name

### 删除分支
git branch -d name

### 删除远程分支

git push origin --delete [branch-name]
git branch -dr [remote/branch]














### 查看git日志，一条一行
git log --pretty=oneline
