class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 += '.'
        version2 += '.'
        
        version1_list = list(map(int, filter(None, version1.split('.'))))
        version2_list = list(map(int, filter(None, version2.split('.'))))
        
        maxLength = max(len(version1_list), len(version2_list))

        version1_list += [0] * (maxLength - len(version1_list))
        version2_list += [0] * (maxLength - len(version2_list))

        for num in range(maxLength):
            if version1_list[num] < version2_list[num]:
                return -1
            elif version1_list[num] > version2_list[num]:
                return 1

        return 0

print(Solution().compareVersion("1.0.1", '1'))  # Output: 1


                
        
# print(Solution().compareVersion("1.0.1",'1'))