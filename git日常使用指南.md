# git日常使用指南

## 常用指令

>## 常用命令
>
>> - cd ：改变目录；
>> - cd . .  ：回退到上一个目录，直接cd进入默认目录；
>> - pwd：显示当前所处目录路径；
>> - ls：显示当前目录下所有文件，ls（ll）显示内容更加详细；
>> - touch : 新建一个文件 如 touch index.js 就会在当前目录下新建一个index.js文件；
>> - rm:  删除一个文件, rm index.js 就会把index.js文件删除；
>> - mkdir:  新建一个目录,就是新建一个文件夹；
>> - rm -r :  删除一个文件夹, rm -r src 删除src目录

```bash
rm -rf /  # 不要再Linux环境下轻易使用，否者会删除所有文件，也就是传说中的删库跑路，要想好！！！
```

> > - mv 移动文件, mv index.html src index.html 是我们要移动的文件, src 是目标文件夹,当然, 这样写,必须保证文件和目标文件夹在同一目录下;
> > - reset: 重新初始化终端/清屏;
> > - clear:清屏；
> > - history ：查看命令历史；
> > - help：帮助；
> > - exit ：退出；
> > - “#” ： 注释；

```bash
git config - l # 参看配置信息
```

![image-20211229223754501](C:\Users\o水歌儿\AppData\Roaming\Typora\typora-user-images\image-20211229223754501.png)

> ##  git 配置文件
>
> >
> >
> >> - Git\etc\gitconfig  ：Git 安装目录下的 gitconfig   --system 系统级
> >> - C:\Users\Administrator\ .gitconfig   只适用于当前登录用户的配置  --global 全局

>
>
>## 设置用户名邮箱
>
>>
>>
>>> ```bash
>>> #当你安装Git后首先要做的事情是设置你的用户名称和e-mail地址。这是非常重要的，因为每次Git提交都会使用该信息。它被永远的嵌入到了你的提交中。
>>> git config --global user.name "stephensong" #设置用户名
>>> git config --global user.email ****@qq.com #设置邮箱
>>> git config --glbal --list # 查看当前有哪些用户信息；
>>> ```

## git基本理论

> ## 三个区域
>
> Git本地有三个工作区域：工作目录（Working Directory）、暂存区(Stage/Index)、资源库(Repository或Git Directory)。如果在加上远程的git仓库(Remote Directory)就可以分为四个工作区域。文件在这四个区域之间的转换关系如下：
> ![image-20211229225543428](C:\Users\o水歌儿\AppData\Roaming\Typora\typora-user-images\image-20211229225543428.png)
>
> - Workspace：工作区，就是你平时存放项目代码的地方；
>
> - Index / Stage：暂存区，用于临时存放你的改动，事实上它只是一个文件，保存即将提交到文件列表信息；
>
> - Repository：仓库区（或本地仓库），就是安全存放数据的位置，这里面有你提交到所有版本的数据。其中HEAD指向最新放入仓库的版本；
>
> - Remote：远程仓库，托管代码的服务器，可以简单的认为是你项目组中的一台电脑用于远程数据交换
>
>   ```bash
>   git add . -> git commit ->git push # 这一套命令完成本地到远程仓库的提交；
>   ```

## 创建仓库

>## 仓库创建两种方式
>
>- ```bash
>  git init # 在当前目录新建一个代码库；
>  ```
>
>  ```bash
>  git clone [url] # 从远程clone一个远程仓库；
>  ```

## 文件的状态

> 版本控制就是对文件的版本控制，要对文件进行修改、提交等操作，首先要知道文件当前在什么状态，不然可能会提交了现在还不想提交的文件，或者要提交的文件没提交上。
>
> > - Untracked: 未跟踪, 此文件在文件夹中, 但并没有加入到git库, 不参与版本控制. 通过git add 状态变为Staged;
> > - Unmodify: 文件已经入库, 未修改, 即版本库中的文件快照内容与文件夹中完全一致. 这种类型的文件有两种去处, 如果它被修改, 而变为Modified. 如果使用git rm移出版本库, 则成为Untracked文件;
> > - Modified: 文件已修改, 仅仅是修改, 并没有进行其他的操作. 这个文件也有两个去处, 通过git add可进入暂存staged状态, 使用git checkout 则丢弃修改过, 返回到unmodify状态, 这个git checkout即从库中取出文件, 覆盖当前修改 !
> > - Staged: 暂存状态. 执行git commit则将修改同步到库中, 这时库中的文件和本地文件又变为一致, 文件为Unmodify状态. 执行git reset HEAD filename取消暂存, 文件状态为Modified;

> ## 查看文件状态
>
> ```bash
> git status # 查看所有文件的状态；
> git status [filename] # 查看指定文件的状态；
> git add. # 添加所有文件进入暂存区；
> git commit -m "消息内容" # 提交暂存区的内容到本地仓库；
> ```
>
> ## 忽略文件
>
> 有些时候我们不想把某些文件纳入版本控制中，比如数据库文件，临时文件，设计文件等
>
> 在主目录下建立".gitignore"文件，此文件有如下规则：
>
> - 忽略文件中的空行或以井号（#）开始的行将会被忽略；
>
> - 可以使用Linux通配符。例如：星号（*）代表任意多个字符，问号（？）代表一个字符，方括号（[abc]）代表可选字符范围，大括号（{string1,string2,...}）代表可选的字符串等；
>
> - 如果名称的最前面有一个感叹号（!），表示例外规则，将不被忽略；
>
> - 如果名称的最前面是一个路径分隔符（/），表示要忽略的文件在此目录下，而子目录中的文件不忽略；
>
> - 如果名称的最后面是一个路径分隔符（/），表示要忽略的是此目录下该名称的子目录，而非文件（默认文件或目录都忽略）；
>
> - ```bash
>   *.txt # 忽略所有.txt结尾的文件，这样上传就不会被选中；
>   ！lib.txt # 但lib.txt除外；
>   /temp # 仅忽略项目根目录下的TODO文件，不包括其他目录temp；
>   build/ # 忽略build/下的所有文件；
>   doc/*.txt # 会忽略doc/notes.txt，但不会忽略doc/servers/arch.txt
>   ```

