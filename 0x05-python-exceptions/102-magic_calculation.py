#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('out of range')
            else:
                result += (a ** b) / i
        except Exception:
            result = b + a
            break
    return (result)
