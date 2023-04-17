#凸n角形が凸かどうか判定する
#時計周り、反時計回りでも大丈夫

def cross(x1,y1,x2,y2): return x1*y2 - x2*y1

def is_convex(n,verttexes):
    flg = True
    for i in range(n):
        a = verttexes[i%n]
        b = verttexes[(i+1)%n]
        c = verttexes[(i+2)%n]
        
        vec_ab = [b[0] - a[0], b[1] - a[1]]
        vec_bc = [c[0] - b[0], c[1] - b[1]]
        
        if cross(*vec_ab, *vec_bc) < 0:
            flag = False
            break
    return flg