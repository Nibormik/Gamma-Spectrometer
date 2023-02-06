import matplotlib.pyplot as plt
import random
width = 1023
X = [random.randint(0,65664)/(i*0.011+1) for i in range(0,width)]
Y = [i for i in range(0,width)]
plt.bar(Y,X,1)
plt.show()