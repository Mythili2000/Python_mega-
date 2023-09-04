'''How to remove an item from a list'''

while True:
    bag = input("Enter your item in to put in bag:")
    hand_bag = []
    hand_bag.append(bag)
    print(hand_bag)
    prompts = input("choose to remove an item remove:")
    if prompts == 'remove':
        item = input("Enter an item you want to remove:")
        hand_bag.remove(item)
        print(hand_bag)
