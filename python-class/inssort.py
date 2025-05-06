
def insertion_sort(lst):
    # Iterate from the second element to the end
    for i in range(1, len(lst)):
        curVal = lst[i]
        prev = i - 1
        # Shift elements of A[0..i-1] that are greater than curVal
        # one position to the right
        while prev>=0 and lst[prev]>curVal:
            print(lst)
            lst[prev],curVal=curVal,lst[prev]
            prev-=1
        # Place curVal in its correct position
        lst[prev+1] = curVal
    return lst

# Example usage:
if __name__ == "__main__":
    arr = [7, 3, 5, 2, 9, 1]
    sorted_arr = insertion_sort(arr)
    print("Sorted array:", sorted_arr)