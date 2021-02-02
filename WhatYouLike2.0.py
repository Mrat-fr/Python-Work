import pandas as pd # This puts in pandas to sort out the data
df = pd.read_json("train.json")#will open and read the train file, also
data = df.to_dict()# making df into a dictionary
 
like_list = []# This is going to be the list where everything they like will be stored
dislike_list = []# This is going to be the list where everything they don't like will be stored
like = 0 #created this so the while loop would work
dislike = 0#created this so the while loop would work
#This section will take the like ingredients that has been inputted then store it in the list
print ("----      CUISINES YOU LIKE       ----")#The title, just visual
print ("----    select '/' to move on     ----")#tells the person to input / to move on
print ("----       INGREDIENTS LIKE       ----")#title to them to input what they like
while like != "/":#this is going to loop to let them put as many like ingredients until they don't  want no more, then press / to move on
  like = input(">>>")# asks the user to input what they want
  like_list.append(like)# adds what the user inputs into the likelist
print ("----     INGREDIENTS DISLIKE      ----")#title to them to input what they dislike
while dislike != "/":#this is going to loop to let them put as many dislike ingredients until they don't want no more, then press / to move on
 dislike = input(">>>")# asks the user to input what they don't want
 dislike_list.append(dislike)# adds what the user inputs into the dlikelist

#This section will take both list and print likelist while removing any that has dlikelist within the cuisine ingredients
for x in data['id']:# This will look at the dictionary and specifically id section
 for t in like_list:# This will look at all the id and see which on contain anything from likelist
   if t in data['ingredients'][x] and t not in dislike_list:# This then will look to and makes sure it does not include anyone that has dislike ingredient
     print("cuisine: ", data['cuisine'][x], "the id is: ", data['id'][x], "The ingredient is: ", t)#Then this will print everything that is left and format it to show the cuisine and the id along with the like ingredient that it contains
