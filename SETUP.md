# 环境搭建指南

本指南将帮助你快速搭建Python和PyTorch学习环境。

## 🚀 快速开始

### 1. 克隆项目
```bash
git clone <repository-url>
cd my-project
```

### 2. 创建虚拟环境（推荐）

#### 使用conda
```bash
# 创建新环境
conda create -n pytorch-tutorial python=3.9

# 激活环境
conda activate pytorch-tutorial

# 安装依赖
pip install -r requirements.txt
```

#### 使用venv
```bash
# 创建虚拟环境
python -m venv pytorch-tutorial

# 激活环境
# Windows
pytorch-tutorial\Scripts\activate
# macOS/Linux
source pytorch-tutorial/bin/activate

# 安装依赖
pip install -r requirements.txt
```

### 3. 验证安装

#### 检查Python环境
```bash
python --version
pip list
```

#### 检查PyTorch安装
```bash
python -c "import torch; print(f'PyTorch版本：{torch.__version__}'); print(f'CUDA可用：{torch.cuda.is_available()}')"
```

#### 运行示例程序
```bash
cd python-basics/lesson01-hello-world
python hello.py

cd ../../pytorch-tutorial/lesson15-introduction-setup
python pytorch_intro.py
```

## 📋 详细安装步骤

### Python安装

#### Windows
1. 访问 [Python官网](https://www.python.org/downloads/)
2. 下载最新版本的Python安装包
3. 运行安装程序，勾选"Add Python to PATH"
4. 验证安装：打开命令提示符输入`python --version`

#### macOS
```bash
# 使用Homebrew安装
brew install python@3.9

# 或者从官网下载安装包
```

#### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv
```

### PyTorch安装

#### CPU版本（适合初学者）
```bash
pip install torch torchvision torchaudio
```

#### GPU版本（需要NVIDIA显卡）
```bash
# CUDA 11.8
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

# CUDA 12.1
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```

### 开发工具安装

#### Jupyter Notebook
```bash
pip install jupyter notebook
```

启动Jupyter：
```bash
jupyter notebook
```

#### VS Code插件推荐
- Python
- Jupyter
- Pylance
- Python Docstring Generator

## 🔧 环境配置

### 验证GPU支持
```python
import torch

print(f"PyTorch版本：{torch.__version__}")
print(f"CUDA可用：{torch.cuda.is_available()}")

if torch.cuda.is_available():
    print(f"CUDA版本：{torch.version.cuda}")
    print(f"GPU数量：{torch.cuda.device_count()}")
    print(f"当前GPU：{torch.cuda.get_device_name(0)}")
```

### 测试基本功能
```python
# 测试PyTorch基础功能
import torch

# 创建张量
x = torch.randn(2, 3)
y = torch.randn(2, 3)

# 基本运算
z = x + y
print("张量运算测试通过！")

# GPU测试（如果可用）
if torch.cuda.is_available():
    x_gpu = x.cuda()
    y_gpu = y.cuda()
    z_gpu = x_gpu + y_gpu
    print("GPU运算测试通过！")
```

## 📚 学习资源

### 在线文档
- [Python官方文档](https://docs.python.org/zh-cn/3/)
- [PyTorch官方文档](https://pytorch.org/docs/)
- [PyTorch中文教程](https://pytorch-cn.readthedocs.io/)

### 推荐书籍
- 《Python编程：从入门到实践》
- 《PyTorch:入门与实践》(陈云著)
- 《深度学习入门：基于Python的理论与实现》

### 在线课程
- [Coursera - Deep Learning](https://www.coursera.org/specializations/deep-learning)
- [fast.ai - Practical Deep Learning for Coders](https://course.fast.ai/)

## ❓ 常见问题

### Q: 如何选择CPU或GPU版本？
A: 如果你有NVIDIA显卡且显存大于4GB，推荐安装GPU版本，可以显著提升训练速度。否则选择CPU版本即可。

### Q: 安装过程中遇到权限错误怎么办？
A: 在命令前加上`sudo`（Linux/macOS）或以管理员身份运行命令提示符（Windows）。

### Q: 如何更新PyTorch？
A: 运行`pip install --upgrade torch torchvision torchaudio`

### Q: Jupyter Notebook无法启动怎么办？
A: 尝试重新安装：`pip install --upgrade --force-reinstall jupyter notebook`

### Q: 如何检查CUDA版本？
A: 在命令行输入`nvidia-smi`或`nvcc --version`

## 🎯 下一步

环境搭建完成后，你可以：
1. 从[Python基础](./python-basics/)部分开始学习
2. 运行示例代码验证环境
3. 加入学习社区，与其他学习者交流

祝你学习愉快！🎉
