#!/usr/bin/python3

print("Welcome to the generic Python 3 programme/Script.\n The programme performs various processes on a set of protein fasta files.\n The user inputes the taxonomic identifier and the protein name which is then taken in for further processing.")

while True:
    ans = input("Would you like to process further? (y or n)\n")
    if ans == 'y' or ans == 'Y'  :
        print("Hey ho! Let's go!!!")
        break
    elif ans == 'n' or ans == 'N' :
        print("Ok. Have a good day! Bye!")
        break
    elif ans == 'maybe' :
        print("Make up your mind numpty!!!")
    else :
        print("Haha! Very funny! Pick y or n")

