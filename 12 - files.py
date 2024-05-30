#5-30-2024

#open file so that file is read
#club_file = open("club.txt", 'r')
club_file = open('club.txt', 'a')

#print every member 
#for member in club_file.readlines():
    #print(member)

#now use append to add a member
club_file.write('\nSana - Social Media')
#create a new .txt file

club_file = open('club1.txt', 'w')
#write to that file the updated member list 2024
club_file.write('2024 list')
club_file.write('\n millie - vice president \nwardiyah - president')
#create a .html file with the updated member list
club_file = open('club.html', 'w')
#close file
club_file.close()