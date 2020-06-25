'''
Probability of two students in same class having same birth date
ONLY DAY AND NOT YEAR
numTrials = number of classes to simulate
user can set ClassSize 20-200
func receives input numpy vector of length class size
Should return 1 for same bday, 0 for not
0 and 364 to represent bday
'''
import numpy as np
import matplotlib.pyplot as plt

def probability_same_birthdays():
    k = 0
    x = np.zeros(9)
    y = np.zeros(9)
    numTrials = 1000 #input
    
    for num in range(25,250,25):
        ClassSize = num #input
        birthdays = np.random.randint(0, 364, size=(numTrials, ClassSize))
        duplicate_birthdays = np.zeros(numTrials)
                    
        for i in range(numTrials):  
            if len(birthdays[i]) != len(set(birthdays[i].flatten())):
                duplicate_birthdays[i] = 1
                        
        total_duplicates = np.sum(duplicate_birthdays)
        y[k] = total_duplicates * 100 / float(numTrials)
        x[k] = ClassSize   
        k += 1
    print(y)
    
    plt.plot(x,y)
    plt.xlabel('Class Size')
    plt.ylabel('Chance Two Students Will Have Same Birthday (%)')
    plt.show()
    
    
print(probability_same_birthdays())