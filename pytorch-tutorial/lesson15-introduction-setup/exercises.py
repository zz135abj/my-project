# PyTorch环境搭建练习题目

import torch
import time

print("=== 练习1：环境检查 ===\n")

# 检查PyTorch版本
print(f"PyTorch版本：{torch.__version__}")

# 检查CUDA可用性
print(f"CUDA可用：{torch.cuda.is_available()}")

# 如果有GPU，显示GPU信息
if torch.cuda.is_available():
    print(f"GPU数量：{torch.cuda.device_count()}")
    for i in range(torch.cuda.device_count()):
        print(f"GPU {i}：{torch.cuda.get_device_name(i)}")
else:
    print("未检测到GPU，将使用CPU进行计算")

print("\n" + "="*50 + "\n")

print("=== 练习2：张量创建练习 ===\n")

# 创建不同类型的张量
tensor_int = torch.tensor([1, 2, 3])
tensor_float = torch.tensor([1.0, 2.0, 3.0])
tensor_zeros = torch.zeros(3, 3)
tensor_ones = torch.ones(2, 4)
tensor_random = torch.randn(2, 3)

print("整数张量：", tensor_int)
print("浮点张量：", tensor_float)
print("零张量：\n", tensor_zeros)
print("一张量：\n", tensor_ones)
print("随机张量：\n", tensor_random)

# 显示张量属性
print(f"\n整数张量类型：{tensor_int.dtype}")
print(f"浮点张量形状：{tensor_float.shape}")
print(f"零张量维度：{tensor_zeros.dim()}")

print("\n" + "="*50 + "\n")

print("=== 练习3：简单计算 ===\n")

# 创建两个矩阵
A = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)
B = torch.tensor([[5, 6], [7, 8]], dtype=torch.float32)

# 矩阵运算
print("矩阵A：\n", A)
print("矩阵B：\n", B)
print("A + B：\n", A + B)
print("A * B (元素乘)：\n", A * B)
print("A @ B (矩阵乘)：\n", A @ B)

# 其他运算
print("A的转置：\n", A.T)
print("A的逆矩阵：\n", torch.inverse(A))
print("A的行列式：", torch.det(A))

print("\n" + "="*50 + "\n")

print("=== 练习4：GPU加速测试 ===\n")

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
    
    # 检查结果是否一致
    print(f"结果一致性检查：{torch.allclose(z_cpu, z_gpu.cpu())}")
else:
    print("GPU不可用，无法进行GPU加速测试")

print("\n" + "="*50 + "\n")

print("=== 挑战任务：矩阵操作演示 ===\n")

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
    try:
        U, S, V = torch.svd(matrix)
        print(f"\n奇异值：{S}")
    except:
        # 如果svd不可用，使用其他方法
        eigenvalues = torch.linalg.eigvals(matrix @ matrix.T)
        singular_values = torch.sqrt(torch.abs(eigenvalues))
        print(f"\n奇异值（通过特征值计算）：{singular_values.real}")
    
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

print("\n" + "="*50)
print("🎉 所有练习完成！")
print("你已经成功完成了PyTorch环境搭建和基础操作练习。")
print("接下来可以继续学习张量的更多高级操作。")
