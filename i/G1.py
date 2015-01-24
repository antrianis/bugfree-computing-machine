# -*- coding: utf-8 -*-
import math,string,itertools,fractions,heapq,collections,re,array,bisect
#ACB_
#ABC_
#

start = ['A','C','B','',]
end = ['A','B','C','']

start = ['A','C','B','',]
end = ['A','','C','B']


def move_car(ids,ide):
    print "we are moving car" , start[ids] ,"at pos " , ids, "to pos " , ide
    print "before" , str(start)
    temp = start[ids]
    start[ids] = end[ide]
    start[ide] = temp
    print "after" , str(end)

def solve():

    for ids,vals in enumerate(start):
        if not vals:
            empty_spot = ids

    for ids,vals in enumerate(start):
        for ide, vale in enumerate(end):
            if vals == vale and ids!=ide:
                if start[ide]:
                    move_car(ide, empty_spot)
                    empty_sport = ide
                move_car(ids,ide)


if __name__ == '__main__':
    print "Goal"
    print start
    print end
    print "----"
    solve()

#
#     my_url = "my url"
#     c  = {
#         "a" : ["a string with substituion" + my_url , "another string with subsition %(url)s" % {'url': my_url}]
#
#     }
#     for val in c:
#         print c[val]
#         for k in c[val]:
#             print k
