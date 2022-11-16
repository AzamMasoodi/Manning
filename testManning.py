"""
Calculate Manning coeficient
Flow Resistance in Open Channel Due to Vegetation at Reach
Scale: A Review (D’Ippolito,2021)
Flexibilt range: (-2 - 0)
Bx=channel blockage
wVeg*hVeg:total cross-sectional area of vegetation in the channel (Fig.5)
"""
import numpy as np
import matplotlib.pyplot as plt
#Depth of water (m)

'''flexibilty=0'''
hVeg=0.214
LVeg=2.47
W=3.56
CDrag=1
a=100
Cf=0.052
grav=9.81
kLN=1
'''Bx=(LVeg*hVeg)/(W*DWH)'''
'''DensVeg=(m*(np.pi)*dVeg^2)/4'''
'''if flexibility==0:'''
def Manning(DWH):
    if DWH<=hVeg:
        Bx=LVeg/W
        if Bx < 0.8:
            '''Eq.24'''
            n=((kLN*(DWH**(1/6)))/(grav**0.5))*((C/2)**0.5)*((1-Bx)**(-3/2))
            plt.plot(Bx, n, 'ro')
            plt.show()
        else:
            '''Eq.26'''
            n=((kLN*(DWH**(1/6)))/(grav**0.5))*((CDrag*a*DWH/2)**(1/2))
            plt.plot(Bx, n, 'ro')
            plt.show()
        return n,Bx
    else:
        #DHW>=hVeg
        Bx=(LVeg*hVeg)/(W*DWH)
        ''' Eq.29 pp.14'''
        n=((kLN*(DWH**(1/6)))/(grav**0.5))*(1/(((2/C)**0.5)*((1-hVeg/DWH)**1.5)+((2/(CDrag*a*DWH))**0.5)*(hVeg/DWH)))
        plt.plot(Bx, n, 'ro')
        plt.show()
    return n,Bx
print(Manning(0.36))

