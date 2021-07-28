# #x.append(numpy.random.normal(loc=10.0, scale=10.0, size=None))
# import random
# import numpy as np
# def generate_people(vaccinated,Precovid,Age,EagernessHospital,Mask):
#     if vaccinated:
#         if Age<45:
#             return False
#         else:
#             severe=1
#     elif PrevCovid:
#         severe=2
#     else:
#         if Age<25:
#             severe=Severity1[random.randint(0,50)]
#         elif Age<40:
#             severe=Severity2[random.randint(0,50)]
#         elif Age<60:
#             severe=Severity3[random.randint(0,50)]
#         else:
#             severe=Severity4[random.randint(0,50)]
#     return [severe,EagernessForHospital,Mask,0]
        
        

# Severity1=np.append(np.random.randint(1,4,40),np.random.randint(4,10,10))
# Severity2=np.append(np.random.randint(1,7,40),np.random.randint(7,10,10))
# Severity3=np.append(np.random.randint(1,7,35),np.random.randint(4,10,15))
# Severity4=np.append(np.random.randint(1,8,30),np.random.randint(4,8,20))


# #Severity,mask,MetingPeople,EagernessfrHospital,:People
# #Severity:=Age,earlier Disease,Previous_Covid,Vaccination
# #Character:=Phase Timeing,No of people meet*Area_Ratio

# #[n,values]
# Hospital_Limit=1000000
# Hospitalized=[0 for x in range(52)]
# self_Quarantined=[0 for x in range(52)]
# InteratedWithCovid=[[100,[7,1,0,0]]]
# Recovered=0
# RIP=0
# Confirmed=0
# Active=0

# meanVaccinated=[0,0,0,0,0,0,0,0,0,0,0,0,0,0]#outof126
# meanCovid=     [0,0,0,0,0,0,0,0,0,0,0,0,0,0]#outof126
# govRestriction=[0,0,0,0,0,0,0,0,0,0,0,0,0,0] #out of 1
# PopDensity=1
# i=0

# while(True):
#     if days%30==0:
#         vaccinated=[0]*(126-meanVaccinated[i])+[1]*meanVaccinated[i]
#         PrevCovid=[0]*(126-meanCovid[i])+[1]*meanCovid[i]
#         Age=list(range(0,25))*6+list(range(25,75))*3#list of 300
#         EagernessForHospital=[0,0,1,1,1,1,1,1,1,2,2,2,2,2]
#         MeetingPeople=[int(PopDensity*(1-govRestriction[i])*x)   for x in [0]*5+[1]*15+[2]*20+[3]*10+[4]*4+[10]*1+[7]*3]
#         mask=[0]*(100-govRestriction[i]*100)+[1]*(govRestriction[i]*100)
#         i+=1
    
    
#     for x in range(len(InteratedWithCovid)):
#         if InteratedWithCovid[1][3]<0:
#             InteratedWithCovid[x][1][3]+=1
    
#     people=generate_people(vaccinated[random.randint(0,126)],
#         PrevCovid[random.randint(0,126)],
#         Age[random.randint(0,300)],
#         EagernessForHospital[random.randint(0,14)],
#         mask[random.randint(0,100)])


#     for x in range(len(InteratedWithCovid)):
#         times=7*InteratedWithCovid[x][0]*
#         if InteratedWithCovid[x][1][1]==0:
#             if InteratedWithCovid[x][1][0]<=3:
#                 times*=1
#                 while(times):
#                     if people!=False:


import random        
Maskval=50
TimeforHospital=7
VaccinatedVal=10
HospitalLimit=1000000

Mask=[0]*(100-(Maskval))+[1]*(Maskval)
Vaccinated=[0]*(100-VaccinatedVal)+[1]*(VaccinatedVal)
Severity=[0]*80+[1]*20  #In Hospital 10%chance of deTAH, ELSE 80%


chance10=[0]*9+[1]*1
chance50=[0]*5+[1]*5
chance90=[0]*1+[1]*9

days=0
Confirmed=100
Recovered=0
Death=0
Active=Confirmed-Recovered
Data=[]
NewCases=Confirmed
while(True):
    days+=TimeforHospital
    temp=TimeforHospital*NewCases
    NewCases=0
    for i in range(temp):
        NumPeople=random.randint(0,3)
        while(NumPeople):
            flip=0
            if Vaccinated[random.randint(0,99)]==1:
                pass
            
            else:
                pt=random.randint(0,99)
                people=random.randint(0,99)
                chanceval=random.randint(0,9)
                if Mask[pt]==1 and Mask[people]==1:
                    if chance10[chanceval]==1:
                        flip=1
                elif Mask[pt]==1 and Mask[people]==0:
                    if chance50[chanceval]==1:
                        flip=1
                elif Mask[pt]==0 and Mask[people]==0:
                    if chance90[chanceval]==1:
                        flip=1

            if flip==1:
                NewCases+=1
                Confirmed+=1
                if Severity[random.randint(0,99)]==0:
                    Recovered+=1
                else:
                    if Active//2<HospitalLimit:
                        if chance10[random.randint(0,9)]==0:
                            Recovered+=1
                        else:
                            Death+=1
                    else:
                        if chance90[random.randint(0,9)]==0:
                            Recovered+=1
                        else:
                            Death+=1
            NumPeople-=1
    Active=Confirmed-Recovered
    print(days,Confirmed,Active,NewCases)
    Data.append([days,Confirmed,Active,NewCases])
    if days>200:
        break



                


                




