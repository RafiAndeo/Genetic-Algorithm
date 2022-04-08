import random

e = 2.718281828459045
generasi = 100

def sinus(e, y):
    return (e**(y*1j)).imag

def cosinus(e, x):
    return (e**(x*1j)).real

# main program
def main(x, y):
    return ((cosinus(e,x)+sinus(e,y))**2)/((x**x)+(y**y))

"""
h(x, y) = (cos x + sin y)^2 / x^2 + y^2, dengan batas -5 <= x <= 5 dan -5 <= y <= 5 
"""

# decode chromosome
kromosom =[]
for s in range(generasi):
    kromosom.append((random.uniform(-5,5),random.uniform(-5,5)))

# fitness function
def fitness(x, y):
    hasil = main(x, y)
    nilai_fitness = abs(1/hasil)

    if hasil == 0:
        return 99999
    else:
        return nilai_fitness 

# roulette wheel selection
def roulette_wheel(nilai_fitness, generasi):
    total = 0
    i = 1
    for i in range(generasi):
        total = total + nilai_fitness
    
    r = random.random()
    while (r > 0):
        r = r - nilai_fitness/total
        i = i + 1
    return i

# crossover
def crossover(generasi, rate):
    for i in range(generasi):
        if (i*random.random()) > rate:
            hasil_cross = random.random()
            if hasil_cross > 5 or hasil_cross < -5:
                hasil_cross = random.random()
            else:
                return hasil_cross

# mutation
mutasi = random.uniform(0.99,1.01)

# solutions
for i in range(generasi):
    genom = []
    rasio = 10
    for s in kromosom:
        nilai_fitness = fitness(s[0],s[1])
        genom.append( (nilai_fitness,s) )
    genom.sort()
    genom.reverse()
    crossover(generasi, rasio)
    roulette_wheel(nilai_fitness, generasi)

    print(f"== Gen {i} best solutions === ")
    print(genom[0])
    print("Hasil =",(abs(main(s[0],s[1]))))

    if s[0] > 5 or s[0] < -5 or s[1] > 5 or s[1] < -5:
        break

    # changing generations
    kromosom_terbaik = genom[:100]
    
    gen = []
    for s in kromosom_terbaik:
        gen.append(s[1][0])
        gen.append(s[1][1])

    newGen = []
    for _ in range(generasi):
        g1 = random.choice(gen) * mutasi
        g2 = random.choice(gen) * mutasi

        newGen.append( (g1,g2) )

    kromosom = newGen