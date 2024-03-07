def multiply(**kwargs):
    result = 1
    for key, value in kwargs.items():
        result *= value
    return result

print(multiply(x=1, y=2, z=3, t= 6))