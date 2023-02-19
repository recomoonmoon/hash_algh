from collections import defaultdict
def merge(nums1, nums2):
    h1 = defaultdict(int)
    h2 = defaultdict(int)
    for i in nums1:
        h1[i] += 1
    for i in nums2:
        h2[i] += 1
    ans = []
    for i in set(nums2):
        ans+=[i]*min(h1[i], h2[i])
    return ans

print(merge(nums1=[4,9,5], nums2=[9,4,9,8,4]))