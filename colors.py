from colorama import Fore, Style

reset = Style.RESET_ALL
question_color = '\033[37;7m'
ng = Style.BRIGHT

green = ng + Fore.GREEN
purple = ng + Fore.MAGENTA


def coloric_text(message, color, to_print=bool()):
    text = color + message + reset
    
    return text if not to_print else print(text)

if __name__ == '__main__':
    coloric_text('Hello, World!', question_color, True)
