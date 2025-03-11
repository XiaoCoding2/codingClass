
class Solution:
    def generate(self, numRows: int):
        lst1=[[1]]
        lst2=[]
        # Step 1: Handle the case where no rows are needed
        if numRows == 1:
            print(lst1)
        # Step 2: Iterate over the number of rows to generate each row
        for x in range(numRows):
            lst2=[]
            p_r=lst1[-1]
            lst2.append(1)
            for idx in range(0,len(p_r)):
                if idx < len(p_r)-1:
                    lst2.append(p_r[idx]+p_r[idx+1])
            lst2.append(1)
            lst1.append(lst2)
        print(lst2)

sol=Solution()
sol.generate(3)