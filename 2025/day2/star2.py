sm = 0

with open("2025/day2/input.txt") as f:
    line = f.read()
    line = line.split(",")
    for id_range in line:
        first_id, second_id = id_range.split("-")
        for id in range(int(first_id), int(second_id)+1):
            factors = []
            num_str = str(id)
            num_length = len(num_str)

            for possible_divisor in range(1, int(num_length**0.5)+1): 
                if num_length%possible_divisor==0:
                    factors.append(possible_divisor)
                    if possible_divisor*possible_divisor!=num_length:
                        factors.append(num_length//possible_divisor)

            factors.sort(reverse=True)
            factors = factors[1:]
            for factor in factors:
                sequence = num_str[0:factor]
                if sequence* (len(num_str)//len(sequence)) == num_str:
                    sm+=id
                    break
print(sm)