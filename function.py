def calc(a, b, ch):
    if ch == '+':
        return a + b
    elif ch == '-':
        return a - b
    elif ch == '/':
        return round(a / b)
    elif ch == '*':
        return a * b


def mult_div(user_created_list):
    i = 0
    while i <= len(user_created_list)-1:
        if user_created_list[i] == '*' or user_created_list[i] == '/':
            result = calc(int(
                user_created_list[i - 1]), int(user_created_list[i + 1]), user_created_list[i])
            user_created_list.insert(i-1, result)
            del user_created_list[i:i + 3]
            i -= 2
        i += 1


def add_sub(modilied_list):
    j = 1
    while j <= len(modilied_list)-1:
        result = calc(int(modilied_list[j - 1]),
                      int(modilied_list[j + 1]), modilied_list[j])
        modilied_list.insert(j-1, result)
        del modilied_list[j:j + 3]
        if j == len(modilied_list)-1:
            break