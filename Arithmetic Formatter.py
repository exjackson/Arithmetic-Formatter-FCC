def arithemetic_formatter(problems,statprint=False):
    first = ""
    second = ""
    sumx = ""
    lines = ""
    if len(problems) >= 6:
        return "Error: Too many problems."
    for x in problems:
        a = x.split()
        firsts = a[0]
        seconds = a[2]
        operands = a[1]
        if (len(firsts) > 4 or len(seconds) > 4):
            return "Error: Numbers cannot be more than four digits."
        if not firsts.isnumeric() or not seconds.isnumeric():
            return "Error: Numbers must only contain digits."
        if (operands == '+' or operands == '-'):
            if operands == "+":
                sums = str(int(firsts) + int(seconds))
            else:
                sums = str(int(firsts) - int(seconds))
            length = max(len(firsts), len(seconds)) + 2
            top = str(firsts).rjust(length)
            bottom = operands + str(seconds).rjust(length - 1)
            line = ''
            res = str(sums).rjust(length)
            for s in range(length):
                line += '-'
            first += top + '    '
            second += bottom + '    '
            lines += line + '    '
            sumx += res + '    '
        else:
            return "Error: Operator must be '+' or '-'."
    first.rstrip()
    second.rstrip()
    lines.rstrip()
    if statprint:
        sumx.rstrip()
        arranged_problems = first + '\n' + second + '\n' + lines + '\n' + sumx
    else:
        arranged_problems = first + '\n' + second + '\n' + lines
    return arranged_problems


              
print(arithemetic_formatter(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"],True))