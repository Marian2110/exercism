"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """

    return [number + i for i in range(3)]


def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """

    return rounds_1 + rounds_2


def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """

    return number in rounds


def card_average(hand):
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """

    return sum(hand) / len(hand)


def approx_average_is_average(hand):
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average.

    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """

    first_card = hand[0]
    last_card = hand[-1]

    first_last_average = sum([first_card, last_card]) / 2
    middle_card = hand[len(hand) // 2]

    true_average = card_average(hand)
    
    return true_average == first_last_average or true_average == middle_card


def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """

    even_indexed_cards = hand[::2]
    odd_indexed_cards = hand[1::2]
    even_indexed_average = calculate_average(even_indexed_cards)
    odd_indexed_average = calculate_average(odd_indexed_cards)

    return even_indexed_average == odd_indexed_average

def calculate_average(cards):
    return sum(cards) / len(cards) if cards else 0


def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """

    if hand and hand[-1] == 11:
        return hand[:-1] + [hand[-1] * 2]
    return hand
    