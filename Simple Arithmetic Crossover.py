
def fitness(vect,valori):
    return np.dot(vect,valori)

def generare_pop(dim,valori):
    populatie=[]
    calitate=np.zeros(10)
    for i in range(10):
        vect = np.random.uniform(-1,1,size=10)
        suma=sum(vect)
        vect[9]=1-suma
        vectorFinal=vect*(vect[9]/suma)
        fit = fitness(vectorFinal,valori)
        calitate[i]=fit
        populatie.append(vectorFinal)
    return populatie,calitate

def aritmetica_simpla(p1,p2):
    return (p1+p2)/2

def cross(pop,dim,valori,pc):
    copii=[]
    for individ in pop:
        i = np.random.randint(0,10)
        other_individ=pop[i]
        prob = np.random.uniform(0,1)
        if prob<=pc:
            child = aritmetica_simpla(individ,other_individ)
            suma=sum(child)
            child[len(child)-1]=1-suma
            final_child = child*(child[len(child)-1]/suma)
            copii.append(final_child)
        else:
            copii.append(individ)
    return copii;

valori = [4,2,6,4,8,9,9,7,2,1]
pop,calitate = generare_pop(10,valori)
copii = cross(pop,10,valori,0.8)
for p in pop:
    print(p)
print("Copii")
for c in copii:
    print(c)