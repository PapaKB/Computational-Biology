# Tutorial 2 Questions
1. Write a program to implement Needleman-Wunsch for proteins
    * You will need the blosum50 scoring matrix
    * You can use any programming language
    * Run this on HEAGAWGHEE versus PAWHEAE
    * Compare this to page 23 in lecture 5
    * Match the protein sequence SALPQPTTPVSSFTSGSMLGRTDTALTNTYSAL with PSPTMEAVTSVEASTASHPHSTSSYFATTYYHLY

2. Modify your program to implement the Smith-Waterman algorithm
    * Again run this on HEAGAWGHEE versus PAWHEAE
    * Compare this to page 5 in lecture 6
    * Find the best local match between MQNSHSGVNQLGGVFVNGRPLPDSTRQKIVELAHSGARPCDISRILQVSNGCVSKILGRY and TDDECHSGVNQLGGVFVGGRPLPDSTRQKIVELAHSGARPCDISRI

3. We are going to test the BLAST algorithm
    * Download the Pax6 protein for the mouse by going to http://www.uniprot.org/uniprot/P63015 choose the "Format" tab and choose the FASTA (canonical) format
    * Do the sacme for the eyeless protein for the fruit fly http://www.uniprot.org/uniprot/O96791
    * Perform a BLAST sequence comparison using the web service at https://blast.ncbi.nlm.nih.gov

4. Program the following HMM to generate CG rich regions

5. Write a viterbi algorithm for finding the most likely CG regions and find a way of drawing this

6. Run this on the genome for the Lambda Phage: https://www.ncbi.nlm.nih.gov/nuccore/215104?report=fasta