# 定义一个函数   文件未提交的话是橘色，提交之后是黑色，修改之后是蓝色
def  comm():
    a = 1
    b = 2
    c = a + b
    return c

if __name__ == '__main__':
    rs = comm()
    print(rs)

