z = 7
m = 'o'
val= True

y = [9,"m", ["Casa"]]

print(y)
for elemento in y:
    if type(elemento) == int:
        y[0]=elemento+10
        print(elemento+10)
    else:
        print(f"El elemento es: {elemento}")
print(y)