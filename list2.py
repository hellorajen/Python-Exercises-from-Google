#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Additional basic list exercises

# D. Given a list of numbers, return a list where
# all adjacent == elements have been reduced to a single element,
# so [1, 2, 2, 3] returns [1, 2, 3].
# You may create a new list or
# modify the passed in list.
def remove_adjacent(nums):
  # +++your code here+++
  i=0
  while(len(nums)>i+1):
    if(nums[i]==nums[i+1]):
      nums.pop(i+1)
    else:
      i=i+1
  return nums
 
# E. Given two lists sorted in increasing order, create and return a merged
# list of all the elements in sorted order. You may modify the passed in lists.
# Ideally, the solution should work in "linear" time, making a single
# pass of both lists.

from heapq import merge
def linear_merge2(list1, list2):
  return(list(merge(list1,list2)))

def linear_merge(list1, list2):
  # +++your code here+++
  i=0
  while (len(list1)>i):
    # print('---------------------')
    # print('i= ',i,' ', list1[i], ' ', list1)
    j=0
    while (len(list2)>j):
        
        # print('i=', i, ' ', list1[i], ' compared with j= ',j,' ',list2[j], ' ', list2)
        if list1[i]>=list2[j]:
            list1.insert(i,list2[j])
            list2.pop(j)
            # print(list1)
        # uncomment following 2 lines
        # if you do not want duplicates coming from another list    
        #elif list1[i]==list2[j]:
        #    list2.pop(j)
        else:
            # print('i=', i, ' ', list1[i], ' compared with j= ',j,' ',list2[j], ' ', list2, 'breaking inner loop')
            break
    i+=1
  list1.extend(list2)  
  return list1

# Note: the solution above is kind of cute, but unforunately list.pop(0)
# is not constant time with the standard python list implementation, so
# the above is not strictly linear time.
# An alternate approach uses pop(-1) to remove the endmost elements
# from each list, building a solution list which is backwards.
# Then use reversed() to put the result back in the correct order. That
# solution works in linear time, but is more ugly.


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print ('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


# Calls the above functions with interesting inputs.
def main():
  print ('remove_adjacent')
  test(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
  test(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
  test(remove_adjacent([]), [])
  test(remove_adjacent([1, 2, 2, 2, 3, 4]), [1, 2, 3, 4])
  test(remove_adjacent([2]), [2])
 
  print ('linear_merge')
  test(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']),
       ['aa', 'bb', 'cc', 'xx', 'zz'])
  test(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']),
       ['aa', 'bb', 'cc', 'xx', 'zz'])
  test(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']),
       ['aa', 'aa', 'aa', 'bb', 'bb'])

  print ('linear_merge 2')
  test(linear_merge2(['aa', 'xx', 'zz'], ['bb', 'cc']),
       ['aa', 'bb', 'cc', 'xx', 'zz'])
  test(linear_merge2(['aa', 'xx'], ['bb', 'cc', 'zz']),
       ['aa', 'bb', 'cc', 'xx', 'zz'])
  test(linear_merge2(['aa', 'aa'], ['aa', 'bb', 'bb']),
       ['aa', 'aa', 'aa', 'bb', 'bb'])


if __name__ == '__main__':
  main()
