def pe0001(upto):
    total = 0
    for i in range(upto):
        if i % 3 == 0 or i % 5 == 0:
            total += i
    return total

print(pe0001(1000))