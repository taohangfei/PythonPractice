# Definition for a point
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    def getRatio(self,a,b):
        if a[0]!= b[0]:
            return float(a[1] - b[1])/float(a[0] - b[0])
        else:
            return "*"
    def getLength(self,l,occur):
        result = 0
        for i in l:
            result+=occur[i]
        return result
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        if len(points)<=2:
            return len(points)
        ratio_dict = {}
        max = 0
        from collections import Counter
        occurances = Counter(points)
        points = list(set(points))
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                ratio = self.getRatio(points[i],points[j])
                if ratio not in ratio_dict:
                    ratio_dict[ratio] = {}
                    ratio_dict[ratio][points[i]] = set([points[i],points[j]])
                    length =self.getLength(ratio_dict[ratio][points[i]],occurances)
                    if length > max:
                        max = length
                else:
                    isIn = False
                    for key in ratio_dict[ratio]:
                        if self.getRatio(key,points[i]) == ratio:
                            ratio_dict[ratio][key].add(points[i])
                            ratio_dict[ratio][key].add(points[j])
                            length =self.getLength(ratio_dict[ratio][key],occurances)
                            if length > max:
                                max = length
                            isIn = True
                            break
                    if not isIn:
                        ratio_dict[ratio][points[i]] = set([points[i],points[j]])
                        length =self.getLength(ratio_dict[ratio][points[i]],occurances)
                        if length > max:
                            max = length
        return max

a = Solution()
print a.maxPoints([(0,0),(1,1),(0,0)])