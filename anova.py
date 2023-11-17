#Anova
a=[10,9,7.5,8.5,9,10,8,8,9]
b=[8,9,10,8,8,5,7,9.5,9,7,10]
c=[9,8,7,10,9,8,7,10,9,8]
#null hypothesis there is no significance
#anova formula
#anova=variance between/variance within
#to calculate variance between sum of all columns [len(each column)*[mean( of column)-(mean of all columns)]]
x_a=sum(a)/len(a)
x_b=sum(b)/len(b)
x_c=sum(c)/len(c)

mu=(x_a+x_b+x_c)/3

va=len(a)*(x_a-mu)
vb=len(b)*(x_b-mu)
vc=len(c)*(x_c-mu)

var_bet=va+vb+vc
print("Variance between: ",var_bet)
#variance within
sum1=0
sum2=0
sum3=0

for i in a:
    sum1=sum1+((i-x_a)**2)

for i in b:
    sum2=sum2+((i-x_b)**2)

for i in c:
     sum3=sum3+((i-x_c)**2)

var_within=sum1+sum2+sum3
print("Variance within: ",var_within)
anova=var_bet/var_within
print("Anova value: ",anova)
if(anova<1):
    print("Accept the null hypothesis")
else:
    print("Reject the null hypothesis")