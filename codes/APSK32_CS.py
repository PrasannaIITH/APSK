import scipy as sp
import numpy as np
import numpy.random as random



M1 = input('Number of symbol in First Cirlce =  ' );
M2 = input('Number of symbol in Second Cirlce =  ' );
M3 = input('Number of symbol in Third Cirlce =  ' );

sqrt = np.sqrt
pi = np.pi

R1 = sqrt(7); 
P1 = pi/M1;
R2 = 3*sqrt(7); 
P2 = pi/M2;
R3 = 9*sqrt(7); 
P3 = 2*pi/M3;
RA1 = [R2,R2,R3,R3,R2,R2,R3,R3,R2,R2,R3,R3,R2,R2,R3,R3];
PH1 = [P1,P2,P3,0,pi-P1,pi-P2,pi-P1,pi-P3,-P1,-P2,-P1,-P3,pi+P1,pi+P2,pi+P3,pi];
RA2 = [R2,R1,R3,R3,R2,R1,R3,R3,R2,R1,R3,R3,R2,R1,R3,R3];
PH2a = [pi/2-P2,pi/2-P1,pi/2-P3,pi/2-P1,pi/2+P2,pi/2+P1,pi/2+P3,pi/2+P1];
PH2b = [3*pi/2+P2,3*pi/2+P1,3*pi/2,3*pi/2+P3,3*pi/2-P2,3*pi/2-P1,3*pi/2-P3,3*pi/2-P1];
R = [RA1,RA2];
PH = [PH1,PH2a, PH2b];