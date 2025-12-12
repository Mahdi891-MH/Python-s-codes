import random

data = [{'name': 'Instagram', 'follower_count': 346, 'description': 'Social media platform', 'country': 'United State'},
        {'name': 'Cristiano Ronaldo', 'follower_count': 215, 'description': 'footballer', 'country': 'Portugal'},
        {'name': 'Ariana Grande', 'follower_count': 183, 'description': 'Musician and actress', 'country': 'United State'},
        {'name': 'Dwayne Johnson', 'follower_count': 181, 'description': 'actor and professional wrestler', 'country': 'United State'},
        {'name': 'Selena Gomez', 'follower_count': 174, 'description': 'musician and actress', 'country': 'United Stated'},
        {'name': 'Kylie Jenner', 'follower_count': 172, 'description': 'Reality TV personality and businesswomen and self_made billioner', 'country': 'United State'},
        {'name': 'Kim Kardashian', 'follower_count': 167, 'description': 'Reality TV personality', 'country': 'United State'}
        ]


def randomly_choose(challenger):
    competitor = random.choice(challenger)
    return competitor


def compare(com1, com2):
    print(f"compare A: {com1['name']}, {com1['description']}, from {com1['country']}")
    print(f"against B: {com2['name']}, {com2['description']}, from {com2['country']}")
    if com1['follower_count'] > com2['follower_count']:
        return 'A'
    elif com2['follower_count'] > com1['follower_count']:
        return 'B'


competitor1 = randomly_choose(data)
competitor2 = randomly_choose(data)

score = 0

while True:
    winner = compare(competitor1, competitor2)
    user_choice = input("Who has more follower? type 'A' or 'B': ").capitalize()
    if user_choice == winner:
        score += 1
        print(f"You are right! current score is {score}")
    else:
        print("Sorry that is wrong!")
        print(f"your score {score}")
        break
    competitor1 = competitor2
    competitor2 = randomly_choose(data)
    while competitor1 == competitor2:
        competitor2 = randomly_choose(data)
    print()
