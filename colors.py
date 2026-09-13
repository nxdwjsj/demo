# ANSI 颜色码
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"


def color_text(text, color):
    """给文字加颜色（新功能：彩色输出）"""
    return f"{color}{text}{RESET}"
