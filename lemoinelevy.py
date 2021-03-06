#
# Copyright (c) 2017-2020, Marcin Barylski
# All rights reserved.

# Redistribution and use in source and binary forms, with or without modification, 
# are permitted provided that the following conditions are met:
# 
# 1. Redistributions of source code must retain the above copyright notice, 
#    this list of conditions and the following disclaimer.
# 
# 2. Redistributions in binary form must reproduce the above copyright notice, 
#    this list of conditions and the following disclaimer in the documentation 
#    and/or other materials provided with the distribution.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED 
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. 
# IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, 
# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, 
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, 
# OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, 
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) 
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY 
# OF SUCH DAMAGE.
# 

import math
import unittest
import sys
import numpy as np
import os
from datetime import datetime
import time
sys.path.insert(0, '..\\primes\\')
import primes

class LemoineLevyPartition:

    # object for carrying out operations on prime numbers
    primes = ""

    def __init__(self, p):
        self.primes = p
    
    def delta_constant_plus (self, iteration):
        return 2

    def delta_constant_minus (self, iteration):
        return -2

    def delta_variable (self, iteration):
        if iteration == 0:
            delta = 0
        elif iteration == 1:
            delta = 2
        elif iteration == 2:
            delta = -4
        elif iteration > 2:
            delta = 2
        return delta

    def delta_prime (self, iteration):
        if iteration == 0:
            delta = 0
        else:
            delta = self.primes.get_ith_prime(iteration + 1) - self.primes.get_ith_prime(iteration)
        return delta

    def is_even (self, number):
        return ((number & 1) == 0)   

    def search_for_partition (self, p1, p2, delta):
        found = False
        iteration = 0

        startTime = time.time()
        while (not found):
            iteration += 1
            if self.primes.is_prime (p1) and self.primes.is_prime (p2):
                found = True
            if (not found):
                p1 = p1 + delta (iteration)
                p2 = p2 - delta (iteration)/2
            if p2 < 2 or p1 < 2:
                raise ("CouldNotFindGP")
        duration = time.time() - startTime
        return p1, p2, duration, iteration

    def find_all_sums (self, n):
        min_i = 2
        max_i = n
        factors = []
        for i in range (min_i, max_i):
            p1 = i
            p2 = n - p1*2
            if self.primes.is_prime(p1) and self.primes.is_prime (p2):
                pair = (p1, p2)
                factors.append (pair)
            
        return factors
