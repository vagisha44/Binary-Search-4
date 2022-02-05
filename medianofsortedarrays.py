class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #perform binary search on smaller array  because there can be a case where we need to have whole elements onearray in left partition. if we choose larege array then it will throw index out of bound
        m=len(nums1)
        n=len(nums2)
        if n<m:
            return self.findMedianSortedArrays(nums2,nums1)
        low=0
        high=m
        while low<=high:
            midx=low+(high-low)//2
            midy=((m+n)//2)-midx
            l1=-math.inf if midx==0 else nums1[midx-1]
            r1=math.inf if midx==len(nums1) else nums1[midx]
            l2=-math.inf if midy==0 else nums2[midy-1]
            r2=math.inf if midy==len(nums2) else nums2[midy]
            if l1<=r2 and l2<=r1:
                if (m+n)%2!=0:
                    return min(r2,r1)
                else:
                    return (max(l1,l2)+min(r2,r1))/2
            if l2>r1:
                low=midx+1
            else:
                high=midx-1
        return -1