import random
while True:
    print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissor \n")
    choice=int(input("Enter your choice :"))
    while choice > 3 or choice <1:
        choice=int(input('Enter a valid choice please '))
    if choice == 1:
        choice_name= 'Rock'
    elif choice == 2:
        choice_name= 'Paper'
    else:
        choice_name= 'Scissor'
    print('User choice is ',choice_name)
    print('Now its Computers Turn..')
    comp_choice = random.randint(1,3)
    while comp_choice == choice:
        comp_choice = random.randint(1,3)
    if comp_choice == 1:
        comp_choice_name = 'rock'
    elif comp_choice == 2:
        comp_choice_name = 'paper'
    else:
        comp_choice_name = 'scissor'
    print("Computer choice is ", comp_choice_name)
    print(choice_name,'Vs',comp_choice_name)
    if choice == comp_choice:
        print('Its a Draw',end="")
        result="DRAW"
    if (choice==1 and comp_choice==2):
        print('paper wins\n',end="")
        result='paper'
    elif (choice==2 and comp_choice==1):
        print('Paper wins\n',end="")
        result='Paper'
    if (choice==1 and comp_choice==3):
        print('Rock wins \n',end= "")
        result='Rock'
    elif (choice==3 and comp_choice==1):
        print('rock wins \n',end= "")
        result='rock'
    if (choice==2 and comp_choice==3):
        print('Scissor wins \n',end="")
        result='scissor'
    elif (choice==3 and comp_choice==2):
        print('scissor wins \n1',end="")
        result='Scissor'
    if result == 'DRAW':
        print(" Its a tie ")
    if result == choice_name:
        print("User wins")
    else:
        print("Computer wins")
    print("Do you want to play again? (Y/N)")
    ans = input().lower
    if ans =='n':
        break
    print("thanks for playing")
