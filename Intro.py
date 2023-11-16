#!/usr/bin/python3

#importing tthe os, system and subprocess modules

import os, sys, subprocess, time

# Introductory message to interact with the user and a brief description of what the programme does. In additio, there is a for loop that takes the variable and 'types' it out. The time module imports the sleep submodule and further aids in creating an effect of typing out the message

Intro_message = ("Welcome to the generic Python 3 programme/Script.\n The programme performs various processes on a set of protein fasta files.\n The user inputs the taxonomic identifier and the protein name which is then taken in for further processing.")

for char in Intro_message:
    time.sleep(0.020)
    sys.stdout.write(char)
    sys.stdout.flush()

# while True loop to interact with the user to determine whether or not to continue with the programme. If the user inputs 'y' or 'Y', the programme sends a brief message to the user indicating that the programme has received the input and would proceed.There is an interactive "countdown" which ticks into initialising the process and the the loop breaks. If the user inputs 'n' or 'N' the programme sends a message indicating that the programme will no longer continue and stops.There is an 'easter egg' included to make the programme seem more user interactive and includes a 'maybe' as an input that indicates the user to "make up your mind numpty!!!" xD

while True:
    ans = input("\nWould you like to process further? (y or n)\n").lower()
    if ans == 'y' or ans == 'yes'  :
        print("Initialising Programme countdown...")
        time.sleep(1)
        print("beep boop beep boop")
        time.sleep(1)
        print("5.....")
        time.sleep(0.5)
        print("4....")
        time.sleep(0.5)
        print("3...")
        time.sleep(0.3)
        print("2..")
        time.sleep(0.2)
        print("1.")
        time.sleep(0.1)
        print("Hey ho! Let's go!!!")
        break
    elif ans == 'n' or ans == 'no' :
        print("Exiting programme ...")
        time.sleep(1)
        sys.exit("Ok! Have a good day bye!!!")
        time.sleep(1)
    elif ans == 'maybe' :
        print("Make up your mind numpty!!!")
    else :
        print("Haha! Very funny! Pick y or n")

# The next while True loop requires the user to input the name of the taxonomic group of interest. The while true loop negates any integer/numerical value and requests the user to provide an alphabetical value instead. The taxonomic group then gets stored as a variable which then gets used later for esearch and efetch 
time.sleep(1)
while True:
    print("The programme requires 2 inputs from the user")
    while True:
        taxon_group = input("Enter your taxonomical group \n").replace(" ", "_").lower()
        if not taxon_group.isalpha() :
            print("Please type an alphabetical value")    
        else :
            print("\nThis is your taxonomical group:", taxon_group)
            break

    # This while True loop interacts with the user to provide a protein name and negates any standalone integer values. The input is stored as a variable and hgets used for esearch and efetch
    time.sleep(1)
    while True:    
        protein = input("Enter your protein name\n").lower()
        protein_name=protein.replace(" ", "_")
        if protein_name.isdigit() : 
            print("Please input a valid protein name:")
        else :
            print("\nYour protein name is:" ,protein)
            break

    # This print statement prints the user input taxonomical group and protein name by calling their variables. 
    time.sleep(1)
    Inputs = ("\n\nYour input Taxon group is:" ,taxon_group, "\nYour input Protein name is:",protein)
    for char in Inputs:
        time.sleep(0.020)
        sys.stdout.write(char)
        sys.stdout.flush()

    Totalcount = False
    totalseq = f"esearch -db protein -query '{protein_name}[protein] AND {taxon_group}[orgn] NOT partial' | xtract -pattern Count -element Count"
    total = int(subprocess.run(totalseq, shell=True, capture_output=True, text=True).stdout.strip())
    if total == 0 or total == 1:
        print("\nInadequate number of sequences")
        Totalcount = True
        continue
    elif total > 1000 or total == 1000:
        total = 1000
    
    print("\nTotal number of sequences for your input taxonomical group and protein is: ", total)
        
    if Totalcount:
       break

    time.sleep(0.5)
    Status = ("\n\n Searching NCBI Protein and fetching output fasta format...")
    for char in Status:
        time.sleep(0.020)
        sys.stdout.write(char)
        sys.stdout.flush()

    fetchfasta = f"esearch -db protein -query '{protein_name}[Protein] AND {taxon_group}[Organism] NOT PARTIAL' | efetch -format fasta -start 1 -stop {total} > {protein_name}_{taxon_group}.fasta"
    os.system(fetchfasta)

    Outputstatus = (f"\n\nYour output fasta file is {protein_name}_{taxon_group}.fasta")
    for char in Outputstatus:
        time.sleep(0.020)
        sys.stdout.write(char)
        sys.stdout.flush()


    print("\nList of species are:")

    Species = f'cat {protein_name}_{taxon_group}.fasta | grep ">" | awk -F\'[][]\' \'{{print$2}}\' | uniq -c | sort -nr'

    os.system(Species)
    
    Satisfied = False
    while True:
        Proceed = input("Are you satisfied with the resulting dataset? y/n \n").lower()
        if Proceed == 'no' or Proceed  == 'n':
            print("Ok! Let us reroute you to input your taxon and protein of interest")
            break
        elif Proceed  == 'yes' or Proceed == 'y':
            Satisfied = True
            break
        else :
            print("Make up your mind numpty!!!")
        
    if Satisfied:
        break

print("Assuming you are content,let us continue")

print("\n")
print("The programme will now align the fasta file using clustalo and further use plotcon to plot a graph")


MSA = f"clustalo -i '{protein_name}_{taxon_group}.fasta' -o '{protein_name}'_'{taxon_group}'_Aligned.fasta --auto  -v --force" 

os.system(MSA)

print("\n Your output Aligned file is saved as '{protein_name}'_'{taxon_group}'_Aligned.fasta")

size = input("\nPlease input a window size for the plot graph\n")

Plot = f"plotcon -sequences '{protein_name}'_'{taxon_group}'_Aligned.fasta -graph png -winsize '{size}' -goutfile Align'{size}' --auto"

os.system(Plot)



