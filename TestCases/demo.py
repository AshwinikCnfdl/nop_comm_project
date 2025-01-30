s = "aaaabbbbcccc"
print(s.count("a")) #  4
print(s.count("a",4)) # 0

name = "Rushath"
print(name.count("a"))

s = "hello i am python"
print(s.split()) #['hello', 'i', 'am', 'python']
print(s.split("h")) #['', 'ello i am pyt', 'on']
print(s.split("h",1)) #['', 'ello i am python']

# wap to print how many word present in the String
# sparete the data,mm,yyyy dob = "15-02-2024"

s = "hello i am python hello i am java"
words = s.split() #['hello', 'i', 'am', 'python']
print(len(words))
print(s.count(" "))
dob = "15-02-2024"
dd,mm,yyyy = dob.split("-") #[15,02,2024]
print(dd,mm,yyyy)

# join method:-- it return the String it joins each char with wich char u passed
# "-".join(iterable)

s = "hello"
print("&".join(s))

#wap to convert IND date formate to US Date Formate
#29-01-2024  :--- convert 2024-01-29

In = "29-01-2024"
split_IN = In.split("-") # [29 , 01 ,2024]
split_Us = split_IN[::-1] #[2024,01,29]
us =  "-".join(split_Us) # 2024-01-29
print(us)