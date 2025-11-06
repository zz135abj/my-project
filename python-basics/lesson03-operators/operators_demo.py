# 第3课：运算符与表达式 - 示例代码

# 1. 算术运算符
print("=== 算术运算符 ===")
a = 10
b = 3

print(f"a + b = {a + b}")  # 加法: 13
print(f"a - b = {a - b}")  # 减法: 7
print(f"a * b = {a * b}")  # 乘法: 30
print(f"a / b = {a / b}")  # 除法: 3.3333...
print(f"a // b = {a // b}")  # 整除: 3
print(f"a % b = {a % b}")  # 取模: 1
print(f"a ** b = {a ** b}")  # 幂运算: 1000

# 2. 比较运算符
print("\n=== 比较运算符 ===")
x = 5
y = 10

print(f"x == y: {x == y}")  # False
print(f"x != y: {x != y}")  # True
print(f"x > y: {x > y}")  # False
print(f"x < y: {x < y}")  # True
print(f"x >= y: {x >= y}")  # False
print(f"x <= y: {x <= y}")  # True

# 3. 赋值运算符
print("\n=== 赋值运算符 ===")
num = 10
print(f"初始值: {num}")

num += 5  # num = num + 5
print(f"num += 5: {num}")

num -= 3  # num = num - 3
print(f"num -= 3: {num}")

num *= 2  # num = num * 2
print(f"num *= 2: {num}")

num //= 4  # num = num // 4
print(f"num //= 4: {num}")

# 4. 逻辑运算符
print("\n=== 逻辑运算符 ===")
age = 25
has_license = True

print(f"age >= 18 and has_license: {age >= 18 and has_license}")
print(f"age < 18 or has_license: {age < 18 or has_license}")
print(f"not has_license: {not has_license}")

# 5. 运算符优先级示例
print("\n=== 运算符优先级 ===")
result1 = 2 + 3 * 4  # 乘法优先
print(f"2 + 3 * 4 = {result1}")  # 14

result2 = (2 + 3) * 4  # 括号改变优先级
print(f"(2 + 3) * 4 = {result2}")  # 20

result3 = 10 > 5 and 3 < 7
print(f"10 > 5 and 3 < 7 = {result3}")  # True

# 6. 类型转换
print("\n=== 类型转换 ===")
str_num = "100"
int_num = int(str_num)
print(f"字符串转整数: {int_num}, 类型: {type(int_num)}")

float_num = 3.14
int_from_float = int(float_num)
print(f"浮点数转整数: {int_from_float}")

num = 42
str_from_int = str(num)
print(f"整数转字符串: '{str_from_int}', 类型: {type(str_from_int)}")

# 7. 实用示例：计算商品折扣
print("\n=== 实用示例：计算商品折扣 ===")
original_price = 100
discount_rate = 0.2  # 8折
final_price = original_price * (1 - discount_rate)
savings = original_price - final_price

print(f"原价: ¥{original_price}")
print(f"折扣: {discount_rate * 100}%")
print(f"最终价格: ¥{final_price}")
print(f"节省: ¥{savings}")
