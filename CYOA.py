"""
This game continue endlessly as you play as an overworked student, it does not end until your mental reaches a certain value.
One round has two semi-rounds.
You will be asked if you want to continue the game after one whole round, in other words, two semi-rounds.

Aside from including classes, and try:...except ValueErrors:..., it still follows the general structures.
A function is called within the function to repeat itself instead of using a while loops.
Due to the addition of classes, instead of just calling the function, for example: start(), one must include the class name: game.start().

Global variables are not declared at the start of functions due to all the variable being in the __init__ function,
which initializes all the variable, making it global within all the functions within the class.
Therefore, instead of: global x; x += 100. One uses: self.x += 100.

Additionally, try using Ctrl+C to forcefully interrupt code,
typing in multiple invalid values muiltiple times
or achieve a random ending by just spamming 1 or something
"""

import random
import time

mark_list = []
#list of random names
names = ['Bob', 'Pop', 'Sob', 'Rob', 'Mob', 'Dob', 'Wob', 'Hob', 'Job', 'Lob', 'Cob', 'Tob', 'Oob']

class Game:
    
    #controls the round numbers, the switch between semi-round one and two in a whole round
    def __init__(self, x = 0, y = 0, mental = 0, mark = 100, miss = False, choose_question = True, ctrl = True, problem = 0):
        self.error = 0
        try:
            name = input("Please Enter Your Name: ")
        except KeyboardInterrupt:
            #generates random name
            self.error += 1
            time.sleep(1)
            print('Are you serious....?')
            time.sleep(1)
            print('*sighs*')
            time.sleep(0.5)
            print("Fine... your name will be...")
            name_list = random.choices(names)
            name = name_list[0]
            time.sleep(2)
            print(f'{name} it is...')
            time.sleep(1)
            print(f'Please do not be offended :)\nI\'m just horrible with names\nPlus, it was you who decided to not cooperate.')
            time.sleep(2.5)

        self.x = x 
        self.y = y
        self.mental = mental
        self.surprise = None
        self.miss = miss
        self.mark = mark
        self.ctrl = ctrl
        self.problem = problem
        self.choose_question = choose_question
        self.name = name
        
        print(f'\nIn this game, you will play as a child who has a strict family.\nYour whole family, including you, are all perfectionists.\nYour goal in the game is to survive, while keeping up your good grades.')
        time.sleep(5)

        
        #bug fix--> _continue_() is now called at the end of every semi-round after the first whole round, objects in mark_list are now properly popped.
        self.bug_fix = False

    def ctrl_c_except(self): #function runs when player tries to exit the game by pressing ctrl+c
            self.error += 1
            print(f'------------------------\n[ᴛʜᴇ sʏsᴛᴇᴍ ʜᴀs ᴅᴇᴛᴇᴄᴛᴇᴅ ᴛʜᴇ ᴘʟᴀʏᴇʀ ᴇxɪᴛɪɴɢ ᴛʜᴇ ᴄᴏᴅᴇ ᴡɪᴛʜᴏᴜᴛ ᴘᴇʀᴍɪssɪᴏɴ]')
            print("0%")
            time.sleep(1)
            print("12%")
            time.sleep(2)
            print("41%")
            time.sleep(1)
            print("70%")
            time.sleep(3)
            print("99%")
            time.sleep(5)
            print("100%")
            time.sleep(2)
            print("Restarting...")
            time.sleep(5)

    #called in every function, checking for mental
    def everytime(self): 
        game.wow()
        if self.error >= 20:
            #Kind of an ending
            print("\nI'm done with you.\nGet out of my game.")
            time.sleep(1)
            quit()
        if self.error == 10:
            print(f'\n\n{self.name}!\nSTOP TRYING TO TYPE IN INVALID RESPONSES AND EXITING THE GAME!\n\n')
            time.sleep(3)    

        if self.ctrl == True:
            game.help_()
        if self.mental >= 50:
            #Player dies in a randomly generated way, picking one option out of two
            rand_ending = random.randint(1,2) 

            if rand_ending == 1:
                #player is free to interpret differently what this emoticon means or resembles.
                print(f'------------------------\nYour life has been harsh on you recently.\nYou think about the effort you put in to raise your marks\nYou think about the unsatisfied expression from your parents\nYou think about the anxiety and pressure you felt every test')
                print(f'You walked over to a high location, gazing at the scenery below and around you and closes your eyes...')
                print(f'ミ(ノ _ _)ノ') #Endling 1
            if rand_ending == 2:
                print(f'------------------------\nYou suddenly freeze, your eyes widen as you feel your heart muscles contract painfully\nShortly, your vision goes black, and that was the last thing your felt')

            print(f'Congratulations for reaching the end, {self.name}')
            time.sleep(2)
            
            #player dies
            quit() 

    #after round two. After round two, is called every round if player chooses to continue. 
    def _continue_(self): 
        game.everytime()
        
        self.x = 0
        self.y = 2

        #removes the first object in the list
        mark_list.pop(0) 
        game.start()

    #start of the story, repeated each round
    def start(self): 
        game.everytime()
        
        if self.y == 0:

            #not included in second round, controlled by variable y, self.y
            print(f'------------------------\nWelcome to:\n𝕿𝖍𝖊𝖗𝖊 𝖎𝖘 𝕹𝖔 𝕰𝖓𝖉𝖎𝖓𝖌\nUnless...\nYou gotta play this for multiple rounds\nGood Luck, {self.name}.\n(  ･ω･)ﾉ')
            
        try:
            choice1 = int(input(f'________________________\n(:3[▓▓▓▓▓▓▓▓]\nYour alarm wakes you up at 5 am in the morning. \nYou had to wake up early to study for an important test, but \nyou felt so exhausted. What do you do?\n------------------------ \nChoice 1: Wake up at 5 am and review. \nChoice 2: Set the alarm to 7:30 am, allowing you to sleep more, but have no time to review. \nChoice 3: Set the alarm to 6am, so you could sleep a bit longer, but have less time to review.\n------------------------ \nYour Choice:')) 
            if choice1 == 1:
                print(f'------------------------\nYou reviewed for 2 hours, you feel much more confident in the test.\n╰(⇀‸↼)╯')
                self.problem -= 1
                self.mental += 1
                game.breakfast()
            elif choice1 == 2 or choice1 == 3:
                self.surprise = random.randint(1,3) 

                #player misses the alarm, ends up getting up late for school. Jumps to the next_period function, since player missed the test.
                if self.surprise == 1: 
                    print(f'------------------------\nYou reset your alarm to another time. \nTurns out you were too tired to check if you turned the alarm back on after changing the time. \nYour alarm did not wake you up and your parents busted into your room angrily, waking you up. \n(╯°Д°）╯︵ /(.□ . \)\nOh no!\nIt is already 10am, you are late for school and missed your test!\nYou ran to school and sighed as you head towards your next class')
                    self.mental += 3
                    self.miss = True
                    self.x += 1
                    game.next_period()
                else:
                    if choice1 == 2:
                        print(f'------------------------\nYou wake up at 7:30 and goes downstairs to preapre for school.\n╰(⇀‸↼)╯')
                        self.problem += 2.5
                        game.breakfast()
                    if choice1 == 3:
                        print(f'------------------------\nYou wake up at 6 am and reviews for the test for 1.5 hours.\n╰(⇀‸↼)╯')
                        self.problem += 1
                        game.breakfast()
            else:
                print(f'Please enter a valid value')
                self.error += 1
                game.start()
                
        except ValueError:
            print(f'Please enter a valid value')
            self.error += 1
            game.start()
        except KeyboardInterrupt:
            self.ctrl_c_except()
            game.start()
        
    #breakfast, repeats each round
    def breakfast(self): 
        game.everytime()
        
        try:
            choice2 = int(input(f'------------------------\nFeeling hungry, you wanted to go downstairs and eat breakfast. \nWhat do you do?\n------------------------\nChoice 1: Go downstairs to have breakfast\nChoice 2: Go downstairs and study half an hour.\nYour choice:'))
            if choice2 == 1:
                print(f'------------------------\nYou go downstairs and made some oatmeal and boiled an egg for yourself.\n(づ｡◕‿‿◕｡)づ\nAfter finishing your breakfast, you pack up your stuff and head to school.')
                self.mental -= 1
            elif choice2 == 2:
                self.mental += 1
                self.problem -= 0.5
                print(f'------------------------\nAfter half an hour, you go to school.\n-=≡Σ((( つ•̀ω•́)つ')
            else:
                print(f'------------------------\nPlease enter a valid value')
                self.error += 1
                game.breakfast()
            game.question()
            
        except ValueError:
            print(f'------------------------\nPlease enter a valid value')
            self.error += 1
            game.breakfast()
        except KeyboardInterrupt:
            self.ctrl_c_except()
            game.breakfast()

    #chooses between question one and two. Question one during semi-round 1 in a whole round, question two during semi-round 2 in a whole round. Two rounds make one whole round.
    def question(self):  
        game.everytime()
        
        if self.choose_question == True:
            game.question_one()
            if self.y == 2:
                self.x += 1
        else:
            game.question_two()
            
        game.friend()

    #chosen during semmi-round 1
    def question_one(self): 
        game.everytime()
        
        print(f'------------------------\nYou enter your first period classroom and receives the test from the teacher. You are given the question:')
        print(f'If a student has 3 pairs of socks, 2 sets of uniforms, 5 watches, and 4 pairs of shoes. \nHow many possible combinations are there if the students wants to wear his silver watch to school today?')

        try:
            choice3 = int(input(f'Choice 1: 24 combinations\nChoice 2: 120 combinations \nChoice 3: 14 combinations \nChoice 4: Leave the question blank\nYour choice:'))
            if choice3 == 1:
                self.problem -= 1
                print(f'Hmmm...okay...\n║ ಡ ͜ʖಡ║')
            elif choice3 == 2 or choice3 == 3:
                self.problem += 1
                self.mental += 1
                print(f'Hmmm...okay...\n║ ಡ ͜ʖಡ║') 
            else:
                print(f'------------------------\nPlease enter a valid value')
                self.error += 1
                game.question_one()
                
        except ValueError:
            print(f'------------------------\nPlease enter a valid value')
            self.error += 1
            game.question_one()
        except KeyboardInterrupt:
            self.ctrl_c_except()
            game.question_one()
            
        self.choose_question = False

    #chosen during semi-round 2
    def question_two(self): 
        game.everytime()
        
        print(f'------------------------\nYou enter your classroom and sits down. The teacher hands you the test. \nYou are given the question:')
        print(f'If the force applied on an object is 32.0N and the object moved 32.0m on a 32.0 degree tilted, frictionless  surface. What is the work?')

        try:
            choice3_1 = int(input(f'Choice 1: 343J\nChoice 2: 905J\nChoice 3: 868J\nYour choice:'))
            if choice3_1 == 3:
                self.problem -= 1
            elif choice3_1 == 2 or choice3_1 == 1:
                self.problem += 1
                self.mental += 1
            else:
                print(f'------------------------\nPlease enter a valid value')
                self.error += 1
                self.question_two()
            print("That seems about right...?")
            self.choose_question = True

        except ValueError:
            print(f'------------------------\nPlease enter a valid value')
            self.error += 1
            game.question_two()
        except KeyboardInterrupt:
            self.ctrl_c_except()
            game.question_two()

    #asking friend about test, repeated every round
    def friend(self): 
        game.everytime()
        
        
        print(f'------------------------\nYou finish the rest of the questions and hands the test over to your teacher and leaves for the next period')
        print(f'You ask your friend about one of the questions on the test, which question do you want to ask about?')

        try:
            choice4 = int(input(f'Choice 1: Question 6\nChoice 2: Question 11\nChoice 3:Question 17\nYour choice:'))
            if choice4 == 1 or choice4 == 2 or choice4 == 3:
                question = random.randint(1,3)
                if question == 1:
                    print(f'You asked your friend about the test. Oh... You got a question wrong, for now.\n(ʘ ‿ ʘ)')
                    self.problem += 1
                    self.mental += 1
                elif question == 2:
                    print(f'You asked your friend some questions about the test...You messed up for real this time.\nԅ(‹o›Д‹o›ԅ)')
                    self.problem += 3
                    self.mental += 2
                elif question == 3:
                    print(f'You asked your friend about the test. Phew, nothing wrong, for now.\n( ˘▾˘)~')
            else:
                print(f'------------------------\nPlease enter a valid value')
                self.error += 1
                game.friend()
            
            self.x += 1
            game.next_period()
            
        except ValueError:
            print(f'------------------------\nPlease enter a valid value')
            self.error += 1
            game.friend()
        except KeyboardInterrupt:
            self.ctrl_c_except()
            game.friend()

    #next period, during your first semi-round, you are not given a mark, because you have not done any tests the previous day.
    def next_period(self): 
        game.everytime()
        
        #this if statement was moved from the top of the next_period function
        if self.y == 2 or self.x > 1: 
            if self.miss == False:
                print(f'You enter your classroom.\nYour teacher sent back your marks for the previous test. You got a {mark_list[0]}...')

                #if mark gets to zero, game "crashes" and forcefully quits
                if mark_list[0] == 0: #Ending 2
                    try:
                        print(f'------------------------\n\n,pǝɹɹnɔɔo sɐɥ ɹoɹɹǝ uɐ.ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ᴇxɪᴛɪɴɢ ɢᴀᴍ-\n\n------------------------') 
                        error = input(f'Exiting the game... Return any button to confirm: ')
                        time.sleep(2)
                        quit()
                    except KeyboardInterrupt:
                        print(f'User has used Ctrl + C key to confirm exit...')
                        time.sleep(2)
                        quit()

        try:
            print(f'------------------------\nAs your next period starts, you hear your classmates talking about the test\nDo you join into the discussion?')
            choice5 = int(input(f'Choice 1: Join in the discussion\nChoice 2: Don\'t join in the discussion\nYour choice:'))

        except ValueError:
            print(f'------------------------\nPlease enter a valid value')
            self.error += 1
            game.next_period()
        except KeyboardInterrupt:
            self.ctrl_c_except()
            game.next_period()
            
        if choice5 == 1:
            self.mental += 1
            print(f'You decide to join the discussion\nThe loud discussion distracts the class and the teacher calls you out for not paying attention and chatting about unrelated topics\nAs the period comes to an end,\nthe teacher reminds the class that there is a test tomorrow')
        elif choice5 == 2:
            print(f'You decide to focus on class and not join in the discussion\nThe teacher soon calls out the group of people for disrupting the class\nAs the period comes to an end, the teacher reminds the class that there is a test tomorrow')
            self.mental -= 1
        else:
            print(f'------------------------\nPlease enter a valid value')
            self.error += 1
            game.next_period()

        #mark is appended here, because your mental and problem variables logically shouldn't be impacting the grade of your previous test, but the next test.
        if self.x >= 1: 
            
            self.mark = 100 - (self.problem + self.mental)
            if self.mark > 100:
                self.mark = 100
            elif self.mark < 0:
                self.mark = 0
            mark_list.append(self.mark)
                
        #chooses between home() and home_two(), home() is used during the start of the game, when you have no previous tests.
        if self.y < 1:  
            self.y = 1
            game.home()
        else:
            game.home_two()

    #no previous tests, is called
    def home(self): 
        game.everytime()
        
        if self.miss == False:
            print(f'------------------------\nYou walk back home after school ended.\nAs you lock the door behind you and take of your shoes,\nyour parents start asking about how the test went')

            try:
                choice6 = int(input(f'Choice 1: I did wonderful!\nChoice 2:It was okay...?\nYour choice:'))
                if choice6 == 1:
                    print(f'You felt pretty confident or you at least wanted to make you parents think you were.\nYou said you did wonderful')
                elif choice6 == 2:
                    print(f'You didn\'t want your to get their expectations too high\nYou said it was...okay?')
                    self.mental -= 1
                else:
                    print(f'------------------------\nPlease enter a valid value')
                    self.error += 1
                    game.home()

            except ValueError:
                print(f'------------------------\nPlease enter a valid value')
                self.error += 1
                game.home()
            except KeyboardInterrupt:
                self.ctrl_c_except()
                game.home()
   
        else:
            print(f'------------------------\nYou walk back home after missing a test and sighs.\nYour parents walked to you angrily and continued scolding you for waking up late')
            
        game.review()

    #there are previous tests, is called
    def home_two(self): 
        game.everytime()

        if game.miss == False:
            print(f'------------------------\nAs you get back home after the last period, your parents asked for the results of your previous test')
            print(f'You honestly answered:{mark_list[0]}')
            
            if mark_list[0] == 100:
                print(f'Your parents nod their heads.\n"Keep it up,\nthis is the least you can do."')
            elif mark_list[0] <= 99 and mark_list[0] >= 95:
                print(f'Your parents stare at the mark you got\n"How did you lose marks on such an easy question\nYou don\'t take school seriously,\ndo you?"')
                self.mental += 1
            else:
                print(f'You didn\'t study at all, am I right?')
                self.mental += 2
            game.review()
        else:
            game.miss = False
            print(f'After getting back home, your parents give you a warning glare as they see you\nι(｀ロ´)ノヾ(｡>﹏<｡)ﾉﾞ\nI suppose you didn\'t get yesterday\'s test results,\nsince you missed the class\nYou better remember wake up on time tomorrow!\nThey said.')
            game.review()

    #reviewing for the test tomorrow
    def review(self): 
        game.everytime()
        
        print(f'------------------------\nAfter finally finishing talking to your parents about your test, you walk back to your room with your heavy backpack\n(ﾉω･｀o)')

        try:
            choice7 = int(input(f'You sat down in front of your desk and opens your computer. \nChoice 1: Review for tomorrow\'s test\nChoice 2: Paint\nYour choice:'))
            if choice7 == 1:

                #resets, since it's a new test, however, mental doesn't reset
                self.problem = 1 
                self.mental += 1
                print(f'You review for the test tomorrow, going over all the practice questions\n( ◕ᴗ◕)っ╯ 💻')
            elif choice7 == 2:
                self.problem = 1
                self.mental -= 1
                print(f'You enjoy your time painting in your room, locking the doors while playing calming music in your headphones')
                print(f'------------------------\nListening to music...\n1:36 ━❍──────── -3:18\n↻     ⊲  Ⅱ  ⊳     ↺\nVOLUME: ▁▂▃▄▅▆▇ 100%')
            else:
                print(f'------------------------\nPlease enter a valid value')
                self.error += 1
                game.review()
            game.night()

        except ValueError:
            print(f'------------------------\nPlease enter a valid value')
            self.error += 1
            game.review()
        except KeyboardInterrupt:
            self.ctrl_c_except()
            game.review() 
        
    #going to sleep
    def night(self): 
        game.everytime()
        
        print(f'------------------------\nAs the sun sets, you notice it is getting late.🌥')

        try:
            choice8 = int(input(f'Choice 1: Go to sleep early\nChoice 2: Review for the test\nYour choice:'))
            
            if choice8 == 1:
                self.problem += 1
                self.mental -= 1
                print("Zzzzz...\n⋆｡˚(¦3ꇤ[▓▓]⋆｡˚✩")
            elif choice8 == 2:
                self.problem -= 1
                self.mental += 1
                print(f'You open up your notes and starts reviewing...\nWORK（*￣ □ ￣*；\nAfterwards, you go to sleep\n(¦ꎌ[▓▓▓]')
            else:
                print(f'--------------------\nPlease enter a valid value')
                self.error += 1
                game.night()

            if self.x >= 2 or self.bug_fix == True:
                self.bug_fix = True
                game.cont_()
            else:
                game.start()
                
        except ValueError:
            print(f'------------------------\nPlease enter a valid value')
            self.error += 1
            game.night()
        except KeyboardInterrupt:
            self.ctrl_c_except()
            game.night()

    #asks if player wants to continue, is called after the first whole round, and is later called every semi-round.
    def cont_(self):
        game.everytime()
        
        try:
            continue_ = int(input(f'------------------------\nContinue?\nChoice 1: Yes\nChoice 2: No\nYour Choice:')) #Optional Ending
            if continue_ == 1:
                game._continue_()
            elif continue_ == 2:
                
                #game quits if you choose to stop
                quit() 
            else:
                print(f'------------------------\nPlease enter valid value')
                self.error += 1
                game.cont_()

        except ValueError:
            print(f'------------------------\nPlease enter a valid value')
            self.error += 1
            game.cont_()
        except KeyboardInterrupt:
            self.ctrl_c_except()
            game.cont_()

    #after mental variable goes under or equal to 20, mental help choices
    def help_(self): 
        if self.mental >= 20:

            try:
                mental_choice = int(input(f'------------------------\nYour stress has been increasing...\nYou cannot continue your life like this\n(╯°□°)╯︵ ʞɹoʍ\nYou have a choice, do you want to seek for mental help or not?\nChoice 1: Seek for help\nChoice 2: Do not seek for help\nYour choice:'))
                if mental_choice == 1:

                    #if you choose to ask for help, random is used to generate a variable to determine whether you are successful in seeking help or not
                    help = random.randint(1,2) 
                    if help == 1:
                        print(f'You have told your parents about the situation\nd(눈_눈)b\nThey agreed to seek mental help for you.')
                        self.mental -= 50
                    else:
                        print(f'(｡-_-｡ )( ｡-_-｡)\nYour parents ignored your needs')
                        game.break_()
                elif mental_choice == 2:
                    game.break_()
                else:
                    print(f'------------------------\nPlease enter valid value')
                    self.error += 1
                    game.help_()

            except ValueError:
                print(f'------------------------\nPlease enter a valid value')
                self.error += 1
                game.help_()
            except KeyboardInterrupt:
                self.ctrl_c_except()
                game.help_()

    #called after failing to seek mental help, either player refused to, or parents deny to get help
    def break_(self): 
        self.mental += 10
        print(f'------------------------\n( இ﹏இ`｡)\nYou failed to seek for your mental health...\nYour life will only continue going downhill after this moment.')
        self.ctrl = False

    #mocking the player, just for fun, repeated before every function if problem variable is larger or equal to 5.
    def wow(self): 
        if self.problem >= 5:
            print("------------------------\n(☞ ͡ಥuಥ)☞ Haha.\nYou should really be trying harder")
            


game = Game()

#calling the start() function within the Game class.
game.start() 
