def f11(m):
    f = open("C:\\heheheh.pyw", 'w')
    f.write("test")
    f.close()
    g = open("C:\\heheheh.pyw", 'r')
    import os
    if 'os' in locals(): t = True
    else: t = False
    return [g.read(), t]