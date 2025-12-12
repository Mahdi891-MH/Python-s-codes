import random


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def count_total(scores):
    total = 0
    for i in scores:
        total += i
    return total


want = input("Do you want to play blackjack game (y/n): ").lower()
while want == 'y':
    user_cards = []
    computer_cards = []
    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    if user_cards[0] == 11 and user_cards[1] == 11:
        user_cards[1] = 1
    if computer_cards[0] == 11 and computer_cards[1] == 11:
        computer_cards[1] = 1
    print(f"computer first card is {computer_cards[0]}")
    print(f"your cards are {user_cards}")
    hit_stand = input("Do you want to hit or stand(h/s): ").lower()
    if hit_stand == 'h':
        while hit_stand == 'h':
            hit = deal_card()
            if hit == 11 and (hit+count_total(user_cards)) > 21:
                user_cards.append(1)
            else:
                user_cards.append(deal_card())
            if count_total(user_cards) > 21:
                print(f"your cards are {user_cards}")
                print("You bust!")
                break
            print(f"your cards are {user_cards}")
            hit_stand = input("Do you want to hit or stand(h/s): ").lower()
    if hit_stand == 's':
        print(f"computer's second card is {computer_cards[1]}")
        while count_total(computer_cards) < 17:
            hit = deal_card()
            if hit == 11 and (hit+count_total(computer_cards)) > 21:
                computer_cards.append(1)
            else:
                computer_cards.append(deal_card())
            print(f"computer hit one card now computer cards are {computer_cards}")
        if count_total(computer_cards) >= 17:
            if count_total(computer_cards) > 21:
                print("computer bust! you win")
            else:
                if count_total(computer_cards) > count_total(user_cards):
                    print("You lose!")
                elif count_total(computer_cards) == count_total(user_cards):
                    print("Draw! computer and you are equal")
                else:
                    print("You win")
    want = input("Do you want to play blackjack game (y/n): ").lower()