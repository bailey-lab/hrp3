import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

matched_reads = set()

inputfile = open(input_file, 'r')
lines = inputfile.readlines()
for line in lines:
    line_array = line.split('\t')
    chromosome = line_array[2]
    if chromosome != "*":
        matched_reads.add(line_array[0])

output_file1 = open(output_file, "w+")
for read in matched_reads:
    output_file1.write(read)
    output_file1.write('\n')

output_file1.close()
