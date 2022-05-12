#COPY THIS CLASS!
class fcolors:
    end = '\033[0m'
    black = '\033[0;30m'
    red = '\033[0;31m'
    green = '\033[0;32m'
    yellow = '\033[0;33m'
    blue = '\033[0;34m'
    pink = '\033[0;35m'
    teal = '\033[0;36m'
    white = '\033[0;37m'
    class bold:
        grey = '\033[30;1m'
        orange = '\033[31;1m'
        green = '\033[32;1m'
        yellow = '\033[33;1m'
        blue = '\033[34;1m'
        pink = '\033[35;1m'
        teal = '\033[36;1m'
        white = '\033[37;1m'

#an example, run it to see
print(f"{fcolors.red}Hello World!{fcolors.end}")
