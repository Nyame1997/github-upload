import bjclass
import bjfunctions

if __name__ == '__main__':

	while True:
		print("Welcome to BlackJack! Get as close to 21 as you can without going over!")
		print("Dealer hits until she reaches 17/ Aces count as 1 or 11.")

		deck = bjclass.Deck()
		deck.shuffle()

		player_hand = bjclass.Hand()
		player_hand.add_card(deck.deal())
		player_hand.add_card(deck.deal())

		dealer_hand = bjclass.Hand()
		dealer_hand.add_card(deck.deal())
		dealer_hand.add_card(deck.deal())

		player_chips = bjclass.Chips()

		bjfunctions.take_bet(player_chips)

		bjfunctions.show_some(player_hand, dealer_hand)

		playing = True

		while playing:

			bjfunctions.hit_or_stand(deck, player_hand)

			bjfunctions.show_some(player_hand, dealer_hand)

			if player_hand.value > 21:
				bjfunctions.player_busts(player_hand, dealer_hand, player_chips)
				break

		if player_hand.value <= 21:

			while dealer_hand.value < 17:
				bjfunctions.hit(deck, dealer_hand)

			bjfunctions.show_all(player_hand, dealer_hand)

			if dealer_hand.value > 21:
				bjfunctions.dealer_busts(player_hand, dealer_hand, player_chips)

			elif dealer_hand.value > player_hand.value:
				bjfunctions.dealer_wins(player_hand, dealer_hand, player_chips)

			elif dealer_hand < player_hand.value:
				bjfunctions.player_wins(player_hand, dealer_hand, player_chips)

			else: bjfunctions.push(player_hand,dealer_hand)

		print("\nPlayer's winnings stand at: ", player_chips.total)

		new_game = input("Would you like to play another hand? Enter 'y' or 'n': ")

		if new_game[0].lower() == 'y':
			playing = True
			continue

		else:
			print("Thanks for playing!")
			break


