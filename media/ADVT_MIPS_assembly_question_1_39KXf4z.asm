
#
# ELECTRAN QUESTION 9.
#
# The first unsigned halfword gives the number of data values to add together.
# Then the data values follow this given as  unsigned 16-bit values.
# The final memory location allocated with a  'space  2' directive gives the
# memory location to put the result.
#
# No overflow exceptions should result (similar to C-code) when doing the
# addition - any  unsigned overflow should just be ignnored.

# Your key task is to write some MIPS assembly language to add together the
# data values given and put the answer into the  last memory location. 
# 
# You should write your assembly language below the comment line saying:
# "WRITE ASSEMBLY LANGUAGE SOLUTION BELOW".

.data

vals:

# Number of data values to add together as a unsigned halfword.
.half 3

# The actual data values themselves as "16-bit unsigned values".
.half 0xffff, 0xffff, 0xffff

# Memory address to put the sum into.  The result should be stored as a unsigned halfword.
# In this case the assembly language should put  0x00F0 onto this memory location.
# However the code should work in general for any given lists of data values.
.space 2


########## WRITE ASSEMBLY LANGUAGE SOLUTION BELOW ##########

.text
.globl main

main:
# $1 is for counter, $2 for result

la $9, vals
lhu $s1, 0($9)
add $s2, $0, $0

#check if all elements of the array has been added
addi $9, $9, 2
while: beq $s1, $0, done1
lhu $8, 0($9)
addu $s2, $8, $s2
addi $9, $9, 2
subu $s1, $s1, 1
j while

done1:
sh $s2, 0($9)
lhu $10, 0($9)
li $v0, 10
syscall
