# 练习题目和答案

print("=== 练习1：变量创建 ===\n")
# 创建变量存储个人信息
name = "李明"
age = 22
height = 180.5
hobby = "编程"

# 输出信息
print(f"姓名：{name}")
print(f"年龄：{age}")
print(f"身高：{height}cm")
print(f"爱好：{hobby}")
print()

print("=== 练习2：类型转换练习 ===\n")
# 字符串转整数
str_age = "22"
age_int = int(str_age)
print(f"年龄：{age_int}，类型：{type(age_int)}")

# 整数转字符串
score = 95
score_str = str(score)
print(f"分数：'{score_str}'，类型：{type(score_str)}")

# 浮点数转整数
price = 19.99
price_int = int(price)
print(f"价格：{price_int}元，类型：{type(price_int)}")
print()

print("=== 练习3：计算BMI ===\n")
# 输入数据
weight = 65.5  # 体重（kg）
height = 1.75  # 身高（m）

# 计算BMI
bmi = weight / (height ** 2)

# 输出结果
print(f"体重：{weight}kg")
print(f"身高：{height}m")
print(f"BMI指数：{bmi:.2f}")
print()

print("=== 练习4：学生信息管理 ===\n")
# 学生信息
student_name = "王五"
student_id = "2023001"
chinese_score = "85"
math_score = "92"
english_score = "78"

# 转换分数为数字
chinese_score_num = int(chinese_score)
math_score_num = int(math_score)
english_score_num = int(english_score)

# 计算总分和平均分
total_score = chinese_score_num + math_score_num + english_score_num
average_score = total_score / 3

# 输出结果
print(f"学生姓名：{student_name}")
print(f"学号：{student_id}")
print(f"总分：{total_score}")
print(f"平均分：{average_score:.1f}")
print()

print("=== 挑战任务：个人信息调查程序 ===\n")
# 个人信息调查程序
print("=== 个人信息调查 ===")

# 创建变量存储信息
name = "张小明"
age = 25
height = 1.78
weight = 70.0
occupation = "软件工程师"

# 计算BMI
bmi = weight / (height ** 2)

# 输出结果
print(f"\n=== 调查结果 ===")
print(f"姓名：{name}")
print(f"年龄：{age}岁")
print(f"身高：{height}m")
print(f"体重：{weight}kg")
print(f"职业：{occupation}")
print(f"BMI指数：{bmi:.1f}")

# BMI健康提示
if bmi < 18.5:
    print("健康提示：体重偏轻，建议适当增加营养")
elif bmi < 24:
    print("健康提示：体重正常，请继续保持")
else:
    print("健康提示：体重偏重，建议适当运动")
