# Importing Required Packages
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import random
import array
import math as m
import cmath

# Binary Array to Decemial Conversion
def binarey_array2decimal(n):
    list1 = list(n)
    str1 = ''.join(str(e) for e in list1)
    out = int(str1,2)
    return out

# Decimal to Binary Conversion
def decmial_int2binary(n,k):
    # n is the input
    # k is number of bits
    a = bin(n)[2:]
    b = list(a)
    c = [int(i) for i in b]
    if len(c) == k:
        out = c
    else:
        for i in range(k-len(c)):
            c.reverse()
            c.append(0)
        c.reverse()
        out = c
    return out

# Inisialization
M = int(input('Numberof symbol in a constallation M = '))
k = int(np.log2(M))
n = int(input("Number of Transmission bits  n = "))

# Generation of Binary bits
dataIn = []
i = 0
while i < n:
    dataIn.append(random.randint(0,1))
    i += 1

# Constallation Symbols
datain = np.array(dataIn)
con_symbol = datain.reshape(int(n/k),k)

# Carrier signal
CS = np.array([complex(1,1),complex(-1,1), complex(-1,-1), complex(1,-1)])

# Mapping
Tx_symbol = []
i = 0
while i < len(con_symbol):
    mp = binarey_array2decimal(con_symbol[i])
    Tx_symbol.append(CS[mp])
    i += 1

Tx_signal = np.array(Tx_symbol)

'''
for i in range(len_eb_n0):
	#========================================================
    # Noise characteristics
    N0 = 1/(np.exp(Eb_N0_dB[i]*np.log(10)/10.0))
    noise=np.random.normal(0,np.sqrt(N0/2.0),len(Tx_signal)) 
    #=========================================================
'''
# SNR: Signal to Noise Ratio 
Eb = 1 # Energy per bit
SNRdB = np.arange(11)[1:] 
SNR = 10**(SNRdB/10)
Ber = []
Neb = []
mu = 0

# AWGN channel
for count in np.arange(len(SNR)):
    No = Eb/SNR[count]
    sigma = np.sqrt(No/2.0)
    rn = np.random.normal(mu,sigma,len(Tx_signal)) 
    crn = np.array([complex(rn[i], rn[i]) for i in np.arange(len(rn))])
    N = crn
 

# Demapping
    Rx_signal = Tx_signal + N

    i = 0
    x = []
    Rcon_symbol = []
    while i <len(Rx_signal):
        j = 0
        d = []
        while j < len(CS):
            d.append(abs(Rx_signal[i]-CS[j]))
            j += 1
            x.append(d.index(min(d)))
            Rcon_symbol.append(decmial_int2binary(x[i],k))
            i +=1

    dataout = np.array(Rcon_symbol)
    dataOut = dataout.reshape(n,1)


# Number of Errors 
    Error = 0
    for i in dataIn:
        if dataIn[i] == dataOut[i]:
            Error = Error
        else:
            Error = Error + 1   
    Neb.append(Error)
    
# Bit Error Rate (BER) or Probabulity of Error
    Ber.append(Neb[count]/len(dataIn))
    
print("Number of Errors = ",Neb)
print("Bit Error Rate = ", Ber)
plt.plot(SNR, Ber)
plt.show()









