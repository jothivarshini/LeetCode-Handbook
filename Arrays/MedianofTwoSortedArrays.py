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