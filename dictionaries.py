#5-26-24
#key-value pairs

#use a dictionary to convert three letter abbreviation for month to full month name

months={
    "JAN" : "January",
    "FEB" : "February",
    "MAR" : "March",
    "APR" : "April",
    "MAY" : "May",
    "JUN" : "June",
    "JUL" : "July",
    "AUG" : "August",
    "SEP" : "September",
    "OCT" : "October", 
    "NOV" : "November", 
    "DEC" : "December"
}

abbreviation = input('Enter any three letter abbreviation for a month: ').upper()

print("Full month: " + months[abbreviation])

#use .get() function
print(months.get(abbreviation, "Not a vlid key"))