n = int(input("Enter the value of n : "))

size = n + (n - 1)
center = n - 1

temp = []
answer = []
for i in range(size):
    temp.append("T")


for i in range(size):
    answer.append(temp[:])


for digit in range(1, n + 1):
    expansion = digit + (digit - 1)
    position = [center - digit + 1, center - digit + 1]

    for i in range(expansion):
        answer[position[0]][position[1] + i] = str(digit)

    for i in range(expansion):
        answer[position[0] + i] [position[1]] = str(digit)

    position = [center + digit - 1, center + digit - 1]

    for i in range(expansion):
        answer[position[0]] [position[1] - i] = str(digit)

    for i in range(expansion):
        answer[position[0] - i] [position[1]] = str(digit)


for arr in answer:
    print(" ".join(arr))