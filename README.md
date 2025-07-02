LA-list El-Aye-List by Shaun R. Best KG4NWV CopyFree 2025
Example [python lalist -n text.file.1 textfile2.txt]
This is as much a generator as it is a comparator :)
For comparing 2 lists of single words (can be used to compare lists of packages such as pacman packages.)
Scenario, You are an Arch Linux user and you ran command % sudo pacman -Sg plasma > plasmagrp.
you then put that file in VIM and run a macro to delete the leading 'plasma ' on every line..
At this point you have a list of all plasma group packages and you want to use that list to create a new list of only
the plasma packages you want to install and you spent some hours doing this right.  well now you have your list could
be named 'selection' and the list from earlier 'plasmagrp'.
You could run the command % 'python lalist.py selection plasmagrp' and see output file 'leftover2' the file generated
by lalist to get a list only of the packages you haven't enlisted as your selection from 'plasmagrp'.  You did this
because you want to keep reading about every package in the plasma group and have a tool to automatically shorten
your 'todo' list with your 'done' list or etc.  I think Arch Linux users could find this a very helpful tool which
saves them lots of otherwise batch file scripting awk and sed commands usage.

A word is defined as any combination of characters separated by white space (space and tab) or a new line.
LA-list will remove any duplicates from the two input lists and also condense double, tripple or more spacing to just
one character either a newline or space character.  The OUTPUT of the program will be 3 files. 1) common_match
(list of words which appear in both lists.)  2) leftover1 (Words from 1st list which didn't match the second list.)
3) leftover2 (Words from 2nd list which didn't match the first list.)  This can help you keep track of let's say
chosen packages from a Group can be checked against All Group packages to see which ones you haven't copied and
pasted from ones that you have put on a list.  Running LA-list will always overwrite the output files if they exist
so running twice with different lists in the same directory will erease previous output.
