#!/usr/bin/python3

#importing tthe os, system and subprocess modules for running commands. The matplotlib module has also been imported to display the image

import os, sys, subprocess, time
from matplotlib import pyplot as plt
from matplotlib import image as mpimg

cwd = os.getcwd()
wd = cwd + "/Generic_Python3_Script/"
os.mkdir(wd)
os.chdir(wd)

# Introductory message to interact with the user and a brief description of what the programme does. In addition, there is a for loop that takes the variable and 'types' it out. The time module imports the sleep submodule and further aids in creating an effect of typing out the message

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
    
    #This bit of code essentially uses esearch and finds out the total number of hits found in NCBI Protein database and provides the count. If the count is less than or equal to 1, the loop does not continue further and asks the user to input the values for taxonomic group and protein name again. If the count is greater than 1000, the count is set as 1000 to retrieve exactly 1000 sequences for the given input to be taken for further processing
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
    
   #Just a message to show what process is being carried out by the programme

    time.sleep(0.5)
    Status = ("\n\n Searching NCBI Protein and fetching output fasta format...")
    for char in Status:
        time.sleep(0.020)
        sys.stdout.write(char)
        sys.stdout.flush()
    
    #This is the actual bit in charge of searching and retrieving fasta sequences from NCBI Protein. The Input taxonomical group and protein name are stored as variables and get included here in the search and retrieve parameters

    fetchfasta = f"esearch -db protein -query '{protein_name}[Protein] AND {taxon_group}[Organism] NOT PARTIAL' | efetch -format fasta -start 1 -stop {total} > {protein_name}_{taxon_group}.fasta"
    os.system(fetchfasta)

    Outputstatus = (f"\n\nYour output fasta file is {protein_name}_{taxon_group}.fasta")
    for char in Outputstatus:
        time.sleep(0.020)
        sys.stdout.write(char)
        sys.stdout.flush()


    print("\nList of species are:")
    
    #This bit uses grep to scan through the fasta file and lists out the species in decreasing order of occurence and lists more repeating species on top

    Species = f'cat {protein_name}_{taxon_group}.fasta | grep ">" | awk -F\'[][]\' \'{{print$2}}\' | uniq -c | sort -nr'

    os.system(Species)
    
    #This bit asks if the user is satisfied with the current dataset or not. If the user gives no, the loop breaks and reroutes the whole section goes back to asking the user for input again. The flag is set as false before entering a while true loop and is only changed when input is yes. This forces the loop to break and proceed further

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

#Using clustalo to Multiple sequence Align the fasta sequences fully with one iteration and kimura corrected. -v-v provides a detailed description of the process and updates the user. 

MSA = f"clustalo -i '{protein_name}_{taxon_group}.fasta' --full --full-iter --iter=1 --use-kimura -o '{protein_name}'_'{taxon_group}'_Aligned --outfmt=fa --force --threads=50 -v -v" 

os.system(MSA)

print(f"\n Your output Aligned file is saved as {protein_name}_{taxon_group}_Aligned.fasta")

#This bit takes the user input for a window size for plotting a graph and stores it into a variable. The variable then gets input into the command

size = input("\nPlease input a window size for the plot graph\n")

Plot = f"plotcon -sequences '{protein_name}'_'{taxon_group}'_Aligned -graph png -winsize '{size}' -goutfile Align'{size}' --auto"

os.system(Plot)

print(f" Your graph is stored as Align{size}.1.png")

print("Please wait while your image is being displayed")
print("This could take a while")

#using the matplotlib imported initially, this bit uses functions in it to display the output png image from plotcon

image = mpimg.imread(f"Align{size}.1.png")
plt.imshow(image)
plt.axis('off')
plt.show()

#This lengthy section of code initiates by creating two distinct directories. One for storing all fasta files and the other for storing all patmatmotif files. The code takes the input fasta file and seperates each sequence present in it and saves each sequence as a seperate fasta file in the directory for individual fasta files. The code then runs patmatmotif on each individual fasta file and generates multiple .patmatmotif files and stores them in the directory for each patmatmotif file. The code then assimilates each patmatmotif file and creates one huge patmatmotif file with the list of domains of all sequences. The grep command in the end then goes to search the combined motif file and counts the specific motif and stores them in a seperate file

fasta_dir = "Individual_fasta_files"
os.mkdir(fasta_dir)

patmatmotif_dir = "patmatmotif_outputs"
os.mkdir(patmatmotif_dir)

with open(f"{protein_name}_{taxon_group}.fasta") as my_file:
    fasta_file_contents = my_file.read()

list_fasta_seqs = [">" + seq \
                    for seq in fasta_file_contents.split(">") if seq]

for i,seq in enumerate(list_fasta_seqs, start=1):
    file_path = os.path.join(fasta_dir, f"seq_{i}.fasta")
    with open(file_path,"w") as output_file:
        output_file.write(seq)

for file in os.listdir(fasta_dir):
    if file.endswith(".fasta"):
        individual_fasta_file_path = os.path.join(fasta_dir, file)
        output_file_path = os.path.join(patmatmotif_dir, f"{file}.patmatmotifs")

    try:
        with open(output_file_path,"w") as output_file:
            subprocess.run(f"patmatmotifs -sequence {individual_fasta_file_path} -full -outfile {output_file_path}", shell=True)
    except:
        print(f"\n Error in processing patmatmotif files")

combined_output_filename = "combined_patmatmotifs_result.txt"

with open(combined_output_filename, "w") as combined_file:
    for output_filename in os.listdir(patmatmotif_dir):
        if output_filename.endswith(".patmatmotifs"):
            output_file_path = os.path.join(patmatmotif_dir, output_filename)

            with open(output_file_path, "r") as output_file:
                combined_file.write(output_file.read() + "\n")

Allmotifs = f"cat combined_patmatmotifs_result.txt | grep Motif | cut -d'=' -f2 | sort | uniq -c | sort -nr > List_of_Motifs.txt"

subprocess.run(Allmotifs, shell=True, check=True)

print("\n All patmatmotifs results are combined into combined_patmatmotifs_result.txt")

print("\n List of all motifs is stored in List_of_Motifs.txt")

print("This next bit will convert your list of input protein fasta sequences into Nucleotide sequences which can later be used for further analysis")

#This bit uses an EMBOSS backtranseq programme which converts protein sequences into their corresponding initial Nucleotide codons. This can be used for future further processing in terms of evolutionary analyses, BLAST, similarity etc. This adds relevant biological data that can be later used for parallel analyses. 

PtoN =f" backtranseq -sequence '{protein_name}_{taxon_group}.fasta' -cfile Ehuman.cut -outfile Nucleotide_sequences"
os.system(PtoN)

print("\n List of all Nucleotide codons for all sequences is stored in Nucleotide_sequences")


Outro_message = "This brings us to the end of the Programme.\n Hope this Generic Python3 Programme/Script was useful in providing you the required data and was helpful.\n See ya!\n"

for char in Outro_message:
    time.sleep(0.080)
    sys.stdout.write(char)
    sys.stdout.flush()

