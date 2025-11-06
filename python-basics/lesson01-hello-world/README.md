# 第1课：Python简介与环境搭建

## 📖 学习目标
- 了解Python语言的特点和应用领域
- 掌握Python环境的安装方法
- 编写并运行第一个Python程序
- 学会使用基本的开发工具

## 📚 理论知识

### 什么是Python？
Python是一种高级编程语言，具有以下特点：
- **简洁易读**：语法简单，接近自然语言
- **跨平台**：可在Windows、macOS、Linux上运行
- **功能强大**：拥有丰富的标准库和第三方库
- **应用广泛**：Web开发、数据科学、人工智能、自动化等

### 为什么学习Python？
1. **入门简单**：语法规则少，学习曲线平缓
2. **需求量大**：就业前景好，薪资水平高
3. **生态丰富**：众多优秀的框架和库
4. **社区活跃**：遇到问题容易找到解决方案

### Python的应用领域
- **Web开发**：Django、Flask框架
- **数据科学**：NumPy、Pandas、Matplotlib
- **人工智能**：TensorFlow、PyTorch
- **自动化运维**：脚本编写、系统管理
- **游戏开发**：Pygame引擎

## 🛠️ 环境搭建

### 1. 安装Python
访问[Python官网](https://www.python.org/downloads/)下载最新版本：
- Windows：下载安装包，勾选"Add Python to PATH"
- macOS：使用Homebrew或下载安装包
- Linux：使用包管理器安装

### 2. 验证安装
打开终端/命令提示符，输入：
```bash
python --version
```
或
```bash
python3 --version
```

### 3. 安装代码编辑器
推荐使用以下编辑器之一：
- **Visual Studio Code**：功能强大，插件丰富
- **PyCharm**：专业的Python IDE
- **Jupyter Notebook**：适合学习和实验

## 💻 第一个Python程序

### Hello World程序
创建一个名为`hello.py`的文件，输入以下代码：

```python
# 这是我的第一个Python程序
print("Hello, World!")
print("欢迎来到Python的世界！")
```

### 运行程序
在终端中执行：
```bash
python hello.py
```

### 预期输出
```
Hello, World!
欢迎来到Python的世界！
```

## 🔍 代码解释

1. **注释**：以`#`开头的行为注释，不会被程序执行
2. **print()函数**：用于输出内容到控制台
3. **字符串**：用引号包围的文本内容
4. **中文支持**：Python 3默认支持UTF-8编码

## ✏️ 练习题目

### 练习1：环境检查
编写程序检查你的Python版本，并输出安装信息。

```python
import sys
print(f"Python版本：{sys.version}")
print(f"Python安装路径：{sys.executable}")
```

### 练习2：个人信息输出
编写程序输出你的个人信息，包括姓名、年龄、爱好等。

```python
# 请在这里编写你的代码
print("姓名：张三")
print("年龄：20")
print("爱好：编程")
```

### 练习3：计算器雏形
编写程序进行简单的数学运算并输出结果。

```python
# 请在这里编写你的代码
print("10 + 5 =", 10 + 5)
print("10 - 5 =", 10 - 5)
print("10 * 5 =", 10 * 5)
print("10 / 5 =", 10 / 5)
```

### 练习4：艺术字输出
使用print函数输出简单的ASCII艺术。

```python
# 请在这里编写你的代码
print("   *   ")
print("  ***  ")
print(" ***** ")
print("*******")
print("  | |  ")
```

## 🎯 挑战任务

尝试编写一个程序，输出一个简单的自我介绍，包括：
- 你的名字
- 你为什么学习Python
- 你希望通过Python实现什么

示例输出：
```
我叫李明，我学习Python是因为它简单易学。
我希望通过Python开发有趣的人工智能应用。
```

## 📝 学习笔记

请记录以下内容：
1. Python安装过程中遇到的问题和解决方法
2. 你选择的代码编辑器及其优缺点
3. 对Python的第一印象
4. 本次课程的重要知识点

## 🔗 扩展阅读

- [Python官方教程](https://docs.python.org/zh-cn/3/tutorial/)
- [Python编程：从入门到实践](https://book.douban.com/subject/26829016/)
- [菜鸟教程Python3](https://www.runoob.com/python3/python3-tutorial.html)

---

**下节课预告**：变量与数据类型 - 学习如何在Python中存储和操作不同类型的数据。
