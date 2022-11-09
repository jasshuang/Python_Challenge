import csv
import os

#define the variables
total_vote = 0
candidates= []
results= {}

#open the csv file
with open('election_data.csv','r') as file:
    reader = csv.reader(file, delimiter= ',')
    
    #skip the header
    header = next(reader)


    for row in reader:

        #counting the total rows
        total_vote  +=1

        #add candidates to the list
        current_candidate = row[2]
        #if the candiate is not in the list, add the name to the list and reset the vote counts
        if current_candidate not in candidates:
            candidates.append(current_candidate)
            results[current_candidate] = 0
        
        #if the candidate is in the list, add 1 to the vote counts
        else:
            results[current_candidate] += 1



winner = max(results, key = results.get)
    

#print the report
print("Election Results")
print("----------------------------------------")
print(f"Total Votes: {total_vote }" )
print("----------------------------------------")
for c in candidates:
    print(f'{c}: {round(results[c]*100/total_vote,3)}% ({results[c]})')
print(f'Winner: {winner}!')


# save the output file path
output_file = os.path.join("output.txt")

# open the output file, create a header row, and then write the zipped object to the csv
with open(output_file, "w") as pypoll_output:
    writer = csv.writer(pypoll_output)

    writer.writerow(["Election Results"])
    writer.writerow(["----------------------------------------"])
    writer.writerow([f"Total Votes: {total_vote }"] )
    writer.writerow(["----------------------------------------"])
    for c in candidates:
       writer.writerow ([f'{c}: {round(results[c]*100/total_vote,3)}% ({results[c]})'])
    writer.writerow([f'Winner: {winner}!'])




