# Prototype for a chatbot that attempts to help a customer find a lost package


from os import name


def yesNoCheck(checkMe):
  # Assuming the person writes out a sentence or some phrase that contains yes or no 
   if checkMe and len(checkMe) < 500:
      checkMe = checkMe.strip()
      checkMe = checkMe.lower()
      # Responses met parameters
      if "yes" in checkMe or "oui" in checkMe or "true" in checkMe or "affirmative" in checkMe or "si" in checkMe:
          return True
      elif "no" in checkMe or "non" in checkMe or "false" in checkMe or "negative" in checkMe or "nyet" in checkMe:
          print("No worries then! I hope you have a wonderful day!")
          return False
      # incase of a single letter response
      elif len(checkMe) == 1:
         if checkMe == "y":
            print("Kinda getting a yes vibe from your response")
            return True
         elif checkMe == "n":
            print("Kind of got a no vibe from your response")
            print("No worries then! I hope you have a wonderful day!")
            return False      
      else:
          print("Hmm I'm not sure I understood that can we try that again?")
          return False

def optionChecker(checkMe):
  # Assuming the person writes out a sentence or some phrase that contains yes or no 
   if checkMe and len(checkMe) < 500:
      #Reduce variability by removing spaces and changing to lower case
      checkMe = checkMe.strip() 
      checkMe = checkMe.lower()
      if "optionA" in checkMe or "option a" in checkMe or "name" in checkMe or "info" in checkMe:
          return 0
      elif "optionb" in checkMe or "option b" in checkMe or "address" in checkMe or "shipping" in checkMe:
          return 1
      elif "optionc" in checkMe or "option c" in checkMe or "order" in checkMe or "number" in checkMe:
          return 2
      #incase of a single letter response
      elif len(checkMe) == 1:
         if checkMe == "a":
            return 0
         elif checkMe == "b":
            return 1
         elif checkMe == "c":
            return 2
      else:
         print("I don't think I quite understood that...")
         return 3

#Functions to create dummy data for dbs
def populateDBPersonalIdentifiers(database):
   database["billy"] = "Order seems to have been eaten by Pelicans which is not covered by your insurance"
   database["jimmy"] = "Order is on time to arrive by the year 20XX"
   database["raquel"] = "Order was dropped off. Signed for by Emperor Palpatine"

def populateDBAddress(database):
   database["san jose"] = "So your order is kinda stuck in traffic and will be stuck in traffic for another couple hours until it's quitting time"
   database["california"] = "I think we saw the delivery person crying because we don't cover gas costs but who's to say"
   database["san francisco"] = "It was delivered probably. It's hard to tell if it was the right address though SF is weird."

def populateDBOrderNum(database):
   database[0] = "You placed the first order in the history of our company. Thank you for your service Mr.Johnson."
   database[9999] = "So this is actually the last order we can handle ever. Our package delivery service was moved to our portal division"
   #making a default responsee
   database[1] = "Your order will be there when it's ready. Stop rushing perfection (٭°̧̧̧ω°̧̧̧٭)"

#Database functions
def checkDBString(value, db):
   value = value.lower()
   value = value.strip()
   #Created a case for rejectiong
   if "none" in value or "no" in value:
      tooBad = "Unfortunate but we don't support any other orders here at the moment. Please feel free to take complaints to the complaint department on the -42984295th floor"
      return tooBad
   #base case for selected correct option
   elif value in db:
      return db[value]
   #Default non-compliance option
   else:
      sorry = "Not available which is definitely your fault and not mine at all (٭°̧̧̧ω°̧̧̧٭)"
      return sorry

def checkDB(value,db):
   if value == 0 or value == 9999:
      return db[value]
   else:
      value = 1
      return db[value]
   

def main():
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
    populateDBPersonalIdentifiers(psuedoDBPersonalIdentifiers)
    populateDBAddress(pseudoDBAddressTracker)
    populateDBOrderNum(pseudoDBOrderNumberTracker)
    # Counters for keeping track of failures in the individual processes
    choiceAErrorCounter = 0
    while operational:
      # Choice A
      # Initial Pass through should have unique dialog this will have additional conditions to account for repeated loop
      if choiceAErrorCounter == 0:
        print("To start off did you have a package you were looking for?")
        choiceA = input("Please respond with a yes or no: ")
      # Successful dialog
      if yesNoCheck(choiceA):
          print("\nI'm sorry our delivery service has you worried (╥﹏╥) Please allow me to assist you!")
      # Successfully failed dialog
      elif choiceAErrorCounter <2:
          choiceAErrorCounter += 1
          print("Here, I'll let you have another go at it!")
          choiceA = input("You're sure that there's no package we can help you keep track of?(Yes/No): ")
      # Maliciously or poorly accounted for failure state
      elif choiceAErrorCounter == 2:
         print("I'm sorry we weren't able to assist you please have a great day!")
         print("This program will now self destruct")
         operational = False
         break
      
      # Choice B method of determining how to find package status
      print("So I know of three ways to find out where your missing package may be ")
      print("Option A: Look it up by Name and information")
      print("Option B: Find the order based on the address you wanted it shipped to")
      print("Option C: If you have the order number we can try to look it")
      choiceB = input("So what option would you like to go with A, B or C?: ")
      choiceBOutPutter = optionChecker(choiceB)
      if choiceBOutPutter == 0:
        print("Ah you've selected option A the name and info option eh? Very well let's get down to business!")
        print("Hmm so I'm only seeing like three orders in here so unless your name is Billy, Jimmy or Raquel you might be out of luck here")
        nameSelect = input("What name did you want to look up?: ")
        print("Hmm beep boop. I'm definitely computing it right now...")
        print("You chose to look up: " + nameSelect)
        print("The order status is: " + checkDB(nameSelect))

      elif choiceBOutPutter == 1:
         print("Ooh going with Option B the address checker? An excellent choice!")
         print ("There are only three locations I'm seeing on hand so try to stick to those please? (๏ᆺ๏υ)")
         print("The locations I'm seeing are California, San Jose and San Francisco")
         print("Do any of those sound like yours?")
         addressSelect = input("If so which one is yours?: ")
         print("Hmm beep boop. I'm definitely computing it right now...")
         print("You chose to look up: " + addressSelect)
         print("The order status is: " + checkDB(addressSelect))
      elif choiceBOutPutter == 2:
         print("Yay option C! Lets get the order number ready for checking!")
      else:
         print("How strange it appears your option selection has opened a rip in the spacetime contiunum and taken you back to a previous choice!")
         print("So I know of three ways to find out where your missing package may be ")
         print("Option A: Look it up by Name and information")
         print("Option B: Find the order based on the address you wanted it shipped to")
         print("Option C: If you have the order number we can try to look it")
         choiceBError = 0
         while choiceBError <3 and choiceBOutPutter > 2:
            choiceBError +=1
            choiceB = input("Lets try getting that option input from you again shall we?")
            choiceBOutPutter = optionChecker(choiceB)
         if choiceBError == 3:
            print("Hmm sorry we couldn't figure out the option you selected and it's probably your fault. Why don't you try our Customer service line at 888-888-8888")
            print("This program will now self destruct")
            operational = False
            break
      #Now we'd query database if it existed but I'll just make some simple functions

if __name__ == "__main__":
    main()