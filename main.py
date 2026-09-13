# 这是一个简单的 Python 演示程序


def greet(name):
    """返回问候语"""
    return f"你好, {name}! 欢迎使用 Git! 今天也要加油!"  # 这行是新改的，去左侧栏看看它被标记了


def farewell(name):
    """新增的告别函数"""
    return f"再见, {name}, 期待下次见面!"


if __name__ == "__main__":
    from colors import color_text, GREEN, YELLOW
    print(color_text(greet("Git 学习者"), GREEN))
    print(color_text(farewell("Git 学习者"), YELLOW))
