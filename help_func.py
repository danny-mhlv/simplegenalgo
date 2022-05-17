import numpy as np
import random


def get_target(x):
    return 0.2*x + x*np.sin(8.9*x) + 0.9*np.cos(1.5*x - 2)


def get_fitness(x):
    return (0.2*x + x*np.sin(8.9*x) + 0.9*np.cos(1.5*x - 2)) + 2.5


def generate_chrom(length):
    out = []
    for i in range(length):
        out.append(random.randint(0, 1))
    return out


def pop_random(lst):
    index = random.randrange(0, len(lst))
    return lst.pop(index)


def make_pairs(population):
    pairs = []
    copy = population.copy()
    while copy:
        parent1 = pop_random(copy)
        parent2 = pop_random(copy)
        pair = parent1, parent2
        pairs.append(pair)
        # print(f"Parent1: {pair[0].genotype} | Parent2: {pair[1].genotype}")
    return pairs


def cross(pair, chrom_len, p_mutation):
    genome1 = pair[0].genotype
    genome2 = pair[1].genotype

    cut_index = random.randint(0, chrom_len-1)  # Revert to chrom_len??
    for index in range(cut_index, chrom_len):
        tmp = genome1[index]
        genome1[index] = genome2[index]
        genome2[index] = tmp

    if random.uniform(0, 1) <= p_mutation:
        mutated_gene = random.randint(0, chrom_len)
        genome1[mutated_gene] = 0 if genome1[mutated_gene] == 1 else 1
    if random.uniform(0, 1) <= p_mutation:
        mutated_gene = random.randint(0, chrom_len)
        genome2[mutated_gene] = 0 if genome2[mutated_gene] == 1 else 1

    return [genome1, genome2]


def int_list2str(lst: list):
    string_ints = [str(n) for n in lst]
    return "".join(string_ints)
