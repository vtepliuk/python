#!/usr/bin/env python3

"""
62e04dacb9496ffc2a18f79f48475fb5
python
lab6
v4
vite24
2024-10-31 11:08:56
v4.0.0 (2019-03-05)

Generated 2024-10-31 12:08:57 by dbwebb lab-utility v4.0.0 (2019-03-05).
https://github.com/dbwebb-se/lab
"""

from dbwebb import Dbwebb

# pylint: disable=invalid-name

dbwebb = Dbwebb()
dbwebb.ready_to_begin()



# ==========================================================================
# Lab 6 - python
#
# During these exercises we train on reading, writing and appending data to
# text file's.
#



# --------------------------------------------------------------------------
# Section 1. Files
#
#
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.1 (1 points)
#
# Read the `quotes.txt` -file in UTF-8 encoding and store the content into a
# variable. Answer with the number of characters in the file.
#
# Write your code below and put the answer into the variable ANSWER.
#
file_name = "quotes.txt"

def readfile():
    with open(file_name) as filehandle:
        content_of_file = filehandle.read()
    return content_of_file

content = readfile()

ANSWER = len(content)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.2 (1 points)
#
# Use your variable from the exercise above and answer with the contents on
# line number 2. You should not have a newline at the end of the line.
#
# Write your code below and put the answer into the variable ANSWER.
#

def readfile():
    with open(file_name) as filehandle:
        content_of_file = filehandle.read()
    return content_of_file

content = readfile()
lines = content.split('\n')





ANSWER = lines[1]

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.3 (1 points)
#
# First, read the content inside of quotes.txt and remove the 5 last rows.
# Then replace line number 6 with the new string "I am replaced".
# Then, create a new file called `newQuotes.txt` where you save the new
# changes. Replace `newQuotes.txt` if it already exists.
#
# Answer with the new content inside `newQuotes.txt`. Don't have a "\n" on
# the last line.
#
# Write your code below and put the answer into the variable ANSWER.
#
new_file_name = "newQuotes.txt"

def readfile():
    with open(file_name) as filehandle:
        content_of_file = filehandle.read()
    return content_of_file

content = readfile()
lines = content.split('\n')
lines = lines[:-5]
lines[5] = "I am replaced"
new_content = '\n'.join(lines)
with open(new_file_name, 'w') as filehandle:
    filehandle.write(new_content)
ANSWER = new_content

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.4 (1 points)
#
# Append the following sentence on a new line at the end of newQuotes.txt and
# answer with the content.
#
# *"All creativity is an extended form of a joke."*
#
# Write your code below and put the answer into the variable ANSWER.
#
new_file_name = "newQuotes.txt"
with open(new_file_name, 'r') as filehandle:
    content = filehandle.read()

new_sentence = "All creativity is an extended form of a joke."
updated_file = content + '\n' + new_sentence

with open(new_file_name, 'w') as filehandle:
    filehandle.write(updated_file)






ANSWER = updated_file

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.4", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.5 (1 points)
#
# Store the number of empty lines that `passwords.txt` has and create a new
# file called `newPasswords.txt` containing the lines that are not empty.
#
# Answer with the following:
#
# *passwords.txt has X empty lines and contains: Y*
#
# Replace `X` with the number of empty lines and `Y` with the new files
# content.
#
# Write your code below and put the answer into the variable ANSWER.
#
with open('passwords.txt', 'r') as filehandle:
    lines = filehandle.readlines()
empty_lines_count = 0
not_empty_lines = []

for line in lines:
    if line.strip() == "":
        empty_lines_count += 1
    else:
        not_empty_lines.append(line.strip())
with open('newPasswords.txt', 'w') as filehandle:
    new_file_content = '\n'.join(not_empty_lines)
result = f"passwords.txt has {empty_lines_count} empty lines and contains: {new_file_content}"






ANSWER = result

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.5", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.6 (3 points)
#
# Write the content of line numbers 2, 3 and 4 from `quotes.txt` to a new
# file that you create called `extraQuotes.txt`. Replace `extraQuotes.txt` if
# it already exists.
# Save the total number of characters and the 9 first characters of the
# second line into variables.
#
# Answer with the following string:
# "The file has X characters and the 9 first of the second row are: Y"
#
# **Example**:
# *"The file has 220 characters and the 9 first of the second row are: - Jon
# Doe"*
#
# Do not include newlines when you count the number of characters.
#
# Write your code below and put the answer into the variable ANSWER.
#






ANSWER = "Replace this text with the variable holding the answer."

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.6", ANSWER, False)


dbwebb.exit_with_summary()
