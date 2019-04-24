import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
import cmath
import numpy.random as random
import math 
import array 


# Initialization 
n = input("Number of Transmission Bits n = ")
M = input("Number of Constallation Symbols M = ")
k = int(np.log2(M))
R1 = np.sqrt(7)
R2 = 3*R1

# Binary Array to Decemial Conversion
def binarey_array2decimal(n):
    list1 = list(n)
    str1 = ''.join(str(e) for e in list1)
    out = int(str1,2)
    return out


# Generation of Input Data
dataIn = random.randint(0,2,n)
# Constlation Bits
con_bits = dataIn.reshape(int(n/k),k)

# Carrier SIgnal (Constalation Symbols)

#QPSK
#CS = np.array([np.exp(1j*np.pi/4),np.exp(1j*-1*np.pi/4),np.exp(1j*3*np.pi/4),np.exp(1j*-3*np.pi/4)])

#8PSK
CS = np.array([R1*np.exp(1j*np.pi/4), R1*np.exp(1j*2*np.pi), R1*np.exp(1j*np.pi), R1*np.exp(1j*5*np.pi/4),R1*np.exp(1j*np.pi/2),R1*np.exp(1j*-1*np.pi/4), R1*np.exp(1j*3*np.pi/4),R1*np.exp(1j*3*np.pi/2) ])

 
#16APSK
#CS = np.array([R2*np.exp(1j*np.pi/4),R2*np.exp(1j*-1*np.pi/4),R2*np.exp(1j*3*np.pi/4),R2*np.exp(1j*5*np.pi/4),R2*np.exp(1j*np.pi/12),R2*np.exp(1j*-1*np.pi/12),R2*np.exp(1j*11*np.pi/12),R2*np.exp(1j*13*np.pi/12),R2*np.exp(1j*5*np.pi/12),R2*np.exp(1j*-5*np.pi/12),R2*np.exp(1j*7*np.pi/12),R2*np.exp(1j*-7*np.pi/12),R1*np.exp(1j*np.pi/4),R1*np.exp(1j*-1*np.pi/4),R1*np.exp(1j*3*np.pi/4),R1*np.exp(1j*5*np.pi/4)])


Tx_signal = 1j*np.zeros(len(con_bits))
for i in range(len(con_bits)):
    Tx_signal[i] = CS[binarey_array2decimal(con_bits[i])]
    
# AWGN channel
ebnodb=np.arange(0,11,1)
errors=np.zeros(len(ebnodb))
e=np.size(ebnodb)
m=0
ber=np.zeros(e)

for i in range(e):
    sigma=np.sqrt(0.5*(10.0**(-ebnodb[i]/10.0)))
    noise=np.random.normal(0,sigma,len(Tx_signal))+1j*np.random.normal(0,sigma,len(Tx_signal))
    
    # Received signal with AWGN Noise  noise[i]
    Rx_signal = np.add(Tx_signal, noise)
    #Demapping
    dmin_ind = np.zeros(len(Rx_signal),int)
    for j in range(len(Rx_signal)):
        dist= np.zeros(len(CS))
        for l in range(len(dist)):
            dist[l] = abs(Rx_signal[j] - CS[l])
        dmin_ind[j] = dist.argmin()
    
    dm_bin_str = []
    Rx_con_bits = []
    j = 0
    while j < len(dmin_ind):
        dm_bin_str.append( np.binary_repr(dmin_ind[j],width =k))
        Rx_con_bits.append(list(dm_bin_str[j]))
        j +=1
        
    Rx_con_bits_ary = np.array(Rx_con_bits, int)
    dataOut = np.reshape(Rx_con_bits_ary,n)
    errors[i]=(dataOut!=dataIn).sum()
        

ber=np.true_divide(errors,len(dataIn))    
#theoryBer=0.5*erfc(np.sqrt(0.5*(10**(0.1*ebnodb))))
#plt.plot(ebnodb,theoryBer,'r',ebnodb,ber,'b')
#plt.semilogy(ebnodb,theoryBer,'r',linewidth=1)
plt.semilogy(ebnodb,ber,'-s')
#plt.legend(['theory','Practical'],loc=1)
plt.yscale('log')
plt.ylabel('BitErrorRate')
plt.xlabel('Eb/N0 in dB')
plt.title('BER for 8PSK in AWGN without Channel Coding')
#plt.xtricks([0,1,2,3,4,5,6,7,8,9,10,11])
plt.grid()
plt.show()


