from typing import List

def rates(report: List[int], num_bits) -> int:
    num_lines, gamma_bits, epsilon_bits = len(report), ['0b'], ['0b']
    for k in range(num_bits - 1, -1, -1):
        # obtain # of set bits
        bits_set = sum([1 if line & (1 << k) != 0 else 0 for line in report])
        if bits_set > num_lines // 2:
            gamma_bits.append(str(1))
            epsilon_bits.append(str(0))
        else:
            gamma_bits.append(str(0))
            epsilon_bits.append(str(1))
    gamma, epsilon = int(''.join(gamma_bits), 2), int(''.join(epsilon_bits), 2)
    return gamma * epsilon
