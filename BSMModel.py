# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 08:18:28 2017

@author: Raju
"""

import numpy as np

def CalcBSM(S0, K, T, r, sigma):
    I = 100000 # we will run 100000 simulations
    z = np.random.standard_normal(I)
    ST = S0 * np.exp(( r - 0.5 * sigma ** 2) * T + sigma * np.sqrt(T) * z)
    hT = np.maximum(ST - K, 0)
    C0 = np.exp(-r * T) * sum(hT) / I
    return C0
    
def acceptBSMInput():
    S0 = int(input("Enter Internal strike index level: "))
    K = int(input("Enter strike price of the Eurpoean call option: "))
    T = float(input("Enter Time to Maturity: "))
    r = float(input("Enter riskless short rate: "))
    sigma = float(input("Enter volatility: "))
    return CalcBSM(S0, K, T, r, sigma)
    

# Define a main() function that prints a little greeting.
def main():
    PredictedValue = acceptBSMInput()
    print("The value of European call option is: %5.3f" % PredictedValue)
    
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
