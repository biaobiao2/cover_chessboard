# encoding:utf-8
'''
Created on 2018年10月18日

@author: liushouhua
'''
k = 3
#棋盘的边长
row_size = pow(2, k)

#初始化棋盘
table = [[-1 for i in range(row_size)] for i in range(row_size)]
# L形块的初始值
mark = 0

def draw(topx,topy,sx,sy,size):
    """
    @param topx,topy: 棋盘的左上角坐标
    @param sx,sy: 特殊方格的坐标
    @param size: 棋盘尺寸 
    """
    global mark
    global table
    if size == 1:
        return
    
    #防止递归是改变值，要设置变量保存
    mark += 1
    count = mark
    half = size/2
    
    #处理左上部分棋盘
    if sx < half + topx and sy < half + topy:
        draw(topx,topy,sx,sy,half)
    else:
        table[half+topx-1][half+topy-1] = count
        draw(topx,topy,half+topx-1,half+topy-1,half)
    
    #处理右上部分棋盘
    if sx >= half + topx and sy < half + topy:
        draw(topx+half, topy,sx,sy,half)
    else:
        table[half+topx][half+topy-1] = count
        draw(topx+half,topy,half+topx,half+topy-1,half)
    
    #处理坐下部分棋盘
    if sx < half + topx and sy >= half + topy:
        draw(topx,half + topy,sx,sy,half)
    else:
        table[half+topx-1][half+topy] = count
        draw(topx,half + topy,half+topx-1,half+topy,half)
        
    #处理右下部分棋盘
    if sx >= half + topx and sy >= half + topy:
        draw(topx+half,half+topy,sx,sy,half)
    else:
        table[half+topx][half+topy] = count
        draw(topx+half,half+topy,half+topx,half+topy,half)


def show(t):
    n = len(t)
    for i in range(n):
        for j in range(n):
            print "%s\t" % t[i][j],
        print
        
draw(0, 0, 1, 1, row_size)
show(table)




    
    