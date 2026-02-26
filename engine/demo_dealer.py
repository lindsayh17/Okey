from engine.dealer import Dealer



def main():
    dealer = Dealer()
    board = dealer.deal_new_round(['Alice', 'Bob', 'Alex', 'Jane'], starting_player_idx=0)

    print("Player Hands: \n")

    print("-------------------------")
    for i in range(len(board.players)):

        player = board.players[i]
        hand_size = len(player.hand)

        print("Player index:", i)
        print("Name:", player.name)
        print("Number of tiles in hand:", hand_size)
        print("-------------------------")

    print("Tiles remaining in draw pile:", board.draw_pile.count())

if __name__ == "__main__":
    main()
