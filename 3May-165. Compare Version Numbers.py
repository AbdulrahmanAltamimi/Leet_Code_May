# class Solution:
#     def compareVersion(self, version1: str, version2: str) -> int:
#             # 2.5.33 and 0.1 
#             version1 = version1+'.'
#             # print(version1)
#             version2 +='.'
#             # print (version2)
#             version1_dot= 0
#             version2_dot= 0
#             version1_list = []
#             version2_list = []

#             for chr in range(len(version1)):
#                 if version1 [chr] == "." :
#                    version1_list.append(int(version1[version1_dot:chr]))
#                    version1_dot= chr+1
#             for chr in range(len(version2)):
#                 if version2 [chr] == "." :
                   
#                    version2_list.append(int(version2[version2_dot:chr]))
#                    version2_dot= chr+1
           
           
           
           
#             maxLenth = 0

#             if len(version1_list)> len(version2_list):
#                 maxLenth = len(version2_list)
#             else:
#                 maxLenth = len(version2_list)

#             for i in range(maxLenth+1):

#                 if len(version2_list) > len(version1_list):
#                     version1_list.append(0)
#                 elif len(version2_list) < len(version1_list):
#                     version2_list.append(0)

#             print(version1_list)
#             print(version2_list)


#             for num in range (maxLenth):
#                 if version1_list[num] < version2_list[num]:
#                     return -1
#                 elif version1_list[num] > version2_list [num]:
#                     return 1
#             return 0

            

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