#Ansible 测试

## Playbook
roles的文件结构：
- files/：此角色中用到的所有文件均放置于此目录中
- templates/： Jinja2模板文件存放位置
- tasks/：任务列表文件；可以有多个，但至少有一个叫做main.yml的文件
- handlers/：处理器列表文件；可以有多个，但至少有一个叫做main.yml的文件
- vars/：变量字典文件；可以有多个，但至少有一个叫做main.yml的文件
- meta/：此角色的特殊设定及依赖关系

> mkdir -p base/{files,templates,tasks,handlers,vars,meta}   
> touch base/{tasks,handlers,vars}/main.yaml  

使用 ansible-galaxy 命令可以自动生成对应的文件结构
> ansible-galaxy init test
