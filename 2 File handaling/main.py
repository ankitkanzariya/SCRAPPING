# Step 1: Write 5 quotes to a text file
with open("quotes.txt", "w") as file:
    file.write("Quote 1: The best way to get started is to quit talking and begin doing.\n")
    file.write("Quote 2: Success is not in what you have, but who you are.\n")
    file.write("Quote 3: Dreams don’t work unless you do.\n")
    file.write("Quote 4: Push yourself, because no one else is going to do it for you.\n")
    file.write("Quote 5: Great things never come from comfort zones.\n")

#step 2 read this all quotes in text file
with open("quotes.txt", "r") as file:
    for line in file:
        print(line.strip())

#append more quotes
with open("quotes.txt","a") as file:
    file.write("quote 6: work hard untill you not feel prode.\n")

#read and check appended quotes
with open("quotes.txt", "r") as file:
    for line in file:
        print(line.strip())
