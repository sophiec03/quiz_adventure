# An adventure game
from random import randint

health = 10
energy = 20

if health == 0:
        print("YOU HAVE LOST ALL OF YOUR HEALTH")
        print("Game over")
        quit()

elif energy == 0:
        print("You fall unconsious. The fatal liger kills you.")
        print("Game over")
        quit()
        

        name = input("What is your name?: ")
        print("Ok,", name,"get ready for your adventure")

    



def status():
    global health, energy

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("                                                           Health:", health,", energy:", energy, "                                                          ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
     


def stage1():
    global health, energy

    status()

    print("""You fall to the bottom of the rabbit hole into a giant room. All
    of the furniture is 3 times the size of you. There are doors that are your size,
    but the keys are on a a shelf high above you. On the table next to you, there
     are cakes(your size) that say "eat me". What will you do? Eat it, or leave it?""")
    answer = input("What would you like to do? A: Eat it, or B: Leave it?")
    if answer.lower() == "a":
        print("""The cake makes you grow until your head hits the roof, but
    you can reach the keys.""")
        energy = energy + 2
        stage2()
    elif answer.lower() == "b":
        print("""Nothing happens, how will you ever get those keys though?""")
        stage1b()

def stage1b():
    global health, energy

    status()

    print(""" A rabbit pops out behind a chair. He says to you:"These cakes, they
make you grow. Wouldn't that be helpful...". Will you eat it? Yes or no?""")
    answer = input("What will you choose? A: Yes, or B: No?")
    if answer.lower() == "a":
        print("""You eat the cake and grow until you hit the roof.""")
        energy = energy + 2
        stage2()
    elif answer.lower() =="b":
          print("""A liger(a mix of a lion and a tiger) is released into the
room due to your bad decisions. It claws at you.""")
          print("You lose 10 health")
          health = health - 10
          stage2()
    
          
                
def stage2():
    global health, energy
    

    status()

    print("""You grab the keys off the shelf and look below you. There is a small
bottle on the table. As you look closer, it has a label that says "Drink Me". You are
too big to fit through the doors anymore. Based on your past decisions, what do you do?
Drink it, or leave it?""")

    answer = input("What will you do? A: Drink it, or B: Leave it?")
    if answer.lower() == "a":
        print("""The potion makes you shrink back to your noral size.""")
        stage3()
    elif answer.lower() == "b":
        print("""Nothing happens, but you need to be small enough to fit through the door!""")
        stage2b()


def stage2b():
    global health, energy

    status()

    print("""You know you must do something to become small, and the potion is the only thing
to do right now...""")
    answer = input("Do you A: reconsider your decisions, or B: leave it for good?")
    if answer.lower() == "a":
        print("""It was the right decision! You are small again!""")
        stage3()
    elif answer.lower() == "b":
        print("""A liger(a mix of a lion and a tiger) is released into the
room due to your bad decisions. It kills you.""")
        print("Game over")
        quit()


def stage3():
    global health, energy

    status()

    print("""You get your key and go over to the doors. There are three doors you can go
through.""")
    answer = input("Which door will you try first? A, B or C?")
    if answer.lower() == "a":
        print("""The door leads you into a dark mysterious corridor...""")
        stage3a()
    elif answer.lower() == "b":
        print("""You can see the sun shining as soon as you open the door. You decide this
is the right choice and run forward.""")
        stage4()
    elif answer.lower() == "c":
        print("""There is a dark hole in front of you...""")
        stage3c()


def stage3a():
    global health, energy

    status()

    print("""The dark corridor leads to a small chamber. The air is moist. There is a note that
says: "You have made the wrong choice. You must answer the following question right, or prepare for consequences!""")
    print("What is: 7 - 9 + 14 x 6?")
    answer = input("What is your answer?")
    if answer == "-86":
        print("""You are good at maths. You may go back...""")
        stage3()
    else:
        print("Your lack of knowledge isnot good. A lightning strike flashes, taking  some of your health.")
        health = health - 6
        


def stage3c():
    global health, energy

    status()

    random = randint(0, 1)

    if random == 0:
        print("""You manage to miss falling down the hole. The next corridor leads you to the
the previous room.""")
        stage3()
    elif random == 1:
        print("""You fall down the hole and die.""")
        print("Game over.")
        quit()


def stage4():
    global health, energy

    ligerhealth = 5

    if health == 0:
        print("You are dead")
        quit()
        
    elif ligerhealth == 0:
        print("The liger is dead. You win!")
        stage5()
            

    status()

    print("""You are led to the next room. There is the fatal liger, he wants to fight.""")
    print("""-------------------------------------------------------------------------""")
    print("""                        Liger: health =""", ligerhealth,"""              """)
    print("""-------------------------------------------------------------------------""")
    print("""Time to fight!""")
    print("What attack will you use?")
    answer = input("A: sword, B: magic")
    if answer.lower() == "a":
        print("You have done the liger 10 damage")
        ligerhealth = ligerhealth - 10
    elif answer. lower() == "b":
        print("You do the liger 20 damage")

    random = randint(0,10)

    if random == 0:
        print("The liger has done you no damage")

    elif random == 1:
        print("The liger has done you 1 damage")

    elif random == 2:
        print("The liger has done you 2 damage")
            
    elif random == 3:
        print("The liger has done you 3 damage")

        
    elif random == 4:
        print("The liger has done you 4 damage")

    elif random == 5:
        print("The liger has done you 5 damage")

    elif random == 6:
        print("The liger has done you 6 damage")

    elif random == 7:
        print("The liger has done you 7 damage")

    elif random == 8:
        print("The liger has done you 8 damage")
            
    elif random == 9:
        print("The liger has done you 9 damage")

    elif random == 10:
        print("The liger has done you 10 damage")

    print("What attack will you use?")
    answer = input("A: sword, B: magic")
    if answer.lower() == "a":
        print("You have done the liger 10 damage")
        ligerhealth = ligerhealth - 10
    
    elif answer. lower() == "b":
            print("You do the liger 20 damage")

    random = randint(0,10)

    if random == 0:
        print("The liger has done you no damage")

    elif random == 1:
        print("The liger has done you 1 damage")

    elif random == 2:
        print("The liger has done you 2 damage")

    elif random == 3:
        print("The liger has done you 3 damage")

        
    elif random == 4:
        print("The liger has done you 4 damage")

    elif random == 5:
        print("The liger has done you 5 damage")

    elif random == 6:
        print("The liger has done you 6 damage")

    elif random == 7:
        print("The liger has done you 7 damage")

    elif random == 8:
        print("The liger has done you 8 damage")

    elif random == 9:
        print("The liger has done you 9 damage")

    elif random == 10:
        print("The liger has done you 10 damage")

        
            
  


def stage5():
    global health, energy

    status()

    print("""This is the last room of your trial. Be happy you have made it this far..""")
    print("""Fight the evil pegasus or an evil egg?""")
    answer = input("What will you do? A: Evil pegasus, B: Evil egg")
    if answer.lower() == "a":
        stage6()
    if answer.lower() == "b":
        stage5b()


def stage5b():
    global health, energy

    egghealth = 60

    if health == 0:
        print("You are dead")
        quit()
        
    elif egghealth == 0:
        print("The egg is dead. You win!")
        print("You win the game. Congrats")


                   
    status()

                

    

    print("What attack will you use?")
    answer = input("A: sword, B: magic")
    if answer.lower() == "a":
        print("You have done the egg 10 damage")
        egghealth = egghealth - 10
    
    elif answer. lower() == "b":
            print("You do the egg 20 damage")

    random = randint(0,10)

    if random == 0:
        print("The egg has done you no damage")

    elif random == 1:
        print("The egg has done you 1 damage")

    elif random == 2:
        print("The egg has done you 2 damage")

    elif random == 3
        print("The egg has done you 3 damage")

        
    elif random == 4:
        print("The egg has done you 4 damage")

    elif random == 5:
        print("The egg has done you 5 damage")

    elif random == 6:
        print("The egg has done you 6 damage")

    elif random == 7:
        print("The egg has done you 7 damage")

    elif random == 8:
        print("The egg has done you 8 damage")

    elif random == 9:
        print("The egg has done you 9 damage")

    elif random == 10:
        print("The egg has done you 10 damage")


    print("What attack will you use?")
    answer = input("A: sword, B: magic")
    if answer.lower() == "a":
        print("You have done the egg 10 damage")
        egghealth = egghealth - 10
    
    elif answer. lower() == "b":
            print("You do the egg 20 damage")

        random = randint(0,10)

    if random == 0:
        print("The egg has done you no damage")

    elif random == 1:
        print("The egg has done you 1 damage")

    elif random == 2:
        print("The egg has done you 2 damage")

    elif random == 3
        print("The egg has done you 3 damage")

        
    elif random == 4:
        print("The egg has done you 4 damage")

    elif random == 5:
        print("The egg has done you 5 damage")

    elif random == 6:
        print("The egg has done you 6 damage")

    elif random == 7:
        print("The egg has done you 7 damage")

    elif random == 8:
        print("The egg has done you 8 damage")

    elif random == 9:
        print("The egg has done you 9 damage")

    elif random == 10:
        print("The egg has done you 10 damage")


   print("What attack will you use?")
    answer = input("A: sword, B: magic")
    if answer.lower() == "a":
        print("You have done the egg 10 damage")
        egghealth = egghealth - 10
    
    elif answer. lower() == "b":
            print("You do the egg 20 damage")

        random = randint(0,10)

    if random == 0:
        print("The egg has done you no damage")

    elif random == 1:
        print("The egg has done you 1 damage")

    elif random == 2:
        print("The egg has done you 2 damage")

    elif random == 3
        print("The egg has done you 3 damage")

        
    elif random == 4:
        print("The egg has done you 4 damage")

    elif random == 5:
        print("The egg has done you 5 damage")

    elif random == 6:
        print("The egg has done you 6 damage")

    elif random == 7:
        print("The egg has done you 7 damage")

    elif random == 8:
        print("The egg has done you 8 damage")

    elif random == 9:
        print("The egg has done you 9 damage")

    elif random == 10:
        print("The egg has done you 10 damage")

    

  


def stage6():
    global health, energy

         pegasushealth = 40

    if health == 0:
        print("You are dead")
        quit()
        
    elif pegasushealth == 0:
        print("The pegasus is dead. You win!")
        print("You win the game. Congrats")

     print("""You are led to the next room. There is the fatal pegasus, he wants to fight.""")
    print("""-------------------------------------------------------------------------""")
    print("""                        Pegasus: health =""", pegasushealth,"""              """)
    print("""-------------------------------------------------------------------------""")
    print("""Time to fight!""")


    print("What attack will you use?")
    answer = input("A: sword, B: magic")
    if answer.lower() == "a":
        print("You have done the pegasus 10 damage")
        pegasushealth = pegasushealth - 10
    
    elif answer. lower() == "b":
            print("You do the pegasus 20 damage")

        random = randint(0,10)

    if random == 0:
        print("The pegasus has done you no damage")

    elif random == 1:
        print("The pegasus has done you 1 damage")

    elif random == 2:
        print("The pegasus has done you 2 damage")

    elif random == 3
        print("The pegasus has done you 3 damage")

        
    elif random == 4:
        print("The pegasus has done you 4 damage")

    elif random == 5:
        print("The pegasus has done you 5 damage")

    elif random == 6:
        print("The pegasus has done you 6 damage")

    elif random == 7:
        print("The pegasus has done you 7 damage")

    elif random == 8:
        print("The pegasus has done you 8 damage")

    elif random == 9:
        print("The pegasus has done you 9 damage")

    elif random == 10:
        print("The pegasus has done you 10 damage")


    print("What attack will you use?")
    answer = input("A: sword, B: magic")
    if answer.lower() == "a":
        print("You have done the pegasus 10 damage")
        pegasushealth = pegasushealth - 10
    
    elif answer. lower() == "b":
            print("You do the pegasus 20 damage")

        random = randint(0,10)

    if random == 0:
        print("The pegasus has done you no damage")

    elif random == 1:
        print("The pegasus has done you 1 damage")

    elif random == 2:
        print("The pegasus has done you 2 damage")

    elif random == 3
        print("The pegasus has done you 3 damage")

        
    elif random == 4:
        print("The pegasus has done you 4 damage")

    elif random == 5:
        print("The pegasus has done you 5 damage")

    elif random == 6:
        print("The pegasus has done you 6 damage")

    elif random == 7:
        print("The pegasus has done you 7 damage")

    elif random == 8:
        print("The pegasus has done you 8 damage")

    elif random == 9:
        print("The pegasus has done you 9 damage")

    elif random == 10:
        print("The pegasus has done you 10 damage")


    print("What attack will you use?")
    answer = input("A: sword, B: magic")
    if answer.lower() == "a":
        print("You have done the pegasus 10 damage")
        pegasushealth = pegasushealth - 10
    
    elif answer. lower() == "b":
            print("You do the pegasus 20 damage")

        random = randint(0,10)

    if random == 0:
        print("The pegasus has done you no damage")

    elif random == 1:
        print("The pegasus has done you 1 damage")

    elif random == 2:
        print("The pegasus has done you 2 damage")

    elif random == 3
        print("The pegasus has done you 3 damage")

        
    elif random == 4:
        print("The pegasus has done you 4 damage")

    elif random == 5:
        print("The pegasus has done you 5 damage")

    elif random == 6:
        print("The pegasus has done you 6 damage")

    elif random == 7:
        print("The pegasus has done you 7 damage")

    elif random == 8:
        print("The pegasus has done you 8 damage")

    elif random == 9:
        print("The pegasus has done you 9 damage")

    elif random == 10:
        print("The pegasus has done you 10 damage")


    print("What attack will you use?")
    answer = input("A: sword, B: magic")
    if answer.lower() == "a":
        print("You have done the pegasus 10 damage")
        pegasushealth = pegasushealth - 10
    
    elif answer. lower() == "b":
            print("You do the pegasus 20 damage")

        random = randint(0,10)

    if random == 0:
        print("The pegasus has done you no damage")

    elif random == 1:
        print("The pegasus has done you 1 damage")

    elif random == 2:
        print("The pegasus has done you 2 damage")

    elif random == 3
        print("The pegasus has done you 3 damage")

        
    elif random == 4:
        print("The pegasus has done you 4 damage")

    elif random == 5:
        print("The pegasus has done you 5 damage")

    elif random == 6:
        print("The pegasus has done you 6 damage")

    elif random == 7:
        print("The pegasus has done you 7 damage")

    elif random == 8:
        print("The pegasus has done you 8 damage")

    elif random == 9:
        print("The pegasus has done you 9 damage")

    elif random == 10:
        print("The pegasus has done you 10 damage")


    
    

    

    
    
        
              
    

    
    
        

    
        
    
    
            
    
    
    

    

    
    


    








# Leave this at the bottom - it makes room1 run automatically when you
# run your code.
if __name__ == "__main__":

    print("""You are walking through an abandoned forest when you come across a
    massive tree. You decide to walk up closer to the tree, when you fall down a
    rabbit hole...""")
    stage1()
