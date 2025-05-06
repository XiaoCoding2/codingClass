
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n=len(nums)
        tris=[]
        for x in range(n):
            for y in range(x+1,n):
                for z in range(y+1,n):
                    tri=[]
                    tri.append(nums[x])
                    tri.append(nums[y])
                    tri.append(nums[z])
                    tri.sort()
                    if sum(tri)==0 and tri not in tris:
                        tris.append(tri)
        return tris