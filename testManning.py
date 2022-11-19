'''
Calculate Manning coefficient
Flow Resistance in Open Channel Due to Vegetation at Reach
Scale: A Review (D’Ippolito,2021)
Flexibilty range: (-2 - 0)
wVeg*hVeg:total cross-sectional area of vegetation in the channel (Fig.5)
'''

'''
DWH: Depth of water (m)
grav:Gravitational acceleration constant (m.s-2)
a:The frontal area per unit volume parameter (m-1), for channel it is about 100
C: coefficient to parameteriz the shear stress at the interface between vegetated and unvegetated regions.
    The range of this parameter is 0.05–0.13 (Luhar and Nepf, 2012).
kLN: a constant to correct the dimension of equation (m1/3.s-1)
Bx:Blockage factor
DensVeg=(m*(np.pi)*dVeg^2)/4

if flexibility==0:'''

import pandas as pd
import openpyxl 
import matplotlib.pyplot as plt


wrkbk = openpyxl.load_workbook("NikoraData.xlsx") 
print(wrkbk)
df = wrkbk.active
mylist_n=[]
mylist_Bx=[]
for i in range(2, df.max_row+1):
    DWH=(df.cell(row=i,column=1)).value
    W=(df.cell(row=i,column=2)).value
    hVeg=(df.cell(row=i,column=3)).value
    wVeg=(df.cell(row=i,column=4)).value
    CDrag=1
    a=100
    C=0.052 #input(float,'Coefficent of shear stress at the interface')  # The range of this parameter is 0.05–0.13 (Luhar and Nepf, 2012).
    grav=9.81
    kLN=1
    def Manning(DWH):
        if DWH<=hVeg:
            Bx = wVeg/W
            if Bx < 0.8:
                '''Eq.24'''
                n = ((kLN*(DWH**(1/6)))/(grav**0.5))*((C/2)**0.5)*((1-Bx)**(-3/2))
            else:
                '''Eq.26'''
                n = ((kLN*(DWH**(1/6)))/(grav**0.5))*((CDrag*a*DWH/2)**(1/2))
            mylist_n.append(n)
            mylist_Bx.append(Bx)
            return mylist_n, mylist_Bx, Bx
            
        else:
            #DHW>=hVeg
            Bx = (wVeg*hVeg)/(W*DWH)
            ''' Eq.29 pp.14'''
            n =((kLN*(DWH**(1/6)))/(grav**0.5))*(1/(((2/C)**0.5)*((1-hVeg/DWH)**1.5)+((2*hVeg/(CDrag*a))**0.5)*(1/DWH)))
            mylist_n.append(n)
            mylist_Bx.append(Bx)
        return mylist_n, mylist_Bx, Bx
        

    Manning(DWH)
plt.plot(mylist_Bx, mylist_n, 'ro')
plt.show()
output=["%.3f" % elem for elem in mylist_n]
output_2=["%.3f" % elem for elem in mylist_Bx]
print('n:',output)
print('Bx:',output_2)
