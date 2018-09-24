#Frist we are going to define the Data
t_inf1=20.0   #inlet temperature
t_inf2=-10.0  #outlet temperature
D_T=(t_inf1-t_inf2)  #temperature difference
L_glass= 0.004  #thikness of the glass
L_gap=0.010 # thikness of the gap between the two glasses
H=0.8  # height of he window
W=1.5  # wide of the window
A= H*W  #Area of the window
k_glass=0.78  #conductive coefficient of the glass
k_air=0.026   #conductive coefficient of he air
h_out=40   #convective coefficient outside
h_in=10    # convective coeeffuicient inside

#Now we compute the resistances, then the total resistance as the summ of the all resistance 
R1=1/(h_out*A)
R2=L_glass/(k_glass*A)
R3=L_gap/(k_air*A)
R4=R2
R5=1/(h_in*A)

Rtot=R1+R2+R3+R4+R5
#once the resistances are known, the heat transfer through the wall is the 
# temperature difference in and out divided the total resistance

Q=D_T/Rtot
print( "the heat transfer is equal to " + str(Q))

# the inner temperature can easy compute once the heat transfer is known:
# but now the resistance tham must be considered is the R1

T_inner=Q*R1+t_inf2
print("the inner temperature is " + str(T_inner))