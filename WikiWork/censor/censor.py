import csv
import string


#I use a csv file (with the path provided by the user) to create a dict of curses and their alternatives
curses = {}
f_path = raw_input("Enter path to csv file with censored words and their substitutes. \nEach line in the csv file should be in the format curseword, alternative \n")
curse_list = csv.reader(open(f_path))
for row in curse_list:
    curses[row[0]] = row[1] 


f_path = raw_input("Enter text file you want censored. \n") #getting the text file to be censored
text = open(f_path, 'r') 
new_text = "" #What will become the censored text

for line in text:
    for key,value in curses.iteritems():
        line = string.replace(line, key,value) #I use python's built-in replace function - someone else can do the search/replace by hand!
    new_text += line

    #This part - erasing the old text and writing the new text - is a little messy because I can't figure out how to edit
    #a text with reading/writing in one step in python.  Is there a simpler way to do this?
text.close()
text = open(f_path, 'w')
text.write(new_text)
text.close()
print("The file has been changed")
