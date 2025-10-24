# GitHub同步指南

本指南将帮助你将本地的词云分析项目与GitHub仓库关联并进行同步。

## 一、前置准备

### 1. 安装Git
- Windows 用户：
  1. 打开 **Anaconda Prompt**，输入 `git --version`  
     - 若返回版本号，说明已自带 Git，可跳过后续步骤；  
     - 若提示“不是内部或外部命令”，请继续以下安装流程。  
  2. 访问 [Git 官网](https://git-scm.com/download/win)  
  3. 在下载页面按处理器类型选择安装包：
  **如何查看处理器类型？**  
    1. 同时按下 `Win + R`，输入 `msinfo32` 回车，打开“系统信息”。  
    2. 在右侧找到“处理器”一行，即可看到完整型号；若含“ARM”字样即为 ARM 架构，否则为 Intel/AMD x64。  
    3. 也可在任务管理器（`Win + R` 输入 `taskmgr` 回车/快捷键：Ctrl + Shift + Esc） → 性能 → CPU 页签中查看“架构”字段（本电脑的CPU架构为**CPU：Intel(R) Core(TM) 5 210H**）故为**64位Intel/AMD架构**。
     - 绝大多数电脑为 **64 位 Intel/AMD**，选 **“Standalone Installer → Git for Windows/x64 Setup”**  
     - 若使用 **ARM 架构 Windows 设备**（如 Surface Pro X），选 **“Git for Windows/ARM64 Setup”**  
     - 不确定时，按 `Win + Pause` 打开“系统信息”查看“系统类型”。  
  4. 下载后一路“下一步”完成安装（保持默认选项即可）。  
  5. 安装完成后，重新打开 **命令提示符**、**PowerShell** 或 **Anaconda Prompt**，输入 `git --version` 验证安装成功。


- 访问 [GitHub官网](https://github.com/)
- 注册一个新账号或使用现有账号
- 现有账号为：runyoung0613
- 地址为：https://github.com/runyoung0613

### 2. 配置Git全局设置
- 打开 PowerShell 或命令提示符
- 执行以下命令设置用户名和邮箱（替换为你自己的信息）：
  ```bash
  git config --global user.name "runyoung"
  git config --global user.email "2483182481@qq.com"
  ```

## 二、本地项目初始化

### 1. 在项目目录初始化Git仓库

- **Windows 10/11 快速打开 PowerShell：**
  1. 按下 `Win + X` 组合键，在弹出的菜单中选择 **“Windows PowerShell”** 或 **“终端(Terminal)”**。
  2. 也可直接在任务栏搜索框输入 **PowerShell**，点击搜索结果中的 **“Windows PowerShell”**。

- **传统方式打开命令提示符：**
  1. 按下 `Win + R`，输入 **cmd**，回车即可打开命令提示符。
  2. 或者在开始菜单中搜索 **cmd**，点击 **“命令提示符”**。

- **在项目目录打开 PowerShell 或命令提示符后，执行以下命令：**
  ```bash
  git init
  ```
  - 若提示“Reinitialized existing Git repository”或“Initialized empty Git repository”，均属正常。
  - 系统只是重新初始化了它，这是完全正常的操作。

### 2. 创建.gitignore文件（推荐）
- 新建一个文本文件，命名为 **.gitignore**（注意文件名前有个点）。  
  这个文件的作用是告诉 Git 哪些文件或目录无需纳入版本控制，例如临时文件、日志、虚拟环境、大型结果图片等，避免把它们推送到 GitHub，既节省仓库空间，也保护隐私。

- 保存文件到项目根目录  
  把刚才新建/编辑好的 **.gitignore** 文件直接放到 **E:\Word_cloud_analysis**（即你当前项目的顶层文件夹）。  
  保存后，文件资源管理器里应能看到它与 `*.py`、数据文件夹等并列，证明位置正确。

### 3. bash 配置
- **bash的作用**：Git Bash 让 Windows 也能跑 Linux 命令，复制粘贴零改动。  

PS E:\Word_cloud_analysis> bash
<3>WSL (10 - Relay) ERROR: CreateProcessCommon:798: execvpe(/bin/bash) failed: No such file or directory

- **配置bash环境变量**
1. 右键点击「此电脑」→「属性」→「高级系统设置」→「环境变量」
2. 在「系统变量」中找到并选择「Path」变量，点击「编辑」
3. 点击「新建」，添加以下Git相关路径（根据您的实际安装位置可能有所不同）：
   - E:\git\Git\bin - 包含bash.exe和一些基础的Linux工具
   - E:\git\Git\usr\bin - 包含更多的Linux风格命令行工具
4. 点击「确定」保存所有设置
5. 关闭并重新打开PowerShell，使设置生效

- 出现这样的错误信息，表明系统正在尝试访问Linux风格路径 /bin/bash ，这是WSL的bash路径，而不是Git安装的bash。
在PowerShell中使用Git Bash的完整路径来启动，例如：
& "E:\git\Git\bin\bash.exe"

执行 & "E:\git\Git\bin\bash.exe" 命令后，**会进入一个bash会话环境，但它是在当前PowerShell窗口内部运行的bash，而不是一个完全独立的窗口。**

### 4. 终端使用指南
1. PowerShell（Windows 默认终端）
 **适用场景**  
   仅需执行 Git 命令（git init / add / commit / push 等）  
   熟悉 Windows 命令，不想额外切换窗口  
 **优势**  
  完成 GitHub 同步的核心操作完全够用，无需安装其他终端。

2. Git Bash
**适用场景**  
  习惯 Linux 风格命令（ls -la、cd、mkdir 等）  
  需运行复杂 shell 脚本或命令组合  
  偏好 Unix/Linux 命令行环境  
**优势**  
  提供与 Linux 一致的完整命令体验。

### 5. 本地项目准备
以下步骤将把“E:\Word_cloud_analysis”文件夹正式转化为 Git 仓库，并完成首次提交。请严格按顺序执行，每步均给出目的、命令与排错提示。

#### 5.1 进入项目目录
1. 打开 **PowerShell** 或 **Anaconda Prompt**
2. 输入并回车：
   ```powershell
   cd E:\Word_cloud_analysis
   ```
3. 验证：执行 `pwd`（PowerShell）或 `cd`（cmd），应回显 `E:\Word_cloud_analysis`

#### 5.2 初始化仓库
1. 执行以下命令初始化Git仓库：
   ```bash
   git init
   ```
  后终端返回：
   PS E:\Word_cloud_analysis> git init
   Reinitialized existing Git repository in E:/Word_cloud_analysis/.git/
   ```  
   这说明：  
   1. **目录早已是 Git 仓库**：`.git` 文件夹已存在，无需新建。  
   2. **“Reinitialized” 仅重置配置**：Git 重新读取该目录下的 `.git` 配置，**不会删除或覆盖你之前的任何提交历史、分支与文件**。  
   3. **可继续正常使用**：直接 `git status` / `git add` / `git commit` 即可，无需额外处理。  
   简言之，这条提示只是告诉你“这里本来就是仓库，放心用”。
2. 验证：执行 `git status`，应显示 "On branch master"（或 "On branch main"，根据你的默认分支）

#### 5.3 首次提交
1. 执行以下命令添加所有文件到暂存区：
   ```bash
   git add .
   ```
2. 提交到本地仓库：
   ```bash
   git commit -m "初始化项目"
   ```
3. 验证：执行 `git status`，应显示 "nothing to commit, working tree clean"

## 三、在GitHub创建远程仓库

1. 登录GitHub账号
2. 点击右上角的 "+" 图标，选择 "New repository"
3. 填写仓库信息：
   - Repository name: 例如 "word-cloud-analysis"
   - Description: 简要描述你的项目
   - 选择 Public 或 Private
   - 不要勾选 "Initialize this repository with a README"（因为我们已经有README了）
4. 点击 "Create repository"

## 四、关联本地仓库和远程仓库

创建完GitHub仓库后，你会看到一些命令提示。复制其中的 "git remote add origin" 命令，在本地执行：

```bash
# 将 [your_username] 和 [repository_name] 替换为你实际的GitHub用户名和仓库名
git remote add origin https://github.com/[your_username]/[repository_name].git

# 验证远程仓库连接
git remote -v
```

## 五、推送到GitHub

### 1. 首次推送

```bash
# 将本地master分支推送到远程仓库（GitHub现在默认为main分支）
git push -u origin master
```

如果GitHub提示默认分支是main而不是master，你可以：

```bash
# 将本地master重命名为main
git branch -M main

# 推送到远程main分支
git push -u origin main
```

### 2. 输入GitHub凭证

首次推送时，系统会提示你输入GitHub的用户名和密码（或个人访问令牌）。

**注意：** 自2021年8月起，GitHub不再支持使用密码进行身份验证，你需要创建个人访问令牌（PAT）。

#### 如何创建个人访问令牌：

1. 登录GitHub，点击右上角头像 -> Settings
2. 选择 Developer settings -> Personal access tokens -> Tokens (classic)
3. 点击 "Generate new token" -> "Generate new token (classic)"
4. 设置Token名称，选择权限（至少需要repo权限）
5. 点击 "Generate token" 并复制生成的令牌
6. 推送到GitHub时，将密码替换为这个令牌

## 六、后续工作流程

### 1. 日常修改和同步

```bash
# 查看文件状态
git status

# 添加修改的文件
git add .  # 添加所有修改
git add 特定文件路径  # 添加特定文件

# 提交修改
git commit -m "描述你的修改内容"

# 推送到GitHub
git push
```

### 2. 从GitHub拉取更新

如果你在其他地方修改了代码，或者团队成员提交了更改，可以拉取最新内容：

```bash
# 拉取远程更新
git pull
```

## 七、使用Anaconda命令行工具

如果你使用的是Anaconda Prompt，可以直接在Anaconda环境中执行上述Git命令，这样可以确保使用正确的Python环境。

## 八、常见问题解决

### 1. 权限问题
- 确保你的个人访问令牌有正确的权限
- 检查GitHub账户是否正确关联

### 2. 分支冲突
- 如果多人同时修改同一文件，可能会产生冲突
- 需要手动解决冲突，然后重新提交

### 3. 大型文件上传
- GitHub对单个文件大小有限制（通常是100MB）
- 对于大型词云图片或分析结果，考虑使用.gitignore排除它们

## 九、推荐使用的Git客户端（可选）

如果你不熟悉命令行，可以考虑使用图形化Git客户端：

- GitHub Desktop: 官方的GitHub客户端，简单易用
- GitKraken: 功能强大的Git GUI工具
- SourceTree: Atlassian开发的免费Git客户端

---

按照以上步骤操作后，你的本地词云分析项目就成功地与GitHub仓库关联并同步了。这样你就可以在不同设备上访问你的代码，也方便与他人分享或协作开发。