
'''
    描述：打印三角形图案。
    时间：2020年1月14日12:17:02
    作者：Dragon
'''

'''
打印第一种图案
*
**
***
****
*****
'''
for r1 in range(1,6):
    for c1 in range(1,6):
        if c1<=r1:
            print("*",end="")
    print()

'''
打印第二种图案
    *
   **
  ***
 ****
*****
'''
for r2 in range(1,6):
    for c2 in range(1,6):
        if (6-c2) > r2:
            print(" ",end="")
        else:
            print("*", end="")
    print()

'''
打印第三种图案：1,3,5,7,9
    *    2i-1个，n行，【2n-(2i-1)】/2
   ***
  *****
 *******
*********
'''
for i in range(5):
    for _ in range(5 - i - 1):
        print(' ', end='')
    for _ in range(2 * i + 1):
        print('*', end='')
    print()