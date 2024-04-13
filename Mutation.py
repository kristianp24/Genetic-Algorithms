def fitness(individ,valori):
    return np.dot(individ,valori)

def generare_pop(dim,valori):
    pop=np.zeros([dim,5])
    calitate = np.zeros(dim)
    for i in range(dim):
        individ = np.random.permutation(5)
        calitat = fitness(individ,valori)

        pop[i] = individ
        calitate[i] =calitat
    return pop,calitate

def op_mutatie(individ):
    n=len(individ)
    p1 = np.random.randint(0,n-1)
    p2 = np.random.randint(p1+1,n)
    individ_copy = individ.copy()
    for k in range(p2,p1,-1):
        individ_copy[p1] = individ[p2]
        p1+=1
    return individ_copy

def generare_popnoua(pop,pm,valori,cal):
    popn=pop.copy()
    calitate = cal.copy()
    for i in range(0,len(pop)):
        prob = np.random.uniform(0,1)
        if prob <= pm:
            individNou = op_mutatie(pop[i])
            calitateNoua=fitness(individNou,valori)

            popn[i] = individNou;
            calitate[i] = calitateNoua
    return  popn,calitate


valori = [5,4,6,9,8]
pop,calitate = generare_pop(10,valori)
popn,calitaten=generare_popnoua(pop,0.8,valori,calitate)
print(pop)
print("Calitati:")
print(calitate)
print("Pop noua:")
print(popn)
print("Calitati noua")
print(calitaten)