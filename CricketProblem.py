n=int(input("Enter the input length: "))
arr=[]
sum=0
for i in range(n):
    arr.append(int(input("Enter non-zero price: ")))

#padding the list for loop viability
arr.extend([0,0,0,0,0])
#keeps track of third element with respect to first element
k=0
#keeps track of counts in the set created by the limiting variable 'k'
i=y=0
while i<n:
    print("START INDEX : ",i)
    if i!=k+2:
        #This case deals where n(elements)={0,1}
        if y!=2:
            m=max(arr[i]+arr[i+1]+arr[i+3],arr[i]+arr[i+2]+arr[i+3])
            j=max(arr[i+1]+arr[i+2]+arr[i+4],arr[i+1]+arr[i+3]+arr[i+4])
            i= i if m>=j else (i+1)
            sum+=arr[i]
            y=1 if (i==k+2) else (y+1)
            if y==1: k=i

        #The else case deals with scenario where we have already selected 1 element and we can choose either 2nd or third element         
        else:
            m=max(arr[i]+arr[i+2]+arr[i+3],arr[i]+arr[i+2]+arr[i+4])
            j=max(arr[i+2]+arr[i+3]+arr[i+5],arr[i+2]+arr[i+4]+arr[i+5])
            i=i if m>=j else (i+2)
            sum+=arr[i]
            y=0 if i==k+2 else y+1
            if y==1 :
                k=i
            print("ELSE CASE EXECUTED, INDEX IS ",i)

        print("index:",i,"element",arr[i],"Tracker",k)

    #The else will not add third element but update the tracker's position and reset the counter 
    else:
        y=0

    print("Counter:",y)
    i+=1

print("The maximum price is:",sum)