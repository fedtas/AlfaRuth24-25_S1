import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt("calibrazione_Vbias.txt")

v_bias =[]
ch = []
fwhm = []
errch = []
errfwhm= []
v_buio = []
i_buio = []
fwhm_ch=[]

R=1.1e6

for i in range(16):
	v_bias.append(data[i][0])
	ch.append(data[i][2])
	fwhm.append(data[i][4])
	errch.append(data[i][3])
	errfwhm.append(data[i][5])
	v_buio.append(data[i][1])
	i_buio.append(v_buio[i]/R)
	fwhm_ch.append(fwhm[i]/ch[i])

fig,ax = plt.subplots(1,4)
plt.scatter(v_bias, fwhm)
plt.scatter(v_bias, i_buio)
plt.scatter(v_bias, ch)
plt.scatter(v_bias, fwhm_ch)

plt.show()
