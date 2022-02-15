def  search_bin(num, item):
   low = 0
   high = len(num)-1
   while low <= high:
         mid = (high-low)//2
         if item == num[mid]:
             return mid
         if item < num[mid]:
            high = mid-1
         else:
            low = mid+1
   return None

a = [1,3,5,7,9,11]
search_bin(a,3)





