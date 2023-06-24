def convert(dec):
    if dec > 1:
        convert(dec // 2)
    print(dec % 2, end="")

convert(9)