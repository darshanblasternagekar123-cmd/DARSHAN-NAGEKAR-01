# write a python program to
# a)To accept an integer,Float, String and Bollean
# b)To Display their Value & Data Type
# c)To perform Arithmetic & sring operation

# input section
i=int(input("Enter an integer value:"))
f=float(input("Enter a float value:"))
s=str(input("Enter a string value:"))
b=bool(input("Enter a boolean value (True/False):"))

# output section
print("Integer value & data type is ",i,type(i))
print("Float value & data type is ",f,type(f))
print("String value & data type is ",s,type(s))
print("Boolean value & data type is ",b,type(b))

# output section
print("Integer+Float+",i+f)
print("Integer*2=",i*2)
print("Float/2=",f/2)
print("String+'mite'=",s+'mite')
print("String*2=",s*2)
print("Length of String=",len(s))
print("Boolean value+",b+1)
