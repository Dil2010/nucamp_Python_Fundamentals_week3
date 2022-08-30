import random


diamonds = ["AD", "2D", "3D", "4D", "5D", "6D",
            "7D", "8D", "9D", "10D", "JD", "QD", "KD"]
hand = []

while diamonds:
    answer=input("Please enter to pick a card, or Q then enter quit?")
    if answer=="Q" or answer=="q":
        diamonds=[]
    if answer=="":
        random.shuffle(diamonds)
        new_card=diamonds.pop()
        hand.append(new_card)
        print("Your hand",hand)
        if(len(diamonds)>0):
            print("Remaining Cards",diamonds)
        else:
            print("There are no more cards to pick")


