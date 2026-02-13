user_input = input("Enter something: ")
reverse = ""

for ch in user_input:
    reverse = ch + reverse

print("Reversed output:", reverse)

##################################################
#Slicing sequence[start : stop : step]
text = "ABC"
print(text[::-1])
##################################################
num = int(input("Enter the number "))
reverse_num=0

while num > 0:
    digit=num%10
    reverse_num=reverse_num * 10 + digit
    num = num // 10

print ("Reversed number:", reverse_num)
#####################################################
num= int(input("put a number"))
reverse_num=0
for _ in range(len(str(num))):
    digit= num % 10
    reverse_num= reverse_num * 10 + digit
    num = num // 10

print ("Reversed no:", reverse_num)