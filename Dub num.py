num_srt = input("type a:")
num_srt = num_srt + " " 
num = ""
nums_int=[]
for s in num_srt:
    if s != " ":
        num = num + s
    if s == " ":
        if num != "":
            a = int(num)
            nums_int.append(a)
        num = ""


def remove_duplicate(items):
    unique = []
    for item in items:
        if item not in unique:
            unique.append(item)
    return unique

print(remove_duplicate(nums_int))
