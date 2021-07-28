import random        
Maskval=[0,0,50,75,80,70,70,70,70,70,60,50,50,50,80,70,60,60,60]
TimeforHospital=5
VaccinatedVal=[0,0,0,0,0,0,0,0,0,0,0,0,5,10,15,15,18,20,25]
HospitalLimit=10000000


Severity=[0]*80+[1]*20  #In Hospital 10%chance of deTAH, ELSE 80%


chance10=[0]*9+[1]*1
chance50=[0]*5+[1]*5
chance90=[0]*1+[1]*9

days=0
Confirmed=[100]
Recovered=[0,0,0]
Death=[0]
Active=[(Confirmed[-1]-Recovered[-3])]
Data=[]
NewCases=Confirmed[0]
while(True):
    days+=14
    Interaction=TimeforHospital*NewCases
    NewCases=0
    Recoveredsample=0
    DeathSample=0
    
    Mask=[0]*(100-(Maskval[days//28]))+[1]*(Maskval[days//28])
    Vaccinated=[0]*(100-VaccinatedVal[days//28])+[1]*(VaccinatedVal[days//28])


    if Interaction>10000:
        temp=10000
    else:
        temp=Interaction
    for i in range(temp):
        NumPeople=random.randint(0,2)
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
                if Severity[random.randint(0,99)]==0:
                    Recoveredsample+=1
                else:
                    if Active[-1]//2<HospitalLimit:
                        if chance10[random.randint(0,9)]==0:
                            Recoveredsample+=1
                        else:
                            DeathSample+=1
                    else:
                        if chance90[random.randint(0,9)]==0:
                            Recoveredsample+=1
                        else:
                            DeathSample+=1
            NumPeople-=1
    if Interaction>10000:
        NewCases=int(NewCases*Interaction/10000)
        Recoveredsample=int(Recoveredsample*Interaction/10000)
        DeathSample=int(DeathSample*Interaction/10000)
    Recovered.append(Recovered[-1]+Recoveredsample)
    Confirmed.append(Confirmed[-1]+NewCases)
    Active.append((Confirmed[-1]-Recovered[-3]))
    Death.append(Death[-1]+DeathSample)
    print(days,Confirmed[-1],Active[-1],NewCases)
    
    if days>500:
        Data.append([days,Confirmed,Active,Recovered,Death])
        break

# import pickle
# with open('projectCOVID2.pkl', 'wb') as f:
#     pickle.dump(Data, f)



# with open('projectCOVID.pkl', 'rb') as f:
#     Data1= pickle.load(f)