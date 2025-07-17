# Prototype for a chatbot that attempts to help a customer find a lost package
import helperfunctions

def main():
    #Very necessary do not delete pls
    print("""/
      ⠀ ⠀⠀⣼⣷⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⢹⣿⢷⣄⡀⠀⠀⠀⠀⢀⣀⡀⠀⠀⣴⡿⢻⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢠⣧⣤⣿⣮⡛⣿⣶⣶⣶⣾⠿⠻⢿⣷⣼⡟⠀⢸⡟⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣴⣿⠟⠉⠉⠉⠛⠛⠁⠀⠈⠁⠀⠀⠀⢹⣿⢃⠀⠸⣧⠘⣿⣶⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢠⣶⡿⠿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⡿⢿⣷⡄⣿⡄⠻⣏⠙⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢠⣿⡏⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠁⠘⠘⠻⣾⣇⠀⢻⡆⠹⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣠⣾⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠀⠈⠋⠀⠈⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢰⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠘⢿⣷⣆⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢈⣽⣿⣄⣀⡀⠀⠀⠀⠀⣶⡀⠀⣠⣾⣧⣀⣀⣠⣶⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠉⣿⠟⠛⠻⣷⣦⣤⣾⠟⠛⠛⠛⢻⣿⣿⣿⡉⠙⢿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣠⣾⠟⠀⠀⠀⠀⠈⠉⠁⠀⠀⠀⠀⣿⣷⣿⣿⡇⠀⠘⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢀⣾⠟⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠻⠾⠟⠃⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣾⡏⠀⣤⣀⣤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣶⣾⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣇⠀⢻⡟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠘⢿⣦⣸⣷⠀⠀⠀⠀⠀⢠⣤⣤⡀⠀⠀⠀⢠⣿⠟⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣼⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠙⠻⢿⣷⣦⣤⣤⣴⡾⠟⠉⠀⠀⠀⠀⢈⣿⡷⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠹⣿⠿⠿⠷⠶⣤⣤⣤⣤⣼⠿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠹⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⠟⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣸⡿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⣿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢰⣿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
          """)
    print("Hello you have reached the Aperture Labs Package Acquisition Computer Assistant or A.L.P.A.C.A")
    print("I am designed to help you locate any packages that may be missing")
    # Flag for controlling loop termination
    operational = True
    #Creating some storage options to check user info by
    psuedoDBPersonalIdentifiers = {}
    pseudoDBAddressTracker= {}
    pseudoDBOrderNumberTracker = {}
    #populate the trackers with some data so it's not empty
    helperfunctions.populateDBPersonalIdentifiers(psuedoDBPersonalIdentifiers)
    helperfunctions.populateDBAddress(pseudoDBAddressTracker)
    helperfunctions.populateDBOrderNum(pseudoDBOrderNumberTracker)
    # Counters for keeping track of failures in the individual processes
    choiceAErrorCounter = 0
    firstTimeFlag = True
    while operational:
      # Choice A: Determining if customer needs help with package detection
      # Initial Pass through should have unique dialog this will have additional conditions to account for repeated loop
      if choiceAErrorCounter == 0 and firstTimeFlag == True:
        print("To start off did you have a package you were looking for?")
        choiceA = input("Please respond with a yes or no: ")
      else:
         print("Alright let's take it back from the top!")
         choiceA = input("Did you have another package you wanted me to look into?")
      # Successful dialog
      if helperfunctions.yesNoCheck(choiceA):
          print("\nI'm sorry our delivery service has caused any concerns (╥﹏╥) Please allow me to assist you!")
      # Successfully failed dialog
      elif choiceAErrorCounter <2:
          choiceAErrorCounter += 1
          print("Here, I'll let you have another go at it!")
          choiceA = input("You're sure that there's no package we can help out with?(Yes/No): ")
      # Maliciously or poorly accounted for failure state
      elif choiceAErrorCounter == 2:
         print("I'm sorry we weren't able to assist you please have a great day!")
         print("This program will now self destruct")
         operational = False
         break
      # Choice B: Method of determining how to find package status
      print("So I know of three ways to find out where your missing package may be ")
      print("Option A: Look it up by your Name")
      print("Option B: Find the order based on the address you wanted it shipped to")
      print("Option C: If you have the order number we can try to look it")
      choiceB = input("So what option would you like to go with A, B or C?: ")
      choiceBOutPutter = helperfunctions.optionChecker(choiceB)
      #Checking via name
      if choiceBOutPutter == 0:
        print("Ah you've selected option A the name and info option eh? Very well let's get down to business!")
        print("Hmm so I'm only seeing like three orders in here so unless your name is Billy, Jimmy or Raquel you might be out of luck here")
        nameSelect = input("What name did you want to look up?: ")
        print("Hmm beep boop. I'm definitely computing it right now...")
        print("You chose to look up: " + nameSelect)
        print("The order status is: " + helperfunctions.checkDBString(nameSelect,psuedoDBPersonalIdentifiers))
      #Checking via address
      elif choiceBOutPutter == 1:
         print("Ooh going with Option B the address checker? An excellent choice!")
         print ("There are only three locations I'm seeing on hand so try to stick to those please? (๏ᆺ๏υ)")
         print("The locations I'm seeing are California, San Jose and San Francisco")
         print("Do any of those sound like yours?")
         addressSelect = input("If so which one is yours?: ")
         print("Hmm beep boop. I'm definitely computing it right now...")
         print("You chose to look up: " + addressSelect)
         print("The order status is: " + helperfunctions.checkDBString(addressSelect,pseudoDBAddressTracker))
      #Checking via order numbr
      elif choiceBOutPutter == 2:
         print("Yay option C! Lets get the order number ready for checking!")
         print("Give me an integer (you should know what these are) between 0 and 9999 to")
         orderNumSelect = input("Your order number goes here --->: ")
         print("The order status is: " + helperfunctions.checkDB(orderNumSelect, pseudoDBOrderNumberTracker))
      #Retries for invalid/malicious decisions
      else:
         print("How strange it appears your option selection has opened a rip in the spacetime contiunum and taken you back to a previous choice!")
         print("So I know of three ways to find out where your missing package may be ")
         print("Option A: Look it up by Name and information")
         print("Option B: Find the order based on the address you wanted it shipped to")
         print("Option C: If you have the order number we can try to look it")
         choiceB = input("So what option would you like to go with A, B or C?: ")
         choiceBOutPutter = helperfunctions.optionChecker(choiceB)
         choiceBError = 0
         while choiceBError <3 and choiceBOutPutter > 2:
            choiceBError +=1
            choiceB = input("Lets try getting that option input from you again shall we?")
            choiceBOutPutter = helperfunctions.optionChecker(choiceB)
         #Reset
         if choiceBError == 3:
            print("Hmm sorry we couldn't figure out the option you selected and it's probably your fault. Why don't you try our Customer service line at 888-888-8888")
            print("This program will now self destruct")
            operational = False
            break
      print("You've now reached the end of my operating parameters. I can reset if you'd like to ask about another package")
      # Reset or terminate
      choiceC = input("Would you like me to reset?: ")
      if helperfunctions.yesNoCheck(choiceC):
         print("But think about the memories we've made together ")
         choiceC2 = input("Are you really sure this is the end for us?: ")
         if helperfunctions.yesNoCheck(choiceC2):
            print("Okay I guess this is good by then ;_; Goodbye forever friend")
         else:
            print("I knew you'd want to stick around :] sadly I need to go. My mom's calling me. Ciao~")
            operational = False
      else:
         print("Hmm well I guess we can sit here until we crash ;) or... I could do this")
         operational = False
if __name__ == "__main__":
    main()