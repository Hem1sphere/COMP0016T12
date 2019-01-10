
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
.half 0xee00, 0x00ee, 0x0101

# Memory address to put the sum into.  The result should be stored as a unsigned halfword.
# In this case the assembly language should put  0x00F0 onto this memory location.
# However the code should work in general for any given lists of data values.
.space 2


########## WRITE ASSEMBLY LANGUAGE SOLUTION BELOW ##########

.text
.globl main
main: 
#$a0 for vals
la  $a0, vals
lhu $t0, 0($a0)
addi $t1,$0,0
for: beq $t0,$t1,done
addi $a0,$a0,2
lhu $t2,0($a0)
addu $t3, $t2, $t3
addi $t1,$t1,1
j   for
done:
addi $a0, $a0, 2   
sh $t3, 0($a0)      
lhu $9, 0($a0)
li $v0 10      
syscall
