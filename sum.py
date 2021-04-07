# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
end =  input('Type your end: ')
n = input('Type your o/e: ')
if n == "e":
    start = 0
else:
    start = 1

end = int(end)

def add(start,end,n):
    sum = 0
    for i in range(start,end+1,n):
        sum = sum + i
    print(sum)
    
add(start,end,2)
     