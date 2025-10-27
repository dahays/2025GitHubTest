def main():
    #  main accepts no arguments
    #  it calls menu, and then processes
    #  the returnes value to call each function
    
    choice = menu()
    while choice in range(1, 20):
        if choice == 1:
            oliver(5)
        elif choice == 2:
            henry("test")
        elif choice == 3:
            tate("money")
        elif choice == 4:
            brody(2.5)
        elif choice == 5:
            cohen("love")
        elif choice == 6:
            gage(123)
        elif choice == 7:
            gabe("book")
        elif choice == 8:
            parker("werd")
        elif choice == 9:
            logan_k("U MAD BRO?")
        elif choice == 10:
            allen(67)
        elif choice == 11:
            logan_m("rock on")
        elif choice == 12:
            roman(3.14)
        elif choice == 13:
            sam(5)
        elif choice == 14:
            antonio("pony")
        elif choice == 15:
            bryson("9")
        elif choice == 16:
            tristan(19.91)
        elif choice == 17:
            bricen("ace")
        elif choice == 18:
            alex("sleep token")
        elif choice == 19:
            rhett("MCU")
        else:
            print("Goodbye!")
        choice = menu()
    
    
def menu():
    #  menu accepts no arguments
    #  it presents the user with a list of choices
    #  and returns the chosen menu choice
    
    input("Press enter to continue...")
    print("Please choose from the following choices:")
    print("1.  Oliver")
    print("2.  Henry")
    print("3.  Tate")
    print("4.  Brody")
    print("5.  Cohen")
    print("6.  Gage")
    print("7.  Gabe")
    print("8.  Parker")
    print("9.  Logan K.")
    print("10. Allen")
    input("press enter for more...")
    print("11. Logan M.")
    print("12. Roman")
    print("13. Sam")
    print("14. Antonio")
    print("15. Bryson")
    print("16. Tristan")
    print("17. Bricen")
    print("18. Alex")
    print("19. Rhett")
    
    choice = int(input(":> "))
    return choice
    
def oliver(arg):
    #  ____ accepts a ___ for arg
    #  it does something
    #  it returns something
    pass
    
def henry(arg):
    #  ____ accepts a ___ for arg
    #  it does something
    #  it returns something
    pass
    
def tate(arg):
    #  tate accepts a string for arg
    #  prints "I am Tate!" and the arg
    #  returns a string
    print('I am Tate!')
    likes_money = print(f"I love {arg}!")
    print("Adios!")
    
    return likes_money
    
    
    
def brody(arg):
    #  ____ accepts a ___ for arg
    #  it does something
    #  it returns something
    pass
    
def cohen(arg):
    #  ____ accepts a ___ for arg
    #  it does something
    #  it returns something
    pass
    
def gage(arg):
    #  ____ accepts a ___ for arg
    #  it does something
    #  it returns something
    pass
    
def gabe(arg):
    #  ____ accepts a ___ for arg
    #  it does something
    #  it returns something
    pass
    
def parker(arg):
    #  ____ accepts a ___ for arg
    #  it does something
    #  it returns something
    pass
    
def logan_k(arg):
    #  Logan accepts "U MAD BRO?" for arg
    #  it prints ARE U MAD BRO?
    #  it returns mad
    mad = print('ARE' , arg)
    return mad
    
def allen(arg): #67
    #  ____ accepts a ___ for arg
    #  it does something
    #  it returns something
    print("The topic is", arg)
    print("The", arg, "meme traces back to a drill rap song by Philadelphia rapper Skrilla,")
    print("which features the lyric", arg, "in its chorus.")    

    
def logan_m(arg):
    #  ____ accepts a ___ for arg
    #  it does something
    #  it returns something
    pass
    
def roman(arg):
    #  roman accepts 1 arguement
    #  it prints whatever your arguement was
    #  it returns your input as a message
    print(str(arg, "hi"))
    
def sam(arg):
    #  ____ accepts a ___ for arg
    #  it does something
    #  it returns something
    pass
    
def antonio(arg):
    #  ____ accepts a ___ for arg
    #  it does something
    #  it returns something
    pass
    
def bryson(arg):
    #  ____ accepts a ___ for arg
    #  it does something
    #  it returns something
    pass
    
def tristan(arg):
    #  ____ accepts a ___ for arg
    #  it does something
    #  it returns something
    pass
    
def bricen(arg):
    #  Bricen accepts ace for arg
    #  it does something
    #  it returns something
    ldog = print(f"Logan's dog's name is {arg}")
    return ldog
    
def alex(arg):
    #  ____ accepts a ___ for arg
    #  it does something
    #  it returns something
    pass
    
def rhett(arg):
    #  ____ accepts a ___ for arg
    #  it does something
    #  it returns something
    pass

main()