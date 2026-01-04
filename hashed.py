import hashlib
print("Iam The Alpha ")

print("Iam The Omega")

print("Iam The first and")

print ("Iam the Last ")

print ("<-------Signup Now-------->")

u_name=input("Enter Your User Name :")
my_password=input("enter the password:")

hashed_password = hashlib.sha256(my_password.encode()).hexdigest()

f = open("logs.txt","a")
f.write(u_name + "," + hashed_password + "\n")
f.close()

print("--------------------Mission SuccesFull-----------------")

