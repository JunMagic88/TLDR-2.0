# Search and download eBooks from Libgen 
# Need to git clone this: https://github.com/viown/libgen-dl

from libgenesis import Libgen
import asyncio, subprocess, os


# Create libgen object
lg = Libgen(sort= 'year', sort_mode= 'DESC', result_limit= '1')

# Open the 'Booklist.txt' file
with open('Booklist.txt') as f:
    # Read the lines of the file into a list
    lines = f.readlines()

# Convert the list of lines into a list of book names
booklist = [line.strip() for line in lines]
print("Booklist is "+str(booklist)+'\n')

# for book in booklist 
#   while not chosen
#       keep showing the next available item 
#           if chosen, move to next book search
async def search():
    #bookMD5s = []

    for book in booklist: 
        # search for the book in libgen
        print("searching for..."+book+'\n')
        result = await lg.search(book)
        found = False
        for item in result: 
            if(result[item]['extension']=='epub'):
                print(result[item]['extension']+" | "+result[item]['year']+" | "+str(round(int(result[item]['filesize'])/1000000,1))+"MB | "+result[item]['title']+" | "+result[item]['language']+" | "+result[item]['author']+" | ")
                # ask the user if this is the one they want?
                while True:
                    user_input = input("This one? (Y/N) ")
                    if user_input == "Y" or user_input == "y":
                        found = True
                        subprocess.call(["python","libgen-dl/libgen-dl.py", result[item]['md5']])
                        os.system("move C:\\Users\\PlutoniaX\\Satoshi\\TLDR\\*.epub C:\\Users\\PlutoniaX\\Satoshi\\TLDR\\Books")
                        break
                    elif user_input == "N" or user_input == "n":
                        break
                    else: 
                        print("Invalid input. Please enter Y or N.")
                if found:
                    break

asyncio.run(search())
