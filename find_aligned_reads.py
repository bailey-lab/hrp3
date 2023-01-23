import sys

input_file_begin = sys.argv[1]
input_file_end = sys.argv[2]
bed_file = sys.argv[3]
target_begin_chromosome = sys.argv[4]
target_end_chromosome = sys.argv[5]
base_length = int(sys.argv[6])
output_file = sys.argv[7]

bed_file1 = open(bed_file, 'r')
bed_lines = bed_file1.readlines()

global_begin_position = 'N/A'
global_end_position = 'N/A'

begin_seq_length = 0
end_seq_length = 0

for line in bed_lines:
    chromosome = line.split('\t')[0]
    if chromosome == target_begin_chromosome:
        global_begin_position = int(line.split('\t')[1])
        begin_seq_length = int(line.split('\t')[4])
    if chromosome == target_end_chromosome:
        global_end_position = int(line.split('\t')[2])
        print(target_end_chromosome)
        print(global_end_position)
        end_seq_length = int(line.split('\t')[4])

shared_seq_length = min(begin_seq_length, end_seq_length)
#output_file = open(sys.argv[4], "w+")

begin_reads = set()

file_begin = open(input_file_begin, 'r')
lines = file_begin.readlines()
for line in lines:
    line_array = line.split('\t')
    begin_position = int(line_array[3])
    seq_length = len(line_array[9])
    if begin_position <= global_begin_position - base_length and begin_position >= global_begin_position + shared_seq_length - seq_length:
        begin_reads.add(line_array[0])

matched_reads = set()

file_end = open(input_file_end, 'r')
lines = file_end.readlines()
for line in lines:
    print(line)
    line_array = line.split('\t')
    end_position = int(line_array[3])
    seq_length = len(line_array[9])
    if end_position >= global_end_position and end_position <= global_end_position + seq_length:
        if line_array[0] in begin_reads:
            matched_reads.add(line_array[0])

output_file1 = open(output_file, "a")
for read in matched_reads:
    output_file1.write(read)
    output_file1.write('\n')

output_file1.close()
