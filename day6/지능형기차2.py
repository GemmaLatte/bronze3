passenger = 0
result_passenger = []

for _ in range(10):
    out_passenger, in_passenger = list(map(int, input()))

    passenger += in_passenger - out_passenger

    result_passenger.append(passenger)

result_passenger.sort()

print(result_passenger[-1])