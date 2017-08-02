#Lyrics,Artist, Title Quiz
#Can you name the Songs which first words of the lyrics are the Song's Title"
#By Patricia Flores

#This is the first fuction that will explain the directions. 

def intro(): 
    print "Can you name the the song titles which the first words of the lyrics are the song's title?" 
    print "Test your knowledge on this music quiz to see how you do."
    print


    song01()     # Call the song01 title. Next

def song01():
    print "****Guess this song title and artist****"
    print "_____  ______ , she's been living in her uptown world.Hint(2 words)"
    print
    count = 0
    while count <2:
        answer = raw_input ("Type (Song Title,Artist)")
        if answer != 'Uptown Girl, Billy Joel':
            count += 1
            print "Sorry, your wrong!"
        else: 
            song02()
    song02()

def song02():
    print
    print " Next  (____ _____, walking down the street.)"

    print
    count = 0
    while count <2:
        answer = raw_input ("Type (Song Title,Artist)")
        if answer != 'Pretty Women, Roy Orbinson':
            count += 1
            print "Sorry, your wrong!"
        else: 
            song03()
    song03()

def song03():
    print
    print " Next  (___  ___  ____ ___, we got fun and games.)"
    
    print
    count = 0
    while count <2:
        answer = raw_input ("Type (Song Title, Group-N-Hint)")
        if answer != 'Welcome To The Jungle, Guns-N-Roses':
            count += 1
            print "Sorry, your wrong!"
        else: 
            song04()
    song04()

def song04():
    print
    print " Next (____ ____ ____ x2, when no one is around you,"
    print " Say baby I love you.) "
    
    print
    count = 0
    while count <2:
        answer = raw_input ("Type (Song Title, Group)")
        if answer != "Say My Name, Destiny's Child":
            count += 1
            print "Sorry, your wrong!"
        else:
            song05()
    song05()

def song05():
    print
    print "Last (____ ___ ____ ____ , what a girl needs.)"
    
    print
    count = 0
    while count <2:
        answer = raw_input ("Type (Song Title, Artist)")
        if answer != "What A Girl Wants, Christina Aguilara":
            count += 1
            print "Sorry, your wrong!"
        else: 
            end()
def end():
    print
    print "Thank You for playing ."
    print
    
    answer = raw_input ("Next player, Do you want to play a game? (Y/N) ")
    
    if answer == 'Y':
        intro()
    else:
        print "Good Bye!"
        


        

#main program
intro()




    