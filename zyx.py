print("\033c\033[43;30m\ndata\n")
def asort(arr):
    # Retorna os índices ordenados pelo primeiro item de cada sublista
    return sorted(range(len(arr)), key=lambda i: arr[i][0])
def processs(values):
    v=[]
    vv=[]
    vc=""
    c1=0
    c2=0
    n=0
    va=values.split("\n")
    for a in va:
        vv=[]
        c2=0
        vb=a.split(",")
        for b in vb:
            b=b.strip()
            try:
                n=int(b)
                vv=vv+[n]
            except:
                vc=b
                vv=vv+[vc]
        v=v+[vv]
    return v       
def report(arrs):
    tabs=12
    
    for a in arrs:
        for b in a:
            s=str(b)
            print(s,end="")
            ss=(tabs-len(s)-1)*" "+"|"
            print(ss,end="")
        print("")

def sreport(arr):
    idx_sorted = asort(arr)
    arr_sorted = [arr[i] for i in idx_sorted]
    report(arr_sorted)            
values="""4,0,0,0,hello
3,0,0,1,hello
2,0,0,2,hello
1,0,0,3,hello
0,0,0,4,hello"""
arr=processs(values)
sreport(arr)
