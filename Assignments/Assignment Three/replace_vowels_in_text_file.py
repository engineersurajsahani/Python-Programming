# Replace vowels with '*' in a text file
input_file = 'input.txt'
output_file = 'output.txt'

with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
    for line in infile:
        modified_line = ''.join('*' if char.lower() in 'aeiou' else char for char in line)
        outfile.write(modified_line)
