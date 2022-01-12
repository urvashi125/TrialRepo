print("Welcome to the love calculator")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_string =name1 + name2
lower_combined_string = combined_string.lower();
count_of_t = lower_combined_string.count("t")
count_of_r = lower_combined_string.count("r")
count_of_u = lower_combined_string.count("u")
count_of_e = lower_combined_string.count("e")

true = count_of_t + count_of_r + count_of_u + count_of_e

count_of_l = lower_combined_string.count("l")
count_of_o = lower_combined_string.count("o")
count_of_v = lower_combined_string.count("v")
count_of_e_love = lower_combined_string.count("e")


love = count_of_l + count_of_o + count_of_v + count_of_e_love

total_percentage = int(str(true) + str(love))

if (total_percentage < 10) or (total_percentage > 90):
    print(f"your score is {total_percentage}  you go together like coke and mentos")
elif 40 < total_percentage < 50:
    # print("your score is " + str(total_percentage) + " you are alright together ")
    print(f"your score is {total_percentage} you are alright together ")
else:
    # print("your score is " + str(total_percentage))
    print(f"your score is {total_percentage}")
