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
    taxon_group = input("Enter your taxonomical group \n").replace(" ", "_").lower()
    if taxon_group.isdigit() or taxon_group.isnumeric() :
        print("Please type an alphabetical value")
    else :
        print("This is your taxonomical group:", taxon_group)
        break

while True:
    protein = input("Enter your protein name\n").lower()
    protein_name=protein.replace(" ", "_")
    if protein.isdigit() :
        print("Please input a valid protein name:")
    else :
        print("Your protein name is:" ,protein)
        break

print("\nYour input Taxon group is:" ,taxon_group, "\nYour input Protein name is:",protein_name)

import os

fetchfasta = f'esearch -db protein -query "{protein_name}[Protein] AND {taxon_group}[Organism] NOT PARTIAL" | efetch -format fasta > {protein_name}_{taxon_group}.fasta'

os.system(fetchfasta)

print("Your output fasta file is",f"\n{protein_name}_{taxon_group}.fasta")

