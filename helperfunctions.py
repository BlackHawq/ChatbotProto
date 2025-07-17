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
   if value.isNumeric():
      if int(value) == 0 or int(value) == 9999:
         response = db[value]
   else:
      print("Hmm so I'm just going to look up order number 1 regardless of what you type here since I don't want to deal with error checking")
      value = 1
      response = db[value]
   return response
   
