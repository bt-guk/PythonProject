"""
In Java

    for(int i = 0; i < 5; i++;){
    some code here
    }
"""

for i in range(0, 6): # 6 is excluded
    print(i)

print("========================")

s = "Selenium"

for each in s:
    print(each)
print("==========reverse==============")
reversed_string = ''

for i in s[::-1]:
    reversed_string += i
print(reversed_string)


print("===========Nested Loop=============")

for i in range(1, 5):
    for x in range(1, 5):
        print(f'Hello World')

print("===========while loop=============")

# while True:
#     print("While true printing")
#     break

score = int(input("Enter your score: \n"))

while score > 100 or score < 0:
    score = int(input(f' Score must be in between 0 to 100. Please enter valid score\n'))
if score >= 50:
    print(f'Passed exam with score of {score}')
else:
    print(f'failed exam with score of {score}')