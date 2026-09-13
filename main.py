# 这是一个简单的 Python 演示程序


def greet(name):
    """返回问候语"""
    return f"你好, {name}! 欢迎使用 Git!"


def farewell(name):
    """新增的告别函数"""
    return f"再见, {name}, 期待下次见面!"


if __name__ == "__main__":
    print(greet("Git 学习者"))
    print(farewell("Git 学习者"))
