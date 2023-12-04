import random
from replit import clear
from art import logo


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards_score):
    if sum(cards_score) == 21 and len(cards_score) == 2:
        return 0

    if 11 in cards_score and sum(cards_score) > 21:
        cards_score.remove(11)
        cards_score.append(1)
    return sum(cards_score)


def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return f"{name} lose"

    if user_score == computer_score:
        return "Draw"

    elif user_score == 0:
        return f"{name} has a Blackjack. User win."

    elif computer_score == 0:
        return "Dealer has a Blackjack. Dealer win."

    elif user_score > 21:
        return f"{name} lose. Dealer winner"

    elif computer_score > 21:
        return f"{name} winner"

    elif user_score > computer_score:
        return f"{name} winner"

    else:
        return f"{name} lose. Dealer winner. "


def play_game():
    print(logo)

    user_card = []
    computer_card = []
    game_finish = False

    for choose in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())

    while not game_finish:
        user_score = calculate_score(user_card)
        computer_score = calculate_score(computer_card)
        print(f"{name}'s cards : {user_card} and score : {user_score} ")
        print(f"Dealer first card : {computer_card[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_finish = True

        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_card.append(deal_card())
            else:
                game_finish = True

    while computer_score != 0 and computer_score < 17:
        computer_card.append(deal_card())
        computer_score = calculate_score(computer_card)
    print(f"{name} final card: {user_card} and score : {user_score}")
    print(f"Computer final card : {computer_card} and score : {computer_score}")
    print(compare(user_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    name = input("What is your name ? ")
    clear()
    play_game()






