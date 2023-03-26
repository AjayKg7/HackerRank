def lsq(N, limit, A):
    count = 0
    sum = 0
    for i in range(N):
        for j in range(N - i - 1):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
    print(A)
    for k in A:
        sum += k
        count += 1
        if sum >= limit:
            return count - 1

    return count

# class Btree:
#     def __init__(self,data):
#         self.data = data
#         self.left = None
#         self.right = None

#     def add_node(self,data):
#         if self.data == data:
#             return
#         if data < self.data:
#             if self.left :
#                 self.left.add_node(data)

#             else:
#                 self.left = Btree(data)

#         if data > self.data:
#             if self.right :
#                 self.right.add_node(data)

#             else:
#                 self.right = Btree(data)

#     def minv(self):
#         if self.data == None:
#             return "Invalid vals provided"

#         if self.left:
#             return self.left.minv()

#         else:
#             return self.data

#     def delete(self,val):
#         if not self.data:
#             return
#         # Find the node in the left subtree	if key value is less than root value
#         if val < self.data:
#             if self.left:
#                 self.left = self.left.delete(val)
#         # Find the node in right subtree if key value is greater than root value,
#         elif val > self.data:
#             if self.right:
#                 self.right = self.right.delete(val)
#         # Delete the node if self.data == key
#         else:
#             if self.right is None and self.left is None:
#                 return None

#             # If there is no right children delete the node and new root would be self.left
#             if self.right is None:
#                 return self.left

#             # If there is no left children delete the node and new root would be self.right
#             if self.left is None:
#                 return self.right

#             # If both left and right children exist in the node replace its value with
#             # the minmimum value in the right subtree. Now delete that minimum node
#             # in the right subtree
#             min_val = self.right.minv()
#             self.data = min_val
#             self.right = self.right.delete(min_val)

#         return self

t = int(input())  # Reading input from STDIN
for testcase in range(t):
    n, q = map(int, input().split())
    A = list(map(int, input().split()))
    # Bt = Btree(A[0])
    # for i in A[1:]:
    #     Bt.add_node(i)

    for query in range(q):
        limit = int(input())
        res = lsq(n, limit, A)
        print(res)
    #     accesslmt = 0
    #     counted = 0
    #     for val in range(q):
    #         mvl = Bt.minv()
    #         x=accesslmt+mvl
    #         if x < limit:
    #             accesslmt+=mvl
    #             Bt.delete(mvl)
    #             counted+=1
    #         else:
    #             break
    #     print(counted)

# print('Hi, %s.' % name)         # Writing output to STDOUT