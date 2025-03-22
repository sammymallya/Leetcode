class Solution(object):
    def sortByBits(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        dic={}
        def count_ones(x):
            count=0
            while x:
                x&=x-1
                count+=1
            return count
        for i in arr:
            dic[i]=count_ones(i)
        arr=sorted(arr,key=lambda x:dic[x])
        for i in range(len(arr)):
            for j in range(i,len(arr)):
                if dic[arr[i]]==dic[arr[j]]:
                    if arr[i]>arr[j]:
                        arr[i],arr[j]=arr[j],arr[i]
        return arr
