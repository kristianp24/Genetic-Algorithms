def fitness(x,y,z,t):
    return y*(math.sin(x-2))**2+z+t

def generare_pop(dim):
    pop = np.zeros([dim,5])
    for i in range(dim):
        x = np.random.randint(1,1500)
        y=np.random.randint(-1,2500)
        z = np.random.randint(10,250)
        t = np.random.randint(10,250)
        fitnes = fitness(x,y,z,t)
        vector  = [x,y,z,t,fitnes]

        pop[i] = vector.copy()
    return pop

def operator_recombinare(parent1,parent2):
    child1=parent1.copy()
    child2=parent2.copy()

    prob = np.random.uniform(0,1,4)
    for i in range(4):
        if prob[i] > 0.5:
            child1[i],child2[i] = parent2[i],parent1[i]

    return child1,child2

def cross_pop(pop,pc):
    popn = pop.copy()
    for i in range(0,len(pop),2):
        prob = np.random.uniform(0,1)
        if prob <=pc:
            c1,c2 = operator_recombinare(pop[i],pop[i+1])
            fit1 = fitness(c1[0],c1[1],c1[2],c1[3])
            fit2 = fitness(c2[0],c2[1],c2[2],c2[3])
            c1[4] = fit1
            c2[4] = fit2
            popn[i] = c1
            popn[i+1] =c2
    return popn

pop = generare_pop(10)
print(pop)
print("Pop noua:")
popn = cross_pop(pop,0.8)
print(popn)