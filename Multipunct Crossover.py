def fitness(x,y):
    return y*(math.sin(x-2))**2

def generare_populatie(dim):
    populatie=[]
    for i in range(dim):

        x=np.random.randint(1,1500)
        y=np.random.randint(-1,2500)
        valoare=fitness(x,y)

        x_binar=bin(x)[2:]
        y_bianr = bin(y)[2:]
        vector = [x_binar,y_bianr]
        vector.append(valoare)
        populatie.append(vector)
    return populatie

def crossover_multipunct(parent1,parent2):
    child1=parent1.copy()
    child2=parent2.copy()
    points = sorted(np.random.randint(0,len(parent1),3))

    for i in range(len(points)):
        pozitia = points[i]
        child1[pozitia],child2[pozitia] = parent2[pozitia],parent1[pozitia]

    return child1,child2


def crossover_population(pop,pc):
    popc = pop.copy()

    for i in range (0,len(pop),2):
        prob = np.random.uniform(0,1)
        if prob <= pc:
            c1=pop[i][:2]
            c2=pop[i+1][:2]

            child1,child2=crossover_multipunct(c1,c2)
            x=int(child1[0],2)
            y=int(child2[1],2)
            val1=fitness(x,y)
            child1.append(val1)

            x1=int(child2[0],2)
            y1=int(child2[1],2)
            val2=fitness(x1,y1)
            child2.append(val2)

            popc[i] =child1
            popc[i+1]=child2
    return popc



pop = generare_populatie(10)
copii=crossover_population(pop,0.8)
for p in pop:
    print(p)
print("Copii:")
for p in copii:
    print(p)

