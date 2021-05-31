#....
#   Author is Ma'am Hira Ferman. make some changes by permission of Hira Fermn for project
#....

import random

vowel = 0
personalities = 0
inputSize = int(input("Enter the number for length of network: "))
mkePopulationSize = int(input("Enter the number for popultion size: "))
print("lets take Vowel as a 'ID' in number and same as for personalities.")
vs = int(input("Enter the start number for vowel which is generte in random: "))
ve = int(input("and Enter the end number for vowel: "))
ps = int(input("Enter the start number for personalities which is also generted in random: "))
pe = int(input("and Enter the end number for personalities: "))

def Magent(vowel,personalities):
    return (vowel,personalities)

def makePopulation(n):
    population = []
    for i in range(n):
        for j in range(inputSize):
            v = random.randint(vs,ve)
            p = random.randint(ps,pe)
            agent = Magent(v,p)
            population.append(agent)
    return population

populationN = makePopulation(mkePopulationSize)
print("\nGenerate random network population: ")
print(populationN)

def countPopulation(population):
    t = 0
    for agent in population:
        for i in range(inputSize):
            if agent[0] == i :
                t += 1
    return t / len(population)

prop = countPopulation(makePopulation(mkePopulationSize))
print("\nThe proportion in the population is: ",prop)

def chooswPair(population):
    i = random.randint(0,len(population)-1)
    j = random.randint(0,len(population)-1)
    while i==j:
        j = random.randint(0,len(population)-1)
    return population[i],population[j]

prop = makePopulation(mkePopulationSize)
listner, producer = chooswPair(prop)
print("\nThe population is: ", populationN)
print("This is the chosen pair: ", listner,",", producer)
print("The listener is: ", listner)
print("The producer is: ", producer)

def interact_test(listener, producer):
    for i in range(inputSize):
        if listener[0] == producer[0]:
            return listener
        else:
            if listener[1] == i:
                return listener
            else:
                listener = producer
                return listener

randomlistener, randomproducer = chooswPair(makePopulation(mkePopulationSize))
print("\nThe listener is", randomlistener)
print("The producer is", randomproducer)
updated_listener = interact_test(randomlistener, randomproducer)
print("After ineracting, the listener is",updated_listener)
#
def simulate(n, k):
    population = makePopulation(n)
    proportion = []
    for i in range(k):
        pair = chooswPair(population)
        interact_test(pair[0], pair[1])
        proportion.append(proportion.count(population))
    return population, proportion

new_population, proportion = simulate(20, 500)
print("\nFinal Population:", new_population)
