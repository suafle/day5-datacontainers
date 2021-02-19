import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson,norm,ttest_ind


#Ex a
mu = 100
x = np.arange(poisson.ppf(0.01, mu),poisson.ppf(0.99, mu))
st = poisson(mu)
pmf = poisson.pmf(x,mu)
cdf = poisson.cdf(x,mu)
data1 = st.rvs(size=1000)

plt.plot(x,pmf)
plt.title(r'PMF Poisson $\mu$ = 100')
plt.show()
plt.close()

plt.plot(x,cdf)
plt.title(r'CDF Poisson $\mu$ = 100')
plt.show()
plt.close()

plt.hist(data1)
plt.title('Histogram 1000 Realizations for Poisson')
plt.show()
plt.close()

#Ex b
mu = 0 
std = 1
normal = norm(mu,std)
x = np.arange(-4,4,0.01)
pdf = normal.pdf(x)
cdf = normal.cdf(x)
data2 = normal.rvs(size=1000)

plt.plot(x,pdf)
plt.title(r'PDF Normal $\mu$ = 0, $\sigma$ = 1')
plt.show()
plt.close()

plt.plot(x,cdf)
plt.title(r'CDF Normal $\mu$ = 0, $\sigma$ = 1')
plt.show()
plt.close()

plt.hist(data2)
plt.title('Histogram 1000 Realizations for Normal')
plt.show()
plt.close()

#Ex c
stat = ttest_ind(data1,data2)
print('Assuming equal variance :', stat)
stat = ttest_ind(data1,data2,equal_var=False)
print('Assuming different variance :', stat)

