import matplotlib.pyplot as plt
import numpy as np
x = np.arrange(1, 11, 1) #[1,2,3,4,5,6,7,8,9,10]
y1= (2*x) + 1 #[3,5,7,9...]
y2= (2*x*x) + 2 #[4,9,20...]
plt.plot(x,y1, 'g', linewidth=3, label='y=2x+1')
plt.plot(x,y2, 'r', linewidth=3, label='y=2x^2+1')
plt.legend()
plt.show()