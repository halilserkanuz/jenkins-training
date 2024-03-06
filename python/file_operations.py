# with open("annual_values.csv", "r") as file:
#     data = file.read()
#     data = data.split("\n")
# print(len(data))

with open("annual_values.csv", "r") as file:
    data = file.readlines()

# for line in data:
#     values = line.split(",")
#     value = line[-2]
#     year = line[0]

# sum_up = sum([int(line.split(",")[-2]) for line in data[1:] if line.split(",")[-2]])

print([line.split(",")[-2] for line in data[1:] if line.split(",")[-2]])

# data = [
#     [5,100],
#     [10,100]
# ]


# sum_up = [line[-2] for line in data if line[-2] > 5  ]
# print(sum_up)


# # a, w, r, x, t, b, +, U, r+, w+, a+, rb, wb, ab, rb+, wb+, ab+


