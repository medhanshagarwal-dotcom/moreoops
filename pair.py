class Par_elements:
    def twosum(self, num, target):
        lookup={}
        for i,n in enumerate(num):
            if target-n in lookup:
                return(lookup[target-n],i)
            lookup[n]=i

value=int(input("Enter a the sum of two numbers you want(multiple of 10): "))
print("index1=%d , index2=%d" % Par_elements().twosum((10,20,30,40,50,60),value))
