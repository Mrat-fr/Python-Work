import pandas as pd # This puts in pandas to sort out the data
df = pd.read_json("train.json")#will open and read the train file, also
data = df.to_dict()# making df into a dictionary
 
likelist = []# This is going to be the list where everything they like will be stored
dlikelist = []# This is going to be the list where everything they don't like will be stored

#This section will take the like ingredients that has been inputted then store it in the list
print         ("----      CUISINES YOU LIKE       ----")#The title, just visual
choice = input("Choose what ingredient you would like:")# asks the user to input what they want
likelist.append(choice)# adds what the user inputs into the likelist
print         ("-----     select '1' to move on     -----")#This is what's going to break the loop so tell them how to do it
  
while choice != "1":#this is going to loop to let them put as many like ingredients until they dont want no more, then press 1 to move on
  choice = input("select another ingredient you would like: ")# asks the user to input what they want
  likelist.append(choice)# adds what the user inputs into the likelist

#This section will take the like ingredients that has been inputted then store it in the list
choice2 = input("Choose what ingredient you would not like:")# asks the user to input what they don't want
dlikelist.append(choice2)# adds what the user inputs into the dlikelist
print         ("-----     select '1' to move on     -----")#This is what's going to break the loop so tell them how to do it

while choice2 != "1":#this is going to loop to let them put as many dislike ingredients until they don't want no more, then press 1 to move on
 choice2 = input("select another ingredient you would not like: ")# asks the user to input what they don't want
 dlikelist.append(choice2)# adds what the user inputs into the dlikelist

#This section will take both list and print likelist while removing any that has dlikelist within the cuisine ingredients
for x in data['id']:# This will look at the dictionary and specifically id section
 for t in likelist:# This will look at all the id and see which on contain anything from likelist
   if t in data['ingredients'][x] and t not in dlikelist:# This then will look to and makes sure it does not include anyone that has dislike ingredient
     print("cuisine: ", data['cuisine'][x], "the id is: ", data['id'][x], "The ingredient is: ", t)#Then this will print everything that is left and format it to show the cuisine and the id along with the like ingredient that it contains
