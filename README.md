# hrp3

- find_aligned_reads.py file: Determines if any reads have begin sequence aligned to chr13 and end sequence aligned to chr11.

"python3 find_aligned_reads.py <sam file aligning raw reads to chr13> <sam file aligning raw reads to chr11>  <bed file with target mappings> <int corresponding to how much bases are needed to overlap with chr13 and chr11> <name of output file as txt>

- extract_aligned_hybrid.py: Extracts all the reads that map to the hybrid chromosomes

"python3 extract_aligned_hybrid.py <sam file aligning raw reads to hybrid chromosomes> <name of output file as txt>

- create_hybrid_chr.py: Creates new fused chromosomes using chromosome 11 and chromosome 13 in the middle of the 15kb-shared region

"python create_hybrid_chr.py <chr11.fasta> <chr13.fasta> <bed file with position of shared regions to fuse> <name of output fasta file>

- extract_unique_reads.py: Extracts the unique reads from a sam file since while a given read can map multiple times, we only want to see it once in our final txt file

"python extract_unique_reads.py <sam file aligning raw reads to genome including hybrid chromosomes> <name of output file as txt>

- extract_unique_fastas.py: Extracts the fastas corresponding to the unique reads

"python extract_unique_fastas.py <input fastq file> <output txt file of extract_unique_reads.py> <name of output file as fastq> 

- extract_spanning_chr11.py: Extracts the spanning reads for hybrid chr11-13, normal chr11, hybrid chr13-11, and normal chr13

"python extract_spanning_chr11.py <input sam file aligning raw reads to genome including hybrid chromosomes> <output txt file showing spanning reads mapping to hybrid chr11-13> <output txt file showing spanning reads mapping to normal chr11> <output txt file showing spanning reads mapping to hybrid chr13-11> <output txt file showing spanning reads mapping to hybrid chr13-11>
