# -*- coding: utf8 -*-
# ॐ  LA-list (El Aye, List) [List Against LIst X-Stractor Reveal Leftovers COOL 2 Lists Make 3]
import argparse # important import :)
parser = argparse.ArgumentParser(description='\"LA-list\" El-Aye-List by Shaun R. Best KG4NWV CopyFree 2025\nExample [python lalist -n text.file.1 textfile2.txt]\nFor comparing 2 lists of single words (can be used to compare packages such as pacman packages.)  A word is defined as any combination of characters separated by white space (space and tab) or a new line.  LA-list will remove any duplicates from the two input lists and also condense double, tripple or more spacing to just one character either a newline or space character.\nThe OUTPUT of the program will be 3 files.\ncommon_match (A new list of words which appear in both lists.)\nleftover1 (Words from 1st list which didn\'t match the second list.)\nleftover2 (Words from 2nd list which didn\'t match the first list.)  This can help you keep track of let\'s say chosen packages from a Group can be checked against All Group packages to see which ones you haven\'t copied and pasted from ones that you have put on a list.  Running LA-list will always overwrite the output files if they exist so running twice with different lists in the same directory will erease previous output.')
parser.add_argument("arg_list1", type=str, help="1st List [input file1]")
parser.add_argument("arg_list2", type=str, help="2nd List [input file2]")
parser.add_argument("-n", action="store_true", help="[-n] Use 'Newline' instead of 'Space' Word Separator.  Only affects OUTPUT files because LA-list will accept input files with words separated by either newline(s) or space(s) and tab(s)")
args = parser.parse_args()
''' Load 1st List to Compare '''
with open(args.arg_list1, "br") as file1:
    file1_bytes = file1.read()
wword1 = []
list1 = []
for c in file1_bytes:
    if c > 8 and c < 12 or c > 31 and c < 127:
        if c != 9 and c != 10 and c != 11 and c != 32:
            wword1.append(str(chr(c)))
        if c == 9 or c == 10 or c == 11 or c == 32:
            fwword1 = "".join(wword1)
            if fwword1:
                list1.append(fwword1)
            wword1 = []
''' Remove Duplicates from 1st List '''
list11 = []
for v in list1:
    if v not in list11:
        list11.append(v)
''' Load 2nd List to Compare '''
with open(args.arg_list2, "br") as file2:
    file2_bytes = file2.read()
wword2 = []
list2 = []
for e in file2_bytes:
    if e > 8 and e < 12 or e > 31 and e < 127:
        if e != 9 and e != 10 and e != 11 and e != 32:
            wword2.append(str(chr(e)))
        if e == 9 or e == 10 or e == 11 or e == 32:
            fwword2 = "".join(wword2)
            if fwword2:
                list2.append(fwword2)
            wword2 = []
''' Remove Duplicates from 2nd List '''
list22 = []
for x in list2:
    if x not in list22:
        list22.append(x)
#Build Matched List with Inverse Lists (Output common_match, leftover1, leftover2 list files
common = []
for i, g in enumerate(list11):
    for l, k in enumerate(list22):
        if g == k:
            common.append(g)
            list11[i] = ""
            list22[l] = ""
leftover1 = []
leftover2 = []
for m in list22:
    if m:
        leftover2.append(m)
for n in list11:
    if n:
        leftover1.append(n)
#add newline to ends of records
leftover2[-1] = leftover2[-1] + "\n"
leftover1[-1] = leftover1[-1] + "\n"
common[-1] = common[-1] + "\n"
if args.n == False:
    foleftover1 = " ".join(leftover1).encode()
    focommon = " ".join(common).encode()
    foleftover2 = " ".join(leftover2).encode()
if args.n == True:
    foleftover1 = "\n".join(leftover1).encode()
    focommon = "\n".join(common).encode()
    foleftover2 = "\n".join(leftover2).encode()

''' write files to disc '''
try:
    with open("common_match", "wb") as fmatch:
        fmatch.write(focommon)
        s = len(focommon)
    print(f"common_match written successfully.  {s} bytes")
except IOError as p:
    print(f"Error writing to file: {p}")
try:
    with open("leftover1", "wb") as fl1:
        fl1.write(foleftover1)
        t = len(foleftover1)
    print(f"leftover1 written successfully.  {t} bytes")
except IOError as q:
    print(f"Error writing to file: {q}")
try:
    with open("leftover2", "wb") as fl2:
        fl2.write(foleftover2)
        u = len(foleftover2)
    print(f"leftover2 written successfully.  {u} bytes")
except IOError as r:
    print(f"Error writing to file: {r}")
