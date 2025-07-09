if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    mx = max(arr)
    sc = None  # runner-up score

    for num in arr:
        if num == mx:
            continue
        elif sc is None:
            sc = num
        elif num > sc:
            sc = num

    print(sc)