def DeltaEncoding(int_arr):
    length = len(int_arr)
    for i in reversed(range(length)):
        if i > 0:
            int_arr[i] -= int_arr[i-1]
    