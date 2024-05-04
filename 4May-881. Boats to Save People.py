from typing import List
'''
Example 1:

Input: people = [1,2], limit = 3
Output: 1
Explanation: 1 boat (1, 2)
Example 2:

Input: people = [3,2,2,1], limit = 3
Output: 3
Explanation: 3 boats (1, 2), (2) and (3)
Example 3:

Input: people = [3,5,3,4], limit = 5
Output: 4
Explanation: 4 boats (3), (3), (4), (5)

'''

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()  

        numBoats = 0
        left, right = 0, len(people) - 1

        while left <= right:
            if left == right:  
                numBoats += 1
                break

            if people[left] + people[right] <= limit:  
                left += 1  
                right -= 1
            else: 
                right -= 1  

            numBoats += 1  

        return numBoats
    
print(Solution().numRescueBoats([5,1,4,2],6))  
