def generate_sum_combinations(numbers, max_consecutive):
    def recursive_sum_combinations(current_sum, index, consecutive_count):
        if index == len(numbers):
            result.append(current_sum)
            return

        if consecutive_count < max_consecutive:
            # Include the current number in the sum
            recursive_sum_combinations(current_sum + numbers[index], index + 1, consecutive_count + 1)

        # Skip the current number in the sum
        recursive_sum_combinations(current_sum, index + 1, 0)

    result = []
    recursive_sum_combinations(0, 0, 0)
    return result

n=str(input(""))
j= n.split(" ")
num=int(j[0])
like=int(j[1])
numbers=[]
i=0
# numbers = [1, 2, 3, 4, 5]
while i<num:
    des=int(input(""))
    numbers.append(des)
    i+=1
result = generate_sum_combinations(numbers,like)

print(max(result))
