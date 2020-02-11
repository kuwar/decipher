def order_fct(n):
    i = 0
    while i < len(n):
        j = 0
        while j < len(n):
            if n[i] > n[j]:
                tmp = n[i]
                n[i] = n[j]
                n[j] = tmp
            j += 1
        i += 1
    return n


if __name__ == "__main__":
    print("__main__")

    print(order_fct([1, 5, 2, 9, 6]))

    print("---End---")

    import sys
    print(sys.path)
