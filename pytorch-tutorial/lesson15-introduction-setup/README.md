# 第15课：PyTorch简介与环境搭建

## 📖 学习目标
- 了解PyTorch的历史和特点
- 理解PyTorch与其他深度学习框架的区别
- 掌握PyTorch的安装方法
- 编写第一个PyTorch程序
- 学会使用Jupyter Notebook进行PyTorch开发

## 📚 理论知识

### 什么是PyTorch？
PyTorch是由Facebook（现Meta）人工智能研究团队开发的开源深度学习框架。它具有以下特点：

#### 核心特点
1. **动态计算图**：计算图在运行时构建，便于调试
2. **Pythonic风格**：API设计符合Python编程习惯
3. **易于调试**：可以使用标准Python调试工具
4. **强大的社区支持**：活跃的开发社区和丰富的资源
5. **生产就绪**：支持从研究到生产的完整流程

#### PyTorch vs TensorFlow

| 特性 | PyTorch | TensorFlow |
|------|---------|------------|
| 计算图 | 动态图 | 静态图（TF2.x也支持动态图） |
| API风格 | Pythonic | 自成体系 |
| 调试难度 | 容易 | 相对困难 |
| 学习曲线 | 平缓 | 陡峭 |
| 生产部署 | 成熟 | 非常成熟 |
| 移动端支持 | 良好 | 优秀 |

### PyTorch的核心组件

#### 1. torch
核心张量库，提供多维数组和数学运算功能。

#### 2. torch.autograd
自动求导系统，支持梯度计算和反向传播。

#### 3. torch.nn
神经网络模块，提供构建神经网络的层和损失函数。

#### 4. torch.optim
优化器模块，提供各种优化算法。

#### 5. torch.utils
实用工具，包括数据处理、模型保存等功能。

## 🛠️ 环境搭建

### 1. 系统要求
- Python 3.8-3.11
- 操作系统：Windows、macOS、Linux
- 内存：至少4GB RAM（推荐8GB+）
- 显卡：NVIDIA GPU（可选，用于CUDA加速）

### 2. 安装方法

#### 方法一：使用pip安装（推荐）
```bash
# CPU版本
pip install torch torchvision torchaudio

# GPU版本（CUDA 11.8）
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

# GPU版本（CUDA 12.1）
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```

#### 方法二：使用conda安装
```bash
# CPU版本
conda install pytorch torchvision torchaudio cpuonly -c pytorch

# GPU版本
conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia
```

### 3. 验证安装

创建一个Python脚本验证安装：

```python
import torch

print(f"PyTorch版本：{torch.__version__}")
print(f"CUDA是否可用：{torch.cuda.is_available()}")

if torch.cuda.is_available():
    print(f"CUDA版本：{torch.version.cuda}")
    print(f"GPU数量：{torch.cuda.device_count()}")
    print(f"当前GPU：{torch.cuda.get_device_name(0)}")
```

### 4. Jupyter Notebook安装

```bash
# 安装Jupyter
pip install jupyter

# 启动Jupyter
jupyter notebook
```

## 💻 第一个PyTorch程序

### 基础张量操作
```python
import torch

# 创建张量
x = torch.tensor([1, 2, 3, 4])
y = torch.tensor([5, 6, 7, 8])

# 基本运算
print(f"x + y = {x + y}")
print(f"x * y = {x * y}")
print(f"x 的平方 = {x ** 2}")

# 创建矩阵
matrix = torch.tensor([[1, 2], [3, 4]])
print(f"矩阵：\n{matrix}")
print(f"矩阵形状：{matrix.shape}")
```

### GPU加速示例
```python
import torch

# 检查GPU可用性
if torch.cuda.is_available():
    # 创建张量并移动到GPU
    x = torch.randn(1000, 1000)
    y = torch.randn(1000, 1000)
    
    # CPU计算
    import time
    start_time = time.time()
    z_cpu = torch.mm(x, y)
    cpu_time = time.time() - start_time
    
    # GPU计算
    x_gpu = x.cuda()
    y_gpu = y.cuda()
    start_time = time.time()
    z_gpu = torch.mm(x_gpu, y_gpu)
    gpu_time = time.time() - start_time
    
    print(f"CPU计算时间：{cpu_time:.4f}秒")
    print(f"GPU计算时间：{gpu_time:.4f}秒")
    print(f"加速比：{cpu_time/gpu_time:.2f}x")
else:
    print("GPU不可用，使用CPU计算")
```

## ✏️ 练习题目

### 练习1：环境检查
编写程序检查你的PyTorch环境。

```python
import torch

# 检查PyTorch版本
print(f"PyTorch版本：{torch.__version__}")

# 检查CUDA可用性
print(f"CUDA可用：{torch.cuda.is_available()}")

# 如果有GPU，显示GPU信息
if torch.cuda.is_available():
    print(f"GPU数量：{torch.cuda.device_count()}")
    for i in range(torch.cuda.device_count()):
        print(f"GPU {i}：{torch.cuda.get_device_name(i)}")
```

### 练习2：张量创建练习
创建不同类型的张量。

```python
import torch

# 创建不同类型的张量
tensor_int = torch.tensor([1, 2, 3])
tensor_float = torch.tensor([1.0, 2.0, 3.0])
tensor_zeros = torch.zeros(3, 3)
tensor_ones = torch.ones(2, 4)
tensor_random = torch.randn(2, 3)

print("整数张量：", tensor_int)
print("浮点张量：", tensor_float)
print("零张量：", tensor_zeros)
print("一张量：", tensor_ones)
print("随机张量：", tensor_random)
```

### 练习3：简单计算
使用PyTorch进行数学运算。

```python
import torch

# 创建两个矩阵
A = torch.tensor([[1, 2], [3, 4]])
B = torch.tensor([[5, 6], [7, 8]])

# 矩阵运算
print("矩阵A：\n", A)
print("矩阵B：\n", B)
print("A + B：\n", A + B)
print("A * B (元素乘)：\n", A * B)
print("A @ B (矩阵乘)：\n", A @ B)
```

### 练习4：GPU加速测试
比较CPU和GPU的计算性能。

```python
import torch
import time

# 创建大矩阵
size = 2000
x = torch.randn(size, size)
y = torch.randn(size, size)

# CPU计算
start = time.time()
z_cpu = torch.mm(x, y)
cpu_time = time.time() - start
print(f"CPU计算时间：{cpu_time:.4f}秒")

# GPU计算（如果可用）
if torch.cuda.is_available():
    x_gpu = x.cuda()
    y_gpu = y.cuda()
    
    start = time.time()
    z_gpu = torch.mm(x_gpu, y_gpu)
    torch.cuda.synchronize()  # 等待GPU完成
    gpu_time = time.time() - start
    print(f"GPU计算时间：{gpu_time:.4f}秒")
    print(f"加速比：{cpu_time/gpu_time:.2f}x")
else:
    print("GPU不可用")
```

## 🎯 挑战任务

编写一个PyTorch程序，实现以下功能：
1. 创建一个5x5的随机矩阵
2. 计算矩阵的转置
3. 计算矩阵的行列式
4. 对矩阵进行奇异值分解
5. 比较CPU和GPU的计算时间

```python
import torch
import time

def matrix_operations_demo():
    print("=== PyTorch矩阵操作演示 ===")
    
    # 创建5x5随机矩阵
    matrix = torch.randn(5, 5)
    print(f"原始矩阵：\n{matrix}")
    
    # 计算转置
    transpose = matrix.T
    print(f"\n转置矩阵：\n{transpose}")
    
    # 计算行列式
    det = torch.det(matrix)
    print(f"\n行列式：{det:.6f}")
    
    # 奇异值分解
    U, S, V = torch.svd(matrix)
    print(f"\n奇异值：{S}")
    
    # GPU性能测试
    if torch.cuda.is_available():
        large_matrix = torch.randn(1000, 1000)
        
        # CPU测试
        start = time.time()
        cpu_result = torch.mm(large_matrix, large_matrix.T)
        cpu_time = time.time() - start
        
        # GPU测试
        gpu_matrix = large_matrix.cuda()
        start = time.time()
        gpu_result = torch.mm(gpu_matrix, gpu_matrix.T)
        torch.cuda.synchronize()
        gpu_time = time.time() - start
        
        print(f"\nCPU计算时间：{cpu_time:.4f}秒")
        print(f"GPU计算时间：{gpu_time:.4f}秒")
        print(f"GPU加速比：{cpu_time/gpu_time:.2f}x")

# 运行演示
matrix_operations_demo()
```

## 📝 学习笔记

请记录以下内容：
1. PyTorch的主要特点和优势
2. 安装过程中遇到的问题和解决方法
3. PyTorch与TensorFlow的区别
4. GPU加速的重要性

## 🔗 扩展阅读

- [PyTorch官方教程](https://pytorch.org/tutorials/)
- [PyTorch 60分钟入门](https://pytorch.org/tutorials/beginner/deep_learning_60min_blitz.html)
- [PyTorch官方文档](https://pytorch.org/docs/stable/)

---

**下节课预告**：张量基础 - 深入学习PyTorch的核心数据结构：张量。
