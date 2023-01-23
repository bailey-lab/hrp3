import sys

input_file_1 = sys.argv[1]
input_file_2 = sys.argv[2]
bed_file = sys.argv[3]
output_file = sys.argv[4]

bed_file1 = open(bed_file, 'r')
bed_lines = bed_file1.readlines()

i = 0
bed_chr1 = "N/A"
bed_chr2 = "N/A"
bed_chr1_begin_pos = "N/A"
bed_chr2_begin_pos = "N/A"
bed_chr1_end_pos = "N/A"
bed_chr2_end_pos = "N/A"

for line in bed_lines:
    line_array = line.split('\t')
    if i == 1:
        bed_chr1 = line_array[0]
        bed_chr1_begin_pos = (int(line_array[1]) + int(line_array[2]))/2
        bed_chr1_end_pos = int(line_array[2])
    if i == 2:
        bed_chr2 = line_array[0]
        bed_chr2_begin_pos = (int(line_array[1]) + int(line_array[2]))/2
        bed_chr2_end_pos = int(line_array[2])
    i += 1

#first part of chromosome contains beginning to (chr1_begin_pos - 1)
chr1 = ""
chr1_part1= ""
#second part of chromosome contains chr1_begin_pos to end of chromosome
chr1_part2 = ""

chr2 = ""
chr2_part1= ""
chr2_part2 = ""

input_file1 = open(input_file_1, 'r')
input_lines1 = input_file1.readlines()

j = 0
input_file1_chr_name = ""
input_file_no_line_breaks = ""
for line in input_lines1:
    if j == 0:
        input_file1_chr_name = line.replace("\n", "")
    if j != 0:
        no_line_breaks = line.replace("\n", "")
        input_file_no_line_breaks += no_line_breaks
    j += 1

input_file2 = open(input_file_2, 'r')
input_lines2 = input_file2.readlines()

k = 0
input_file2_chr_name = ""
input_file2_no_line_breaks = ""
for line in input_lines2:
    if k == 0:
        input_file2_chr_name = line.replace("\n", "")
    if k != 0:
        no_line_breaks2 = line.replace("\n", "")
        input_file2_no_line_breaks += no_line_breaks2
    k += 1

temp_chr1 = ">" + bed_chr1
temp_chr2 = ">" + bed_chr2
if input_file1_chr_name == temp_chr1 and input_file2_chr_name == temp_chr2:
    chr1_part1 = input_file_no_line_breaks[0:bed_chr1_begin_pos]
    chr1_part2 = input_file_no_line_breaks[bed_chr1_begin_pos:len(input_file_no_line_breaks)]
    chr2_part1 = input_file2_no_line_breaks[0:bed_chr2_begin_pos]
    chr2_part2 = input_file2_no_line_breaks[bed_chr2_begin_pos:len(input_file2_no_line_breaks)]
else:
    print("Wrong Order of Bed File")

final_chr1 = chr1_part1 + chr2_part2
final_chr2 = chr2_part1 + chr1_part2

output_file_write = open(output_file, "w")

#chr1
final_chr1_name = ">" + "Chromosome_1_hybrid" + " (" + bed_chr1 + ":0-" + str(bed_chr1_begin_pos) + " + " + bed_chr2 + ":" + str(bed_chr2_begin_pos) + "-end" + ")"
output_file_write.write(final_chr1_name)
output_file_write.write("\n")
output_file_write.write(final_chr1)
output_file_write.write("\n")

print(final_chr1_name)

#chr2
new_name1 = ">" + "Chromosome_2_normal" + " (" + bed_chr1 + ")"
output_file_write.write(new_name1)
output_file_write.write("\n")
output_file_write.write(input_file_no_line_breaks)
output_file_write.write("\n")

#chr3
final_chr2_name = ">" + "Chromosome_3_hybrid" + " (" + bed_chr2 + ":0-" + str(bed_chr2_begin_pos) + " + " + bed_chr1 + ":" + str(bed_chr1_begin_pos) + "-end" + ")"
output_file_write.write(final_chr2_name)
output_file_write.write("\n")
output_file_write.write(final_chr2)
output_file_write.write("\n")

#chr4
new_name2 = ">" + "Chromosome_4_normal" + " (" + bed_chr1 + ")"
output_file_write.write(new_name2)
output_file_write.write("\n")
output_file_write.write(input_file2_no_line_breaks)
