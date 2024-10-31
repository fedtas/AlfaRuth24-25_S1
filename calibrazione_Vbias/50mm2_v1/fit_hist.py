import numpy as np
import matplotlib.pyplot as plt
from iminuit import Minuit
from iminuit.cost import ExtendedBinnedNLL
from scipy.stats import norm

file = input("File: ")
raw_data = np.loadtxt(file)

data1 = []

for i in range(len(raw_data)):
    for j in range(int(raw_data[i])):
        data1.append(i)

data = np.array(data1)

signal = []

for i in range(len(data)):
    if data[i] > 4780 and data[i] < 4880: signal.append(data[i])

def model(x,N,mu,sigma):
	return N * norm.cdf(x, loc = mu, scale = sigma)

nbins = int(np.ceil(1 + np.log(len(signal)/np.log(2)))) * 5

bin_content, bin_edges, _ = plt.hist(signal, bins = nbins)

N_events = sum(bin_content)

costf = ExtendedBinnedNLL(bin_content, bin_edges, model)

my_minuit = Minuit(costf, N = len(data), mu = 4800, sigma = 10)
my_minuit.migrad()

channel = my_minuit.values['mu']
err_ch = my_minuit.errors['mu']
fwhm = 2.355 * my_minuit.values['sigma']
err_fwhm = 2.355 * my_minuit.errors['sigma']
frac = fwhm / channel
err_frac = frac * (err_ch/channel + err_fwhm/fwhm)

print("chi2: " + str(my_minuit.fval/my_minuit.ndof))
print("channel: " + str(channel)  + " +/- " + str(err_ch))
print("fwhm: " + str(fwhm) + " +/- " + str(err_fwhm))
print("fwhm/channel (1e-3): " + str(frac * 10**3) + " +/- " + str(err_frac * 10**3))