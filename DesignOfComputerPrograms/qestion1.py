# about A poker problem
# card rank and suit
# poker(hands) -> best hand
# hand rank 
# n-kind straight flush 

def poker(hands):
    'Return the best hand: poker([hand,...]) => hand'
    return max(hands, key=hand_rank)

def hand_rank(hand):
    return ???
