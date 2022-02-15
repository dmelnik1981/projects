def  search_bin(num, item):
   low = 0
   high = len(num)-1
   while low <= high:
         mid = (high-low)//2
         guess = num[mid]
         if item == guess:
             return mid
         if item < guess:
            high = mid-1
         else:
            low = mid+1
   return None

a = [1,3,5,7,9,11]
print(search_bin(a,3))





