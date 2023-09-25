# Modules
import os
import csv

# Set path for file
csvpath = os.path.join(os.getcwd(),"Resources", "election_data.csv")


# Declaring Variables
highestVote = 0
winnerName = ("")
total_votes = 0
voteCount = []
CandidateName = []


# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")
    csvheader = next(csvfile)
    # Loop through
    for col in csvreader:
        candidateNameIndex = -1
        total_votes = total_votes + 1

        # Identify index position of candidate name
        for i in range(len(CandidateName)):
            if col[2] == CandidateName[i]:
                candidateNameIndex = i

        if candidateNameIndex < 0:
            # Intializing candidate and vote in lists
            CandidateName.append((col[2]))
            voteCount.append(int(1))
        else:
            # Adding vote count of candidate 
            voteCount[candidateNameIndex]=voteCount[candidateNameIndex]+1

    # Creating txt file and redirecting output to it
    old_print = print
    log_file = open("output.txt", "w")
    print = lambda *args, **kw: old_print(*args, **kw) or old_print(*args, file=log_file, **kw)
    
    # Displaying results    
    print("Election Results\n")
    print("-------------------------\n")    
    print ("Total Votes: "+str(total_votes)+"\n")
    print("-------------------------\n")
    for i in range(len(CandidateName)):
        print(str(CandidateName[i])+": "+str("%.3f%%" % (100 * voteCount[i]/total_votes))+" ("+str(voteCount[i])+")\n")
        # finding winner
        if highestVote < voteCount[i]:
            highestVote = voteCount[i]
            winnerName = CandidateName[i]

    print("-------------------------\n")
    print ("Winner: "+str(winnerName)+"\n")
    print("-------------------------\n")

    # Closing File
    log_file.close()