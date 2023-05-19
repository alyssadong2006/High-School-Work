import csv
import random
import time

"""
ideas:

-adding data
    -interesting idea
    -doesn't overuse already written code

-multiple filters
    -meh, kind of boring
    -kind of repeats already written code

-asking questions of characters?
    -more advanced, fun? i think
    -now that I've written the code, it's kind of confusing with all the lists, but it works

-Search bar, searching by letters, updates every new letter you type in??
    -meh, good idea but it'll be too messy to update the lists shown everytime
    -plus, it can't really automatically update since you need to manually press enter after every input

"""


def generate_list_characters(filename):

    main_list = []

    file_in = open(filename, encoding='UTF-8', errors='replace')

    file_in.readline()
    file_in = csv.reader(file_in)

    for line in file_in:
        if line[1] != "":
            line[1] = line[1].split(";")
        if line[2] != "":
            line[2] = line[2].split(";")
        
        
        
        
        main_list.append(line)

    return main_list


def print_menu(menu_list):

    print("\n"*5)
    for i in range(0, len(menu_list)):
        print(f'{i+1}. {menu_list[i]}')


def get_menu_selection(menu_list):

    possible_choice_values = []
    for i in range(0, len(menu_list)):
        possible_choice_values.append(str(i+1))

    choice = input("Type number to choose ... ")

    while choice not in possible_choice_values:
        print("Incorrect selection")
        print("\n"*30)
        
        print_menu(menu_list)
        choice = input("Type number to choose ...")

    return int(choice)


def get_all_possible_clans(list_of_characters): #getting information

    clans = []
    
    for character in list_of_characters:
        if character[5].strip() not in clans:
            clans.append(character[5].strip())

    clans.sort()
    return clans


def print_clans(list_clans):

    print("\n\nAll clans available are:")
    print("-"*20)

    for item in list_clans:
        print(f'{item:<30}')
    
    print("\n") 


def get_valid_clan(list_clans):

    clan = input("What clan would you like to filter for?")
    while clan not in list_clans:
        clan = input("Sorry that clan name is not valid. Please try again")
    
    return clan


def filter_all_listings(list_of_characters, clan):

    sub_list = []

    for item in list_of_characters:
        if clan in item[5]:
            sub_list.append(item)

    return sub_list



def get_valid_listing(list_characters):

    possible_choice_values = []
    for i in range(0, len(list_characters)):
        possible_choice_values.append(str(i+1))
    
    choice = input("Which listing would you like to choose?")

    while choice not in (possible_choice_values):
        choice = input("Invalid choice. Try another number")

    choice = int(choice) - 1

    return list_characters[choice]



def print_listings_table(list_characters):

    for i in range(0, len(list_characters)):
        character = list_characters[i]
        s = f"{i+1:<3} {character[0]:<30}"
        print(s)


def print_character_details(some_char):
    #gets user to input new character details
    s = "______________________________________\n"
    s += some_char[0]
    if some_char[5] != "":
        s+=f" is from clan {some_char[5]}"
    s+="\n"
    s+= f"\nSex:{some_char[3]}\n"
    if len(some_char[1])>=1:
        s+= '\nPractices Jutsu(s):\n'
        for jutsu in some_char[1]:
            s+= jutsu+"\n"
    if len(some_char[2])>=1:
        s+= f"\nAppears in:\n"
        for appear in some_char[2]:
            s+= appear +"\n"
    if some_char[4] != "":
        s += f"\nClassified as a {some_char[4]}\n"
    if some_char[6] != "":
        s+=f"\nUses the tool {some_char[6]}\n"
    if some_char[7] != "":
        s+=f"\nOccupation:{some_char[7]}\n"
    if some_char[8] != "":
        s+=f"\nTeam:{some_char[8]}\n"
    if some_char[9] != "":
        s+=f"\nAffiliation:{some_char[9]}\n"
    if some_char[10] != "":
        s+=f"\nNature Type:{some_char[10]}\n"
    if some_char[11] != "":
        s+=f"\nPhoto Link:{some_char[11]}\n"
    
    s+=f"\n"
        
    print(s)

def trivia(characters_info):
    #generates question and gets answer
    exist = False

    #if the trait does not exists, it continues generating new questions until the random trait in the random character exists
    while exist == False:
        value = random.randint(0,len(characters_info)-1)
        types = [["Jutsu",1], ["appears in",2], ["sex",3], ["classification",4], ["clan",5], ["tools",6], ["occupation",7], ["team",8], ["affiliation",9], ["nature type",10]]
        #q_word stands for question word
        q_word = random.choices(types)
        q_word_edit = q_word[0][0]
        if not characters_info[value][q_word[0][1]] == '':
            exist = True

    
    #prints answer for testing, upper/lower case does not matter
    #print(characters_info[value][q_word[0][1]])
    

    answer = str(input(f'{characters_info[value][0]}\'s {q_word_edit} (Write one)? '))

    #answer is correct as long as it exists in the list, upper/lower case does not matter.
    if answer != '':
        if isinstance(characters_info[value][q_word[0][1]], list):
            check = False
            print()
            endRange = len(characters_info[value][q_word[0][1]])
            for choices in range(0,endRange):
                if answer.lower() == characters_info[value][q_word[0][1]][choices].lower():
                    check = True
            if check == True:
                print("Correct!")
            else:
                print("Wrong!")
        elif answer.lower() == characters_info[value][q_word[0][1]].lower():
            print("Correct!")
        else:
            print("Wrong!")
    else:
        print("Wrong!")

    time.sleep(1)

    #prints the character's information
    print(f'\n\n\nCharacter Info:')
    print_character_details(characters_info[value])


def add_char(existing_list):
    new_list = []

    nameCheck = False

    while nameCheck == False:
    #new character name
        name = str(input("New Character Name: "))
        if name != "":
            nameCheck = True
    new_list.append(name)

    #new character jutsu
    jutsu = str(input("Character's jutsu's (format: a,b,c,): "))
    jutsu_list = []
    start = 0
    for i in range (len(jutsu)):
        if jutsu[i] == ",":
            jutsu_list.append(jutsu[start:i])
            start = int(i+1)
    new_list.append(jutsu_list)

    #new character appearence
    appear = str(input("Charater appears in (format:a,b,c,): "))
    appear_list = []
    start = 0
    for i in range (len(appear)):
        if appear[i] == ",":
            appear_list.append(appear[start:i])
            start = int(i+1)
    new_list.append(appear_list)

    #new character sex
    sex = str(input("Character sex: "))
    new_list.append(sex)

    #new character classification
    classification = str(input("Character classification: "))
    new_list.append(classification)

    #new character clan
    clan = str(input("Character clan: "))
    new_list.append(clan)

    #new character tools
    tools = str(input("Character tools: "))
    new_list.append(tools)

    #new character occupation
    occ = str(input("Character occupation: "))
    new_list.append(occ)

    #new character team
    team = str(input("Character team: "))
    new_list.append(team)

    #new character affiliation
    aff = str(input("Character affiliation: "))
    new_list.append(aff)

    #new character nature type
    nat = str(input("Character nature type: "))
    new_list.append(nat)

    #new character photo
    photo = str(input("Character photo link: "))
    new_list.append(photo)
    
    existing_list.append(new_list)

def delete_data(characterList):
    print_listings_table(characterList)
    exist_num = False
    
    while exist_num == False:
        try:
            delete_num = int(input("Please type in the number of the character you want to delete: "))
            if delete_num != '' and delete_num <= len(characterList):
                delete_num -= 1
                print(f'\n\nYou have deleted the character {characterList[delete_num][0]}')
                characterList.pop(delete_num)
                exist_num = True
            else:
                print("Invalid value")
        except ValueError:
            print("Invalid Value")

def game(char_data):
    
    print(f'Create Your Character:')
    value = False
    
    while value == False:
        playerOne = input(f'Please Input a name. Enter \'help\' to see character list: ')
        
        if playerOne.lower() == 'help':
            print_listings_table(char_data)
        else:
            for char in char_data:
                if isinstance(playerOne, str) and playerOne.lower() == char[0].lower():
                    print(f'You have chosen {char[0]}')
                    value = True
                    story(char[0])

                
def story(char):
    continue_ = True
    while continue_ == True:
        power = random.randint(0,100)

        if power < 50:
            stories = [f"{char} stepped out of the village and was assasinated", f"{char} participated in a Ninja War and died with honor", f"{char} died, but system doesn't know why"]
        elif power >= 50 and power < 90:
            stories = [f'{char} lived a peaceful life in the village and died due to old age', f'Despite {char} being a powerful ninja, {char} decides to keep his/her power as a secret and lives a hidden life in the mountains.']
        else:
            stories = [f'{char} was bullied at a young age, which led to {char}\'s distorted personality and determination to become stronger. Eventually, {char} took over the world and killed all those who used to disrespect him/her', f'{char} was a powerful ninja who reigned over the different villages. One day, he/she came across a boy with a hero-like personality named Naruto. Naruto accused {char} of using violence on innocent people. {char} was killed']

        event = random.choice(stories)
        print(f'------------------\n{event}\n------------------')
        cont = str(input(f'Type \'exit\' to exit game, type anything else to continue\nYour choice:'))
        if cont.lower() == 'exit':
            continue_ = False
    
def verify(current_list):
    original_list = generate_list_characters("naruto_data.csv")
    if current_list == original_list:
        print("Your file has not been modified before.")
    else:
        print("Your file has been modified before.")
        Reset = input(f"Do you want to recover your original data?\nEnter 'Yes' to reset.")
        if isinstance(Reset, str) and Reset.lower() == 'yes':
            return True

def main():
    main_character_list = generate_list_characters("naruto_data.csv")
    
    all_clans = get_all_possible_clans(main_character_list)

    menu_items = ['See All Listings', 'Find character by Clan', 'Trivia', 'Add Character', 'Delete Character (Extra)','Mini story (Extra)','Verify File Integrity (Extra)', 'Lol (Don\'t mark this)',  'Exit']
    
    print_menu(menu_items)
    choice = get_menu_selection(menu_items)
    
    while 0 < choice and choice < len(menu_items):
        
        #restates what all_clans is so the possible clans refresh and show added custom clans
        all_clans = get_all_possible_clans(main_character_list)
        
        ##See all listings
        if choice == 1:
            print_listings_table(main_character_list)

        #Find listing by Clan
        elif choice == 2:
            
            print_clans(all_clans)
            clan = get_valid_clan(all_clans)

            sub_list_clans = filter_all_listings(main_character_list, clan)
            print_listings_table(sub_list_clans)

            current_character = get_valid_listing(sub_list_clans)
            
            print_character_details(current_character)

        #Trivia
        elif choice == 3:
            trivia(main_character_list)

        #Add Data to the main_character_list
        elif choice == 4:
            add_char(main_character_list)

        elif choice == 5:
            delete_data(main_character_list)

        elif choice == 6:
            game(main_character_list)

        elif choice == 7:
            if verify(main_character_list) == True:
                main_character_list = generate_list_characters("naruto_data.csv")
            

        elif choice == 8:
        #don't mark choice 8, it's just for fun.
            print(f'\n\n\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣞⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠑⠲⢤⣀⡀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠓⠦⣄⡀⠀⠀⠀\n ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠋⠀⠀⠀⠀⠀⢀⠀⠀⠀⠰⡀⠀⠀⠀⣀⣀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠠⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠴⠛⠁⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⣀⠔⠉⠀⠀⠀⠀⠀⠀⠀⠀⢳⣆⡀⠀⠙⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣤⣻⡀⠀⠀⠀⠀⠀⣦⠀⠀⠀⠀⠀⣠⡴⠒⠉⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⣠⠞⠁⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣦⣀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⣿⠀⠀⠀⠀⢀⡙⢦⡀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠺⠓⠊⠉⠉⣲⠀⠈⡇⠀⠀⠀⠀⠀⣿⣿⡉⠉⠉⠑⠦⣳⡄⠀⠀⠉⠉⠉⠉⠛⠻⠿⠿⣿⣿⣿⣿⡄⠀⠀⠀⣿⠀⠀⠀⠀⠀⢻⠲⠿⣆⡀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠏⠀⣴⣿⡄⠀⠀⠀⢀⡏⠛⠃⠀⠀⠀⠀⠀⠙⠀⣠⡤⣤⣀⣠⠦⠀⠀⠀⠀⠀⣍⠻⣿⣄⠀⠀⢻⠀⠀⠀⠀⠀⠀⢇⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⡸⠀⣼⣿⣿⣷⡀⠀⠀⢸⣇⠀⠀⠀⠀⠠⠄⠀⣰⡟⢉⣤⣤⡉⠁⠀⠀⠀⠀⠤⠀⠙⠁⢹⣿⣆⠀⢸⣧⡀⠀⠀⠀⠀⠸⡆⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⢰⡇⣴⣿⣿⣿⣿⣧⡀⠀⢘⡟⠁⠀⠀⠀⠀⢀⡾⢻⡄⠸⣤⣌⣿⠀⠀⠀⠀⡄⠀⠀⣤⠀⣿⣿⣿⣆⢸⣿⣿⣦⡀⠀⠀⠀⢹⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⣾⡜⢹⣿⣿⣿⣿⣿⣷⡀⠐⣧⡀⠀⢀⣴⠀⠈⠙⠲⠿⠶⠴⠾⠋⠀⠀⠐⠺⠆⠀⠀⠈⠀⣿⣿⣿⣿⣾⣿⣿⣿⣟⢦⡀⠀⠀⣇⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠟⠁⢸⣿⣿⣿⣿⣿⣿⣷⡄⣟⣁⣀⣀⣠⣤⣤⣤⣤⣤⣄⣀⣀⣀⣀⣀⣀⠀⠀⠀⣴⡖⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⢹⢦⡀⢸⡄⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⢦⣸⠀⠙⢦⣧⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢼⣿⣿⡿⢻⡏⠉⠉⠈⠙⠲⢬⣗⡦⣄⠀⠀⠀⣠⠄⠀⠀⣹⠉⠉⢉⣟⣿⠟⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣆⣀⣠⣽⣦⣤⣤⣴⣶⣶\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⡛⡄⠀⣸⠀⠀⣴⠞⢻⡽⢿⣾⣍⢾⣿⣦⠞⠁⠀⠀⠀⢿⣤⣶⡾⢛⣾⣿⣷⠶⣄⡀⠈⠉⢹⠙⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣇⣷⣿⠀⣿⠀⠀⢿⡄⢿⡴⢆⡷⠹⣎⢻⠅⠀⠀⠀⠀⢀⣴⣿⠏⣴⠏⣾⢰⠎⣳⢀⣿⠂⠀⢸⠀⠀⣾⣹⡟⢹⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡏⢱⣿⡇⡟⠀⠀⠈⠳⢤⣉⣉⣤⡤⠟⠀⠀⠀⠀⠀⠀⣼⡿⠁⠀⠻⣄⣉⣓⣚⣣⡾⠃⠀⠀⢸⠀⢸⣿⠻⠃⡟⢿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣇⣿⡿⢻⡇⠀⠀⠀⠀⣀⣀⡤⠀⠀⠀⠀⠀⠀⠀⠀⢀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⢰⢿⣿⡀⣰⠃⠈⢻⣿⣷⡀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⢿⣷⡈⠃⣠⠤⠒⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⢠⡄⠰⢤⣀⠀⠀⠀⠀⢸⣿⣿⢟⣵⠏⠀⠀⠸⣿⣿⣷⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣦⠉⠙⣇⠀⠀⠀⠀⢀⣤⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢲⢤⡀⠀⠌⠙⠲⢤⡀⡼⠋⠁⣹⠋⠀⠀⠀⠀⢻⣿⣿⣄⡀⠀⣀⣀⣀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢦⠀⣿⠀⢀⡤⠞⠉⠀⠀⠀⠀⠀⠀⢀⣤⣀⢀⣀⣀⡀⠀⠀⠀⠈⠀⠈⠳⢆⡀⠀⠀⢙⣧⣀⡞⡇⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⡿⣿\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣈⣻⣹⣦⣉⣤⣤⣤⣾⣄⠀⠀⠀⠀⠈⠻⣽⣵⣟⡿⠃⠀⠀⠀⠀⠀⢧⡀⠀⠙⢦⣠⠟⢀⡿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⡇⠀⠀⠀⠀⠀⠈⠛⠋⡀⢀⣀⠀⢤⡀⠀⠀⠙⢆⠀⢠⡟⠀⣸⡁⢸⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣿⣦⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠲⠶⣶⣉⣉⣉⣉⣉⢉⣉⣭⠭⠟⠛⠀⠀⠀⠈⢳⡟⣶⠋⢸⣿⣿⣿⣿⣶⣶⣤⠀⠀⠀⠀⠀⠀⠈⠻⢿⡄\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⣰⡏⣹⣿⣧⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⡿⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⢞⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡽⠁⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣧⡉⡳⢦⣀⣀⠀⠀⠀⠀⣀⣠⣴⣾⢟⣵⣿⣿⣺⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠃⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠊⠀⠀⠈⠉⢟⡿⣻⣿⢿⣿⣽⡷⣿⣿⢞⡵⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡎⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⢾⠂⠀⢀⢴⢵⡿⣺⢟⣷⡷⣻⣾⣾⢟⣵⠋⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡞⠁⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⢀⣀⣠⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢄⣶⣿⣷⡊⢘⢼⡵⣫⣠⢾⣝⡷⡻⠃⠀⠘⣯⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣷⣤⡀⠀⠀⠀⠀⠀⠀⠀\n⣀⣤⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠔⢹⠃⠈⠳⣞⡿⢻⠞⣵⣫⣫⡾⠁⠀⠀⠀⣸⡿⢙⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣽⣿⣿⣿⣷⣤⣀\n\n私はナルトです!!!......')
            

        print_menu(menu_items)
        choice = get_menu_selection(menu_items)
        

    print("\n\nGood bye!")

main()
