n = int(input())
numbers = list(map(str, input().split()))
numbers.sort(reverse=True)
ans = []
ans.append(''.join(numbers[:]))
ans.append(''.join(numbers[::-1]))
print(*ans)