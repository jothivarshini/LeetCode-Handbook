""" Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106"""

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)
        ef = 0
        of = 0

        if (n1+n2) % 2 == 0:
            ef   = 1
            x, y = (n1+n2)//2 , ((n1+n2)//2) + 1 
        else:
            of = 1
            z  = ( (n1+n2)//2 ) + 1

        res = []

        i = 0
        j = 0
        k = 0
        while(i<n1 and j<n2):
            if nums1[i]<nums2[j]:
                res.append(nums1[i])
                i+=1
            else:
                res.append(nums2[j])
                j+=1
            k+=1
            if k == ((n1+n2)//2) + 1 :
                break
        while(i<n1):
            res.append(nums1[i])
            i+=1
            k+=1
            if k == ((n1+n2)//2) + 1 :
                break
        while(j<n2):
            res.append(nums2[j])
            j+=1
            k+=1
            if k == ((n1+n2)//2) + 1 :
                break          
        if ef == 1:
            return  (res[x-1] + res[y-1])/2 
        return res[z-1]