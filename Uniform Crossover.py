def calitate(x,y,z,t):
    return y*(math.sin(x-2)**2)+z+t

def generare_populatie(dim):
    populatie = []
    for i in range(dim):
        x=np.random.uniform(1,1500)
        y=np.random.uniform(-1,2500)
        z=np.random.uniform(10,250)
        t=np.random.uniform(10,250)

        vector = [x,y,z,t]
        fitness= calitate(x,y,z,t)
        vector.append(fitness)
        populatie.append(vector)
    return populatie

def crossover_op(parent1,parent2):
    child1 = parent1.copy()
    child2 = parent2.copy()
    prob = np.random.uniform(0, 1, 4)
    for i in range (4):

        if prob[i] > 0.5:
            child1[i],child2[i] = parent2[i],parent1[i]

    return child1,child2

def functie_recombinare(populatie,pc):
    populatie_noua=[]
    copii = populatie.copy()
    for i in range(0,len(populatie),2):
        prob = np.random.uniform(0,1)
        if prob <=pc:
            p1=populatie[i][:4]
            p2=populatie[i+1][:4]
            c1,c2=crossover_op(p1,p2)
            new_calitate1 = calitate(c1[0],c1[1],c1[2],c1[3])
            new_calitate2=calitate(c2[0],c2[1],c2[2],c2[3])
            child1=c1
            child2=c2
            child1.append(new_calitate1)
            child2.append(new_calitate2)
            copii[i] = child1
            copii[i+1]=child2
    return copii


pop = generare_populatie(10)
copii = functie_recombinare(pop,0.8)
print("Pop Initiala:")
for p in pop:
    print(p)
print("Pop copii:")
for q in copii:
    print(q)