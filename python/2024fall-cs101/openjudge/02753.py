n = int(input())
numbers = [0 for i in range(21)]
numbers[1] =1
numbers[2] =1
for j in range(3,21):
    numbers[j] = numbers[j-1] + numbers[j-2]
for i in range(n):
    m = int(input())
    print(numbers[m])