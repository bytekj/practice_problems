#!/bin/python3
# Taum is planning to celebrate the birthday of his friend, Diksha. There are two types of gifts that Diksha wants from Taum: one is black and the other is white. To make her happy, Taum has to buy  number of black gifts and  number of white gifts.

# The cost of each black gift is  units.
# The cost of every white gift is  units.
# The cost of converting each black gift into white gift or vice versa is  units.
# Help Taum by deducing the minimum amount he needs to spend on Diksha's gifts.

import sys

t = int(input().strip())
for a0 in range(t):
    b, w = input().strip().split(' ')
    b, w = [int(b), int(w)]
    x, y, z = input().strip().split(' ')
    x, y, z = [int(x), int(y), int(z)]

def cost_of_gift(b, w, x, y, z):
    pass