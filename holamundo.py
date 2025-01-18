mensaje = "hola mundo"
print(mensaje)
a = 2
b = 3
for a in range(4):
    a+1
    print(a)
    for b in range(4):
        b+a
        print(b)
        for c in range(4):
            c+b
            print(c)
            for d in range(4):
                d+c
                print(d)
                for e in range(4):
                    e+d
                    print(e)
# esto es un comentario