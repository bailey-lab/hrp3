import sys

input_file = sys.argv[1]
hybrid_11_13_file = sys.argv[2]
normal_11_file = sys.argv[3]
hybrid_13_11_file = sys.argv[4]
normal_13_file = sys.argv[5]

hybrid_11_13_reads = set()
normal_11_reads = set()
hybrid_13_11_reads = set()
normal_13_reads = set()

inputfile = open(input_file, 'r')
lines = inputfile.readlines()
for line in lines:
    line_array = line.split('\t')
    if len(line_array) >= 20:
        chromosome = line_array[2]
        begin_position = int(line_array[3])
        seq_length = len(line_array[9])
        end_position = None
        for item in line_array:
            if "YS:" in item:
                end_position = int(item.split(':')[2].strip('\n'))
        if chromosome == "Chromosome_1_hybrid":
            #looks for spanning reads (at least 2000 bps into each side)
            #1914041 = serine/threonine protein kinase
            #1934199 = probable protein
            #if begin_position < 1914041 and end_position > 1934199:
            if begin_position < 1917979 and end_position > 1933440:
                hybrid_11_13_reads.add(line_array[0])
        if chromosome == "Pf3D7_11_v3":
            #looks for spanning reads
            #1914041 = serine/threonine protein kinase
            #1933278 = PHISTc
            #if begin_position < 1914041 and end_position > 1933278:
            if begin_position < 1917979 and end_position > 1933440:
                normal_11_reads.add(line_array[0])
        if chromosome == "Chromosome_3_hybrid":
            #looks for spanning reads
            #2789345 = hrp1
            #2782677 = serine/threonine protein kinase
            #if begin_position < 2789345 and end_position > 2807277:
            if begin_position < 2791972 and end_position > 2807447:
                #print(line_array[0])
                #print(end_position)
                hybrid_13_11_reads.add(line_array[0])
        if chromosome == "Pf3D7_13_v3":
            #looks for spanning reads
            #2789345 = hrp1
            #2808200 = probable protein
            #if begin_position < 2789345 and end_position > 2808200:
            if begin_position < 2791972 and end_position > 2807447:
                #print("NO!!!")
                normal_13_reads.add(line_array[0])

output_file1 = open(hybrid_11_13_file, "w+")
for read in hybrid_11_13_reads:
    output_file1.write(read)
    output_file1.write('\n')
print("hybrid_11_13:")
print(len(hybrid_11_13_reads))
print("\n")

output_file2 = open(normal_11_file, "w+")
for read in normal_11_reads:
    output_file2.write(read)
    output_file2.write('\n')
print("normal 11:")
print(len(normal_11_reads))
print("\n")

output_file3 = open(hybrid_13_11_file, "w+")
for read in hybrid_13_11_reads:
    output_file3.write(read)
    output_file3.write('\n')
print("hybrid_13_11_reads:")
print(len(hybrid_13_11_reads))
print("\n")

output_file4 = open(normal_13_file, "w+")
for read in normal_13_reads:
    output_file4.write(read)
    output_file4.write('\n')
print("normal 13:")
print(len(normal_13_reads))
print("\n")

output_file1.close()
output_file2.close()
output_file3.close()
output_file4.close()
