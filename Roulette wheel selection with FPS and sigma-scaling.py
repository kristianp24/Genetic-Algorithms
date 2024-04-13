def fitness(x):
    return math.sin(x-2)**2

def generare_pop(dim):
    pop = []
    for i in range(dim):
        x = np.random.randint(1,2501)
        fit = fitness(x)
        binary = [bin(x)[2:]]

        vect = [binary,fit]
        pop.append(vect)
    return pop

def roulette(pop,sigma):
    fitness_val = np.zeros(len(pop))
    for i in range(0,len(pop)-1):
        fitness_val[i] = pop[i][-1]

    mean = np.mean(fitness_val)
    dev = np.std(fitness_val)
    scaled_fit = (fitness_val-mean)/dev

    selection_prob = scaled_fit/sum(fitness_val)

    parinti = []
    for i in range(len(pop)):
        randomp = np.random.uniform(0,1)
        cumulativep=0
        for i in range(len(selection_prob)):
            cumulativep+=selection_prob[i]
            if cumulativep > randomp:
                parinti.append(pop[i])
                break
    return parinti


pop = generare_pop(10)
fit = roulette(pop,0.3)

for p in pop:
    print(p)

print("Parinti")
for f in fit:
    print(f)