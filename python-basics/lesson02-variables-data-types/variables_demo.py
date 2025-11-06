# 变量与数据类型演示程序

print("=== Python变量与数据类型演示 ===\n")

# 1. 基本数据类型示例
print("1. 基本数据类型:")
name = "张三"          # 字符串类型
age = 20              # 整数类型
height = 175.5        # 浮点数类型
is_student = True     # 布尔类型

print(f"姓名：{name} (类型：{type(name)})")
print(f"年龄：{age} (类型：{type(age)})")
print(f"身高：{height} (类型：{type(height)})")
print(f"是学生：{is_student} (类型：{type(is_student)})")
print()

# 2. 类型转换示例
print("2. 类型转换示例:")
str_num = "100"
num_int = int(str_num)
num_float = float(str_num)
num_str = str(age)

print(f"字符串'{str_num}'转整数：{num_int}")
print(f"字符串'{str_num}'转浮点数：{num_float}")
print(f"整数{age}转字符串：'{num_str}'")
print()

# 3. 布尔值转换规则
print("3. 布尔值转换规则:")
print(f"bool(0) = {bool(0)}")
print(f"bool(1) = {bool(1)}")
print(f"bool(-1) = {bool(-1)}")
print(f"bool('') = {bool('')}")
print(f"bool('hello') = {bool('hello')}")
print(f"bool([]) = {bool([])}")
print(f"bool([1, 2, 3]) = {bool([1, 2, 3])}")
print()

# 4. 变量重新赋值
print("4. 变量重新赋值:")
x = 10
print(f"x = {x}, 类型：{type(x)}")

x = "Hello"
print(f"x = '{x}', 类型：{type(x)}")

x = 3.14
print(f"x = {x}, 类型：{type(x)}")
print()

# 5. 多变量赋值
print("5. 多变量赋值:")
a, b, c = 1, 2, 3
print(f"a = {a}, b = {b}, c = {c}")

# 交换变量
a, b = b, a
print(f"交换后：a = {a}, b = {b}")
print()

# 6. 常量命名约定
print("6. 常量命名约定:")
PI = 3.14159
MAX_SCORE = 100
MIN_AGE = 18

print(f"圆周率：{PI}")
print(f"最高分：{MAX_SCORE}")
print(f"最小年龄：{MIN_AGE}")
print()

print("=== 演示结束 ===")
