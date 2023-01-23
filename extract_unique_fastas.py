import sys

input_file = sys.argv[1]
read_file = sys.argv[2]
file1 = open(input_file, 'r')
lines = file1.readlines()

unique_reads = set()
read_files1 = open(read_file, 'r')
read_lines = read_files1.readlines()

for line in read_lines:
    unique_reads.add(line.replace("\n",""))

output_file1 = open(sys.argv[3], "a")
count = 0
isTargetRead = False
for line in lines:
    count += 1
    if count == 1:
        read = line.split(" ")[0].replace("@","")
        if read in unique_reads:
            isTargetRead = True
            output_file1.write(line)
    if count == 2:
        if isTargetRead == True:
            output_file1.write(line)
    if count == 3:
        if isTargetRead == True:
            output_file1.write(line)
    if count == 4:
        if isTargetRead == True:
            output_file1.write(line)
        count = 0
        isTargetRead = False

output_file1.close()
