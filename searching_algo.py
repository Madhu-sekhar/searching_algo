#linear search


new_list=[i for i in range(1,31)]
print(new_list)



for i in new_list:
  if i==20:
    print('The element is found')
    break
else:
  print('The elemtn is not found')
  
print()


#binary  search

target=100
low=0
mid=0
high=len(new_list)-1

while low <= high:
  mid=(low+high)//2
  if new_list[mid]==target:
    print(f'Your element is found {new_list[mid]}')
  elif target>new_list[mid]:
    low=mid+1
  elif target<new_list[mid]:
    high=mid-1
  else:
    print('the element is not in the list')
    