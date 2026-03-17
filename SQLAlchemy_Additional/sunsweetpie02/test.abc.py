########################################################################################
# test_linguist.py
from Abcd import *


def run_tests():
    """
    Run full test for Linguist application.
    Tests user, deck, card creation, updates, filtering, and assertions.
    """
    user1 = user_create("Siuzanna", "sunsweetpie02@gmail.com", "q232")
    print(f"User created: {user1.name} | {user1.email}")

    deck1 = deck_create("English fundamentals", user1.id)
    print(f"Deck created: {deck1.name}")

    card1 = card_create(user1.id, "Polymorphism", "Поліморфізм", "One interface, many forms")
    print(f"Card created: {card1.word} → {card1.translation}")

    user_update_name(user1.id, "Siuzanna Pyrohova")
    updated_user = user_get_by_id(user1.id)
    print(f"Updated name: {updated_user.name}")

    filtered_cards = card_filter("interface")
    print("Filtered cards:", [(c.word, c.translation) for c in filtered_cards])

    assert updated_user.name == "Siuzanna Pyrohova", "User name update failed"
    assert deck1.name == "English fundamentals", "Deck name incorrect"
    assert card1.word == "Polymorphism", "Card word incorrect"
    assert len(filtered_cards) > 0, "Filter did not return cards"

    print("All tests passed successfully")

if __name__ == "__main__":
    run_tests()

#########################################################################################