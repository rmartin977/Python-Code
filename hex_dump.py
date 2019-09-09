# hex_dump.py
# @ Robert Martin
# August 28, 2019

# This program returns a standard hex_dump output for a given file

# Usage:   At the terminal type: "python hex_dump.py filename".

# import standard libraries

import os
import sys
# sys.tracebacklimit = 0
os.system('clear')

assert(len(sys.argv)>1),'Sorry you need to provide a filename'

# Read raw binary data from file into a python byte array called s_bytes

try:
    fhand = open(sys.argv[1],'rb')
except:
    print('File {} cannot be opened:'.format( sys.argv[1]))
    sys.exit(0)


#fhand = open('../Test.docx','rb')
s_bytes = fhand.read()
fhand.close()



# convert the byte array to hex values
data = s_bytes.hex()

# pad the last row of data to make it 16 bytes
data = data + (32 - len(data)%32)//2 * '2e' + ' '

# put a space character between each byte
data_split = ' '.join(data[i:i+2] for i in range(0,len(data),2))

# the list comprehension below will divide the data into a list of 16 byte sublist
# where each sublist corresponds to a row for the hex_dump

final = [data_split[i:i+48]for i in range(0,len(data_split),48)]

# generate list of decimal codes for printable characters
printable = list(range(32,128))


def hex2string(x):

    """ This function inputs a string of hex character codes
        and returns a string. """

    # Convert string of hex values into a list of equivalent decimal values

    d_values =[int(x.split()[k],16) for k in range(len(x.split()))]

    # replace codes for nonprintable characters with '.' code is 46

    for j,k in enumerate(d_values):
        if int(k) not in printable:
            d_values[j]= 46

    # convert list of decimal values to string of characters and return the string

    s = ''.join(map(chr,d_values))

    return s

# Now print out the hex_dump table to the screen

print('\n\n')
for k in range(len(final)):
    print('{:04X}'.format(16*k),end='')
    print('\t' +final[k][:24]+' '+final[k][24:],end=' ')
    print(hex2string(final[k]))
