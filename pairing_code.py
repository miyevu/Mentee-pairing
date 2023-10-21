# Function to read names or interests from a file and return a list
def read_file(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file]

# Read names and interests from files
names = read_file('names.txt')
interests = read_file('interests.txt')

# Create a dictionary to store matches
matches = {}

# Iterate through names and interests to find matches
for name in names:
    for interest in interests:
        if interest not in matches:
            matches[interest] = []
        matches[interest].append(name)

# Write the matches to an output file
with open('matched_results.txt', 'w') as output_file:
    for interest, matched_names in matches.items():
        output_file.write(f"People interested in {interest}:\n")
        output_file.write('\n'.join(matched_names) + '\n\n')

print("Matching completed. Results written to 'matched_results.txt'.")
