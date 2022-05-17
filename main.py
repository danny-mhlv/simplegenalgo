from matplotlib import pyplot as plt
import numpy as np
import help_func as myfunc
import random

POP_COUNT = 50
CHROM_LEN = 20

P_CROSS = 0.85
P_MUTATION = 0.15
RANGE_L = -3
RANGE_R = 3

step = (RANGE_R - RANGE_L) / 2 ** CHROM_LEN


class Individual:
    def __init__(self, phenotype, genotype, fitness) -> None:
        self.phenotype = phenotype
        self.genotype = genotype
        self.fitness = fitness


# Initialize
population = []
for i in range(POP_COUNT):
    genotype = myfunc.generate_chrom(CHROM_LEN)
    phenotype = RANGE_L + int(myfunc.int_list2str(genotype), base=2) * step
    fitness = myfunc.get_fitness(phenotype)

    population.append(Individual(phenotype, genotype, fitness))

# # Generate pairs
# pairs = myfunc.make_pairs(population)
# # Crossing and mutation
# for pair in pairs:
#     if random.uniform(0, 1) <= P_CROSS:
#         children = myfunc.cross(pair, CHROM_LEN, P_MUTATION)
#         population.extend(children)
# # Reduction (Roulette)

# X = []
# for i in range(POP_COUNT):
#     X.append(population[i][0])
# Y = []
# for i in range(POP_COUNT):
#     Y.append(population[i][1])

# plt.plot(X, Y)
# plt.show()
