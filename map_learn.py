
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]
numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]
summed = list(map(lambda x, y: x + y, numbers1, numbers2))
print(summed)  # Output: [5, 7, 9]


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        triangle = []
        # Step 1: Handle the case where no rows are needed
        if numRows == 0:
            return triangle
        
        # Step 2: Start with the first row
        triangle.append([1])  # First row is always [1]
        
        # Step 3: Iterate over the number of rows to generate each row
        for row_num in range(1, numRows):
            # Start the row with 1
            row = [row_num]
            # You will fill in more in the next steps
            triangle.append(row)
        
        return triangle
def main():
    numRows = 5  # You can change this to test with different inputs
    solution = Solution()
    result = solution.generate(numRows)
    print(result)

if __name__ == "__main__":
    main()