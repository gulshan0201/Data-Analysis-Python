# lst_1 = [1,2,3,4,5,6]
# lst_2 = [9,8,88,66,87]

# print(lst_2)
# # print(lst_2.append(lst_1[3]))


inp_number = int(input("Enter your number"))

if inp_number % 2 == 0:
    print("The number {} is divisible by 2".format(inp_number))
elif inp_number % 3 == 0:
    print("The no {} is divible by 3".format(inp_number))
elif inp_number % 4 == 0:
    print("The number {} is divisible by 4".format(inp_number))  