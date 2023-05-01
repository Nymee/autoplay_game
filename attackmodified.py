#In the original project enemy attacks first so enemy has got an advantage. But it is only fair if both attacks happen simulataneouly


import random

playerHP= 100
enemyHP=120
enemyattackh=30
enemyattackl=20
playerattack=30
damage=0
damage2=0
x=1
c=0
bol=True



def autogameplay():
   playerHP = 100
   enemyHP = 120
   enemyattackh = 30
   enemyattackl = 20
   playerattack = 30
   damage = 0
   damage2 = 0


   while playerHP>0:
    aimenemy =random.randrange(0,2)
    aim =random.randrange(0, 2)

    if aimenemy==1:
        damage=random.randrange(enemyattackl,enemyattackh)
        playerHP=playerHP-damage
        print("Enemy strikes damage for",damage,"points!")


    else:
        print("Enemy missed!")



    if aim==1:
        enemyHP =enemyHP-playerattack
        print("You strike damage for 30 points! \n")

    else:
        print("You missed! \n")

    if playerHP<=0 and enemyHP<=0:
        print("Nobody won the game..")
        break

    if playerHP<=0:
        print("Enemy laughs. You fall to the ground \nGame over.")
        break

    if enemyHP<=0:
        print("Enemy falls to the ground.\nYou won the game.\n")
        break

while bol== True:

 if x==1:
  autogameplay()

 choice=input("Play again?")

 while c==0:
   if (choice!="Yes" and choice!="yes") and (choice!="No" and choice!="no"):
    choice= input("Type Yes/yes or No/no..? 🙄 ")
    continue
   else:
    c=1



 if choice=="No" or choice=="no":
  print("Haha! Coward")
  break

 if choice=="Yes" or choice=="yes":
  c=0








