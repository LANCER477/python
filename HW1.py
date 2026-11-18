user_input = input(" Ввести границы диапазона: ").split()

if len(user_input) >= 2:
    start, end = int(user_input[0]), int(user_input[1])
else:
    start = int(user_input[0])
    end = int(input("Ввести конец: "))

step = 1 if start <= end else -1

print(*range(start, end + step, step))
