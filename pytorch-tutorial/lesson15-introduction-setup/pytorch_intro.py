# PyTorch简介与环境搭建演示程序

import torch
import time

print("=== PyTorch环境检查 ===\n")

# 1. 检查PyTorch版本
print(f"PyTorch版本：{torch.__version__}")
print(f"CUDA是否可用：{torch.cuda.is_available()}")

if torch.cuda.is_available():
    print(f"CUDA版本：{torch.version.cuda}")
    print(f"GPU数量：{torch.cuda.device_count()}")
    for i in range(torch.cuda.device_count()):
        print(f"GPU {i}：{torch.cuda.get_device_name(i)}")
print()

# 2. 基础张量操作
print("=== 基础张量操作 ===\n")

# 创建张量
x = torch.tensor([1, 2, 3, 4], dtype=torch.float32)
y = torch.tensor([5, 6, 7, 8], dtype=torch.float32)

print(f"张量x：{x}")
print(f"张量y：{y}")
print(f"x + y = {x + y}")
print(f"x * y = {x * y}")
print(f"x ** 2 = {x ** 2}")
print()

# 3. 矩阵操作
print("=== 矩阵操作 ===\n")

# 创建矩阵
matrix = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)
print(f"矩阵：\n{matrix}")
print(f"矩阵形状：{matrix.shape}")
print(f"矩阵维度：{matrix.dim()}")
print(f"矩阵元素个数：{matrix.numel()}")

# 矩阵运算
A = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)
B = torch.tensor([[5, 6], [7, 8]], dtype=torch.float32)

print(f"\n矩阵A：\n{A}")
print(f"矩阵B：\n{B}")
print(f"A + B：\n{A + B}")
print(f"A * B (元素乘)：\n{A * B}")
print(f"A @ B (矩阵乘)：\n{A @ B}")
print()

# 4. 不同类型的张量创建
print("=== 张量创建方法 ===\n")

tensor_zeros = torch.zeros(3, 3)
tensor_ones = torch.ones(2, 4)
tensor_random = torch.randn(2, 3)
tensor_arange = torch.arange(0, 10, 2)
tensor_linspace = torch.linspace(0, 1, 5)

print("零张量：\n", tensor_zeros)
print("一张量：\n", tensor_ones)
print("随机张量：\n", tensor_random)
print("等差张量：", tensor_arange)
print("线性空间张量：", tensor_linspace)
print()

# 5. GPU性能测试
print("=== GPU性能测试 ===\n")

if torch.cuda.is_available():
    # 创建大矩阵进行性能测试
    size = 1000
    x = torch.randn(size, size)
    y = torch.randn(size, size)
    
    # CPU计算
    start_time = time.time()
    z_cpu = torch.mm(x, y)
    cpu_time = time.time() - start_time
    print(f"CPU矩阵乘法时间：{cpu_time:.4f}秒")
    
    # GPU计算
    x_gpu = x.cuda()
    y_gpu = y.cuda()
    start_time = time.time()
    z_gpu = torch.mm(x_gpu, y_gpu)
    torch.cuda.synchronize()  # 等待GPU完成计算
    gpu_time = time.time() - start_time
    print(f"GPU矩阵乘法时间：{gpu_time:.4f}秒")
    print(f"GPU加速比：{cpu_time/gpu_time:.2f}x")
    
    # 内存使用情况
    print(f"\nGPU内存使用：{torch.cuda.memory_allocated()/1024**3:.2f}GB")
    print(f"GPU内存缓存：{torch.cuda.memory_reserved()/1024**3:.2f}GB")
else:
    print("GPU不可用，使用CPU计算")
    
    # CPU性能测试
    size = 1000
    x = torch.randn(size, size)
    y = torch.randn(size, size)
    
    start_time = time.time()
    z = torch.mm(x, y)
    cpu_time = time.time() - start_time
    print(f"CPU矩阵乘法时间：{cpu_time:.4f}秒")

print()

# 6. 自动求导示例
print("=== 自动求导示例 ===\n")

# 创建需要梯度的张量
x = torch.tensor(2.0, requires_grad=True)
y = torch.tensor(3.0, requires_grad=True)

# 计算函数：z = x² + 2xy + y²
z = x**2 + 2*x*y + y**2

print(f"x = {x}, y = {y}")
print(f"z = x² + 2xy + y² = {z}")

# 计算梯度
z.backward()

print(f"∂z/∂x = {x.grad}")  # 2x + 2y = 2*2 + 2*3 = 10
print(f"∂z/∂y = {y.grad}")  # 2x + 2y = 2*2 + 2*3 = 10

print("\n=== 演示完成 ===")
print("恭喜！你已经成功运行了第一个PyTorch程序。")
