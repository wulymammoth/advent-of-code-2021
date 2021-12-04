from typing import List

def rates(report: List[int], num_bits) -> int:
    num_lines, gamma_bits, epsilon_bits = len(report), ['0b'], ['0b']
    for k in range(num_bits - 1, -1, -1): # test the k-th bit for each line
        one_bits = 0
        for line in report:
            if line & (1 << k) != 0: # test if k-th bit is set
                one_bits += 1
        if one_bits > num_lines // 2:
            gamma_bits.append(str(1))
            epsilon_bits.append(str(0))
        else:
            gamma_bits.append(str(0))
            epsilon_bits.append(str(1))
    gamma, epsilon = int(''.join(gamma_bits), 2), int(''.join(epsilon_bits), 2)
    return gamma * epsilon
