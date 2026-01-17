lst1 = [2, 3, 5, 15, 25,]
lst2 = [1, 7, 17, 20, 30, 35, 40, 45, 50, 55]
lstresult = []
i=j=0
def mergesort(lst):
      if len(lst) <= 1:
            return
      mid = len(lst) // 2
      leftlst = mergesort(lst, 0, mid)
      rightlst = mergesort(lst, mid, len(lst))
      return mergesort(leftlst, rightlst)
while i < len(lst1) and j < len(lst2):
      if lst1[i] < lst2[j]:
          lstresult.append(lst1[i])
          i += 1
      else:
            lstresult.append(lst2[j])
            j += 1
while j < len(lst2):
     lst1 .append(lst2[j])
     j+=1
while i < len(lst1):
        lstresult.append(lst1[i])
        i += 1
print(lstresult)
