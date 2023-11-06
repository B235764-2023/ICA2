#!/usr/bin/python3

print("Welcome to the generic Python 3 programme/Script.\n The programme performs various processes on a set of protein fasta files.\n The user inputes the taxonomic identifier and the protein name which is then taken in for further processing.")

while True:
    ans = input("Would you like to process further? (y or n)\n").lower()
    if ans == 'y' or ans == 'yes'  :
        print("Hey ho! Let's go!!!")
        break
    elif ans == 'n' or ans == 'no' :
        print("Ok. Have a good day! Bye!")
        break
    elif ans == 'maybe' :
        print("Make up your mind numpty!!!")
    else :
        print("Haha! Very funny! Pick y or n")

print("The programme requires 2 inputs from the user")
while True:
    taxon_group = input("Enter your taxonomical group \n")
    if taxon_group.isalpha() :
        print("This is your input taxonomical group :",taxon_group)
        break
    elif taxon_group.isdigit() or taxon_group.isnumeric() or taxon_group.isspace():
        print("Please type an alphabetical value")

while True:
    protein_name = input("Enter your protein name\n").lower()
    if protein_name.isalpha() :
        print("This is your input protein name :",protein_name)
        break
    elif protein_name.isdigit() or protein_name.isnumeric() or protein_name.isspace():
        print("Please type an alphabetical value")

print("\nYour input Taxon group is:" ,taxon_group, "\nYour input Protein name is:",protein_name)
