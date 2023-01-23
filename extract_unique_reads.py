import sys

input_file = sys.argv[1]

file1 = open(input_file, 'r')
lines = file1.readlines()

count = 0
unique_reads = set()
for line in lines:
    count += 1
    read = line.split('\t')[0]
    unique_reads.add(read)

output_file1 = open(sys.argv[2], "w+")
for read in unique_reads:
    output_file1.write(read)
    output_file1.write('\n')

output_file1.close()
