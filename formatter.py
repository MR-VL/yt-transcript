input_file = "transcript.txt"   # Input file path
output_file = "transcriptFormatted.txt" # Output file path
line_length = 125           # Number of characters per line

with open(input_file, "r") as infile, open(output_file, "w") as outfile:
    # Read the entire content of the file
    text = infile.read().strip()
    
    # Split the text into chunks of `line_length` characters
    for i in range(0, len(text), line_length):
        # Write a chunk of text to the output file
        outfile.write(text[i:i+line_length] + "\n")
        # Write an empty line
        outfile.write("\n")

print("Output file created with empty lines between each split. Check:", output_file)