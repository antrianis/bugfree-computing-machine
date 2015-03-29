def solution(number):
    A = (number - 1) // 3
    B = (number - 1) // 5
    C = (number - 1) // 15    
    return [A - C, B - C, C]
