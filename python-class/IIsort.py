

def sortnums(nums_,namebool):
    if namebool==True:nums=list(nums_.keys())
    else:nums=list(nums_.values())
    for i in range(1, len(nums)):
        curVal = nums[i]
        prev = i - 1
        while prev>=0 and nums[prev]>curVal:
            nums[prev+1]=nums[prev]
            prev-=1
        nums[prev+1]=curVal
        # Place curVal in its correct position
        nums[prev+1] = curVal
    return nums

if __name__=='__main__':
    while True:
        try:
            times=int(input("num of items? "))
            nums={}
            for x in range(times):
                name,score=input("name score: ").split()
                nums[name]=int(score)
            print(nums)
            while True:
                whatToSort=input("Sort by name or score? ").lower()
                if whatToSort=="name":
                    sortnums(nums, True)
                    break
                elif whatToSort=="score":
                    sortnums(nums, False)
                    break
                else:
                    print("Pls be valid")
            break
        except ValueError:
            print("Please Enter valid number.")
    print(nums)
