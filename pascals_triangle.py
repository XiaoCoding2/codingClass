

class Solution(object):
    def generate(self, numRows):#{
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        triangle = [[1]]
        triangle2=[[1],[1,1],[1,2,1],[1,3,3,1]]
        # Step 1: Handle the case where no rows are needed
        if numRows == 0:#{
            return triangle
        #}
        #
        for row_num in range(0, numRows):
            # Start the row with 1
            pairs=triangle[row_num]
            row = []
            triangle.append(row)
        return triangle
#   }
def main_():
    numRows = 4  # You can change this to test with different inputs
    solution = Solution()
    result = solution.generate(numRows)
    print(result)

if __name__ == "__main__":
    main_()

