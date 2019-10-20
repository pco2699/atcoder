def c():
    li = list(input())
    syms = ['+', '-']
    calc = li[0]
    for i in range(2):
        i_calc = calc
        calc += syms[i] + li[1]
        for j in range(2):
            j_calc = calc
            calc += syms[j] + li[2]
            for k in range(2):
                k_calc = calc
                calc += syms[k] + li[3]
                res = eval(calc)
                if res == 7:
                    print(calc+"=7")
                    return
                calc = k_calc
            calc = j_calc
        calc = i_calc


if __name__ == '__main__':
    c()
