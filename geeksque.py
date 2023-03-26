from typing import List

class Solution:

    def is_prime(self,n):
        if n == 1:
            return False
        for i in range(2, n):
            if (n % i) == 0:
                return False
        return True

    def findbot(self, username:List[str],n : int) -> List[int]:
        values = []
        out = []
        for i in username:
            avail = []
            count = 0
            for j in range(0,len(i),2):
                if i[j] not in avail:
                    avail.append(i[j])
                    count+=1
            values.append(count)
            print(count)
        for val in values:
            if self.is_prime(val):
                out.append(1)
            else:
                out.append(0)
        return out

x = Solution()
ret = x.findbot(["foo","bab"],2)
print(ret)
