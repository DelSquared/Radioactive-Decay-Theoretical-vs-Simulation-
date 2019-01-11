import numpy as np 
import matplotlib.pyplot as plt 

ln2=np.log(2) #halflife is fixed at 1 for simplicity

sims = 1000

No = 100
days = 20
t = range(days)

for _ in range(sims):
  population = np.ones((No))
  count = np.array([No])

  for i in range(days-1):
    for j in range(len(population)):
      if np.random.randint(0,1000)%2==0:
        population[j]=0
    s = [np.sum(population)]
    count = np.append(count,s)

  theoretical = No*np.exp(-ln2*t)

  fig=plt.figure()
  plt.plot(t,count,label="Simulation")
  plt.plot(t,theoretical,label="Theoretical")
  plt.title("Plot of N against t (Theoretical vs Simulation of Radioactive Decay)")
  plt.xlabel("t")
  plt.ylabel("N")
  plt.legend()
  plt.grid()
  plt.savefig("plot {}.png".format(_+1))
  plt.close(fig)
