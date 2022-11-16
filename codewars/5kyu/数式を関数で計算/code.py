import sys

# 引数がない場合のデフォルトを設定。
# 引数の値がデフォルトであればそのまま返し、そうでなければ計算結果を返す
def zero(arg1='0'): #your code here
    return arg1 if arg1 == "0" else int(eval("0" + arg1))

def one(arg1='1'): #your code here
    return arg1 if arg1 == "1" else int(eval("1" + arg1))

def two(arg1='2'): #your code here
    return arg1 if arg1 == "2" else int(eval("2" + arg1))

def three(arg1='3'): #your code here
    return arg1 if arg1 == "3" else int(eval("3" + arg1))

def four(arg1='4'): #your code here
    return arg1 if arg1 == "4" else int(eval("4" + arg1))

def five(arg1='5'): #your code here
    return arg1 if arg1 == "5" else int(eval("5" + arg1))

def six(arg1='6'): #your code here
    return arg1 if arg1 == "6" else int(eval("6" + arg1))

def seven(arg1='7'): #your code here
    return arg1 if arg1 == "7" else int(eval("7" + arg1))

def eight(arg1='8'): #your code here
    return arg1 if arg1 == "8" else int(eval("8" + arg1))

def nine(arg1='9'): #your code here
    return arg1 if arg1 == "9" else int(eval("9" + arg1))


# 計算関数
def plus(num): #your code here
    return "+ {}".format(num)
def minus(num): #your code here
    return "- {}".format(num)
def times(num): #your code here
    return "* {}".format(num)
def divided_by(num): #your code here
    return "/ {}".format(num)