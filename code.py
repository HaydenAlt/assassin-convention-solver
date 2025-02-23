from collections import Counter

words = ['spy', 'fool', 'seer', 'baker', 'bully', 'cupid', 'drunk', 'idiot', 'judge', 'mayor', 'siren', 'witch', 'bandit', 'blight', 'bomber', 'cursed', 'doctor', 'forger', 'gunner', 'jailer', 'lurker', 'medium', 'priest', 'random', 'sister', 'warden', 'zombie', 'analyst', 'avenger', 'butcher', 'flagger', 'gambler', 'sheriff', 'sibling', 'trapper', 'arsonist', 'assassin', 'cannibal', 'conjuror', 'ferryman', 'marksman', 'pacifist', 'preacher', 'red lady', 'sorcerer', 'villager', 'wise man', 'alchemist', 'anarchist', 'aura seer', 'bodyguard', 'corruptor', 'detective', 'locksmith', 'lone wolf', 'loudmouth', 'mortician', 'president', 'rainmaker', 'ritualist', 'tough guy', 'vigilante', 'violinist', 'wolf seer', 'accomplice', 'astronomer', 'gentlewolf', 'ghost lady', 'ghost wolf', 'headhunter', 'instigator', 'jelly wolf', 'journalist', 'soulbinder', 'split wolf', 'storm wolf', 'swamp wolf', 'toxic wolf', 'bell ringer', 'illusionist', 'kitten wolf', 'little girl', 'naughty boy', 'santa claus', 'sect hunter', 'sect leader', 'shadow wolf', 'spirit seer', 'wolf scribe', 'wolf shaman', 'beast hunter', 'doppelganger', 'easter bunny', 'flower child', 'grave robber', 'pumpkin king', 'shapeshifter', 'werewolf fan', 'wolffluencer', 'guardian wolf', 'leprous human', 'mad scientist', 'random killer', 'random voting', 'serial killer', 'wolf pacifist', 'wolf summoner', 'alpha werewolf', 'blind werewolf', 'confusion wolf', 'evil detective', 'fortune teller', 'grumpy grandma', 'night watchman', 'wolf trickster', 'handsome prince', 'junior werewolf', 'random werewolf', 'seer apprentice', 'voodoo werewolf', 'regular werewolf', 'werewolf berserk', 'stubborn werewolf', 'custom random role', 'nightmare werewolf', 'random strong villager', 'random regular villager']
guessed_letters = set()
qwerty = "qwertyuiopasdfghjklzxcvbnm"

print("Note that if the word has a hyphen(-), it is bell-ringer.")

length = int(input("Word Length: "))
words = [word for word in words if len(word) == length]

if len(words) == 1:
    print("Answer found! The word is: ", words[0])
    print("Press letters: "+ ''.join(sorted(set(words[0]) - guessed_letters, key=lambda letter: qwerty.index(letter))))
    input("Press Enter to close...")
    quit()
elif len(words) == 0:
    print("Error! There is no words left in the list!")
    input("Press Enter to close...")
    quit()

spaces = input("Number of spaces: ")
spaces = int(spaces) if spaces else 0
words = [word for word in words if word.count(' ') == spaces]

if len(words) == 1:
    print("Answer found! The word is: ", words[0])
    print("Press letters: "+ ''.join(sorted(set(words[0]) - guessed_letters, key=lambda letter: qwerty.index(letter))))
    input("Press Enter to close...")
    quit()
elif len(words) == 0:
    print("Error! There is no words left in the list!")
    input("Press Enter to close...")
    quit()

if any(' ' in word for word in words):
    first_space_length = int(input("Length from the first character to the first space: "))
    words = [word for word in words if word.find(' ') == first_space_length]

if len(words) == 1:
    print("Answer found! The word is: ", words[0])
    print("Press letters: "+ ''.join(sorted(set(words[0]) - guessed_letters, key=lambda letter: qwerty.index(letter))))
    input("Press Enter to close...")
    quit()
elif len(words) == 0:
    print("Error! There is no words left in the list!")
    input("Press Enter to close...")
    quit()

while len(words) != 1:
    all_letters = ''.join(words)
    letter_count = Counter(all_letters)
    while True:
        most_common_letter, _ = letter_count.most_common(1)[0]
        if most_common_letter not in guessed_letters:
            guessed_letters.add(most_common_letter)
            break
        letter_count.pop(most_common_letter)
    print("Guess:", most_common_letter)
    user_input = input("Where is the letter? (If there is none of that letter, leave blank. If there is 2 of that letter, input any.): ")

    if user_input == "":
        words = [word for word in words if most_common_letter not in word]
    else:
        index = int(user_input) - 1
        words = [word for word in words if len(word) > index and word[index] == most_common_letter]
    
    if len(words) == 0:
        print("Error! There is no words left in the list!")
        input("Press Enter to close...")
        quit()
        
if len(words) == 1:
    print("Answer found! The word is: ", words[0])
    print("Press letters: "+ ''.join(sorted(set(words[0]) - guessed_letters, key=lambda letter: qwerty.index(letter))))
    input("Press Enter to close...")
    quit()
