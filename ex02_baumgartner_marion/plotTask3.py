import matplotlib.pyplot as plt
import numpy as np

fig=plt.figure()
data=np.arange(900).reshape((30,30))
for i in range(1,5):
    ax=fig.add_subplot(2,2,i)        
    ax.imshow(data)

plt.suptitle('Main title')
plt.show()   