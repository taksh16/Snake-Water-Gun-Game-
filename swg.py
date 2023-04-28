import random

print('Welcome to Snake-Water-Gun Game')
rounds = int(input('Enter number of rounds: '))
choices = {'g':'s', 's':'w', 'w':'g'}
p_score = c_score = 0
for i in range(1, rounds+1):
    p = input("Choose s for Snake, w for Water, g for Gun: ").strip()
    if p not in choices:
        print("Invalid input, try again\n")
        continue
    c = random.choice(list(choices.keys()))
    print(f'You choose:  {p}, \n  computer choose:  {c}')
    if choices[c] == p:
        c_score += 1
    elif choices[p] == c:
        p_score += 1
    else:
        print(f"\t Round {i} is Draw")
    print(f'Your score in round {i} is : {p_score}')
    print(f'Computer score in round {i} is : {c_score}')

print(f'Your final score is : {p_score}')
print(f'Computer final score is : {c_score}')
if p_score > c_score:
    print("Congratulations!! You Won")
elif c_score > p_score:
    print("You lose!!")
else:
    print("Match Draw!!")

