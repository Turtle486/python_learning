a = []
b = input()
while b != "ok":
    try:
        bb = int(b)
        if bb in a:
            pass
        elif bb not in a:
            a.append(bb)
    except ValueError:
        print("输入数字或\"ok!\"")
    b = input()
else:
    print(sorted(a))