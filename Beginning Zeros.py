def beginning_zeros(number: str) -> int:
    answer = 0
    for i in number:
        if int(i) == 0:
            answer += 1
        else:
            break

    return answer



beginning_zeros('100') #== 0
beginning_zeros('001') #== 2
beginning_zeros('100100') #== 0
beginning_zeros('001001') #== 2
beginning_zeros('012345679') #== 1
beginning_zeros('0000') #== 4
