def mergesort(x):
    if len(x) > 1:
        middle = int(len(x) / 2)
        left = x[:middle]
        right = x[middle:]

        mergesort(left)
        mergesort(right)
        i,j,k = 0,0,0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
              x[k] = left[i]
              i += 1
            else:
                x[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            x[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            x[k]=right[j]
            j += 1
            k += 1
a = str(input("enter the 1-st word "))
b = str(input("enter the 2-nd word "))
while len(b) != len(a):
    b = str(input("enter another 2-nd word "))

a_m = []
for m in a:
    a_m.append(m)
b_m = []
for m in b:
    b_m.append(m)
mergesort(a_m)
mergesort(b_m)
if str(a_m) == str(b_m):
    print("these words are anagrams")
else:
    print( "these words are not anagrams ")

