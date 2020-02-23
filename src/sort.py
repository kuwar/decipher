def order_fct(n):
    """
    Sort the given array of integer in ascending order
    """
    swapped = True

    while swapped:
        swapped = False
        
        for i in range(len(n) - 1):
            
            if n[i] > n[i + 1]:
                tmp = n[i]
                n[i] = n[i + 1]
                n[i + 1] = tmp
                
                swapped = True
    return n


if __name__ == "__main__":
    print("__main__")

    print(order_fct([1, 5, 2, 9, 6]))

    print(order_fct([1, 5, 2, 9, 6]))

    print(order_fct([8, 10, 1, 2, 5, 6, 9]))

    print("---End---")
