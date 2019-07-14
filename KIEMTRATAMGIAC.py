# copy from Bùi Tống Minh Châu

# yêu cầu user nhập giá trị a
a = int(input("Hãy nhập giá trị a: "))

# yêu cầu user nhập giá trị b
b = int(input("Hãy nhập giá trị b: "))

# yêu cầu user nhập giá trị c
c = int(input("Hãy nhập giá trị c: "))

answer = not bool((a**2+b**2-c**2) * (a**2+c**2-b**2) * (c**2+b**2-a**2))

print('Tam giác trên có phải là tam giác vuông không? ', answer)
