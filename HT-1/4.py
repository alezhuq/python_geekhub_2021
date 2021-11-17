# 4. Write a script to concatenate N strings.

N = int(input("how many strings u wanna concatenate? : "))

out_str = ""

for i in range(N):
    input_str = str(input("input {} string : ".format(i+1)))
    out_str += input_str

print(out_str)
