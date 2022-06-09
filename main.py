groups = int(input())
members = input()


member_list = members.split()

for i in member_list:
    number = int(i)
    if number <= 3:
        print("*" * number)
    else:
        print("*")
        