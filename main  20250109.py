#todo Aufgabe 0
#Erstelle eine Variable

A = 0
n_loop = 0

#todo Aufgabe 1
#Gib alle Zahlen von 1 bis 100 aus.

#i = 1
#while(i<=100):
#    print(i)
#    i = i+1

#todo Aufgabe 2
#Ersetze alle Zahlen, die durch 3 teilbar sind, durch "digital"

j = 1

while(j<=100):
    if (j % 3 == 0):
        print("digital")
    else: print(j)
    j = j+1

#todo Aufgabe 3
#Ersetze alle Zahlen, die durch 5 teilbar sind, durch "history"

k = 1

while(k<=100):
    if (k % 5 == 0):
        print("digital")
    else: print(k)
    k = k+1

#todo Aufgabe 4
#Aufgabe 2 und 3 kombiniert

l = 1

while(l<=100):
    if (l%15==0):
        print("digital history")
    elif (l%3==0):
        print("digital")
    elif (l%5==0):
        print("history")
    else: print(l)
    l = l+1

