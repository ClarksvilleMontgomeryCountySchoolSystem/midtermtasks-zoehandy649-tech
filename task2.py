#AFTER PASTING YOUR ANSWER YOU MUST REMOVE THE LINE "import s"
#YOUR CODE WILL FAIL IF YOU DO NOT DELETE THE LINE!!!!!!!!!!!!!

# Given variables
allowance = 15
dishes, room, trash, lawn, laundry, vacuum = 3, 5, 2, 8, 4, 6
candy, soda, game, movie, toy, snack = 4, 2, 15, 10, 7, 3

balance = allowance
# Week 1: You took out the trash and cleaned your room
balance += trash
a1 = balance
balance += room
a2 = balance
# You bought soda
balance -= soda
a3 = balance
# Week 2: Parents gave you a bonus! They doubled your allowance for working hard
balance *= 2
a4 = balance
# You did the laundry
balance += laundry
a5 = balance
# You bought a new movie
balance -= movie
a6 = balance
# Week 3: You decided to put a fourth of your money in savings
balance /= 4
a7 = balance
# Print final allowance
print1 = f"Allowance: ${balance}"
