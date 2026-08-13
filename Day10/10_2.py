import pandas as pd
df = pd.read_csv("student.csv")
print(df)

# 查看某列
print(df["姓名"])

# 计算平均分
print(df["成绩"].mean())

# 查看前几行数据。
# 默认查看前5行：
df.head()
# 查看前3行：
df.head(3)

# 查看最后几行数据。
# 默认查看最后5行：
df.tail()
# 查看最后3行：
df.tail(3)

# 获取所有列名。
print(df.columns)

# 查看数据统计信息。
df.describe()

# 删除空值：
df.dropna()

# 删除重复：
df.drop_duplicates()

# 按标签（名称）取数据。
# df.loc[0]
# 获取索引为0的行。
# df.loc[:, "姓名"]
# 获取姓名列。
df.loc[0, "姓名"]
# 表示：
# 第0行
# 姓名列

# 按位置（数字）取数据。
# df.iloc[0]
# 获取第一行。
# df.iloc[:, 0]
# 获取第一列。
df.iloc[0, 0]
# 表示：
# 第1行
# 第1列
