#973. K Closest Points to Origin
class Solution(object):
    def kClosest(self, points, k):
        def compare(pt):
            x, y = pt[0], pt[1]
            return x ** 2 + y ** 2 
        points = sorted(points, key=compare)
        return points[:k]
        
