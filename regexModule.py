import re

'''
.   Any character Except New Line
/d  - Digit (0-9)
/D  - Not a digit (0-9)
/w  - Word Character (a-z,A-Z,0-9,_)
/W  - Not a Word Character
/s  - Whitespaces (space, tab, newline)
/S  - Not Whitespaces (space, tab, newline)
/b  - Word Boundary
/B  - Not a Word Boundary
^   - Beginning of a String
$   - End of a String
[]  - Matches Characters in Brackets
[^ ]    - Matches Character not in Brackets
|   - Either Or
( ) - Group

Quantifiers:
*   -  0 or More
+   - 1 or More
?   - O or One
{3} - Exact Number
{3,4}   - Range of Numbers (Minimum,Maximum)
'''


text_to_search = '''
abcdefghijklmnoprestuvwxyz
ABCDEFGHIJKLMNOLPQRSTUVWXYZ
123456789

Ha Haha

MetaCharacters (Need to be escaped)
. ^ $ * + ? { } [ ] \ | ( )

su.com

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

Mr. Ranold
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

cat
mat
pat
bat
'''

sentence = 'Start a sentence and then bring it to an end.'


# Matching su.com
pattern1 = re.compile(r'su\.com')
matches1 = pattern1.finditer(text_to_search)
for match in matches1:
    print(match)


# Matching Phone Number
pattern2 = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
matches2 = pattern2.finditer(text_to_search)
for match in matches2:
    print(match)


# Matching Phone Number that have separator (-,.)
pattern3 = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d')
matches3 = pattern3.finditer(text_to_search)
for match in matches3:
    print(match)


# Matching Phone Number that have started with 8 or 9
pattern4 = re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d')
matches4 = pattern4.finditer(text_to_search)
for match in matches4:
    print(match)


# Matching Phone Number in data.txt 
with open("data.txt","r",encoding='utf-8') as f:
    contents1 = f.read()
    pattern5 = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d')
    matches5 = pattern5.finditer(contents1)

    for match in matches5:
        print(match)


# Matching Phone Number in data.txt that started with 8 or 9
with open("data.txt","r",encoding='utf-8') as f:
    contents2 = f.read()
    pattern6 = re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d')
    matches6 = pattern6.finditer(contents2)
    for match in matches6:
        print(match)


# Matching Number in range 1-5 data.txt
with open("data.txt","r",encoding='utf-8') as f:
    contents3 = f.read()
    pattern7 = re.compile(r'[1-5]')
    matches7 = pattern7.finditer(contents3)
    for match in matches7:
        print(match)


# Matching text in range a-z data.txt
with open("data.txt","r",encoding='utf-8') as f:
    contents4 = f.read()
    pattern8 = re.compile(r'[a-z]')
    matches8 = pattern8.finditer(contents4)
    for match in matches8:
        print(match)


# Matching text in range a-z and A-Z data.txt
with open("data.txt","r",encoding='utf-8') as f:
    contents5 = f.read()
    pattern9 = re.compile(r'[a-zA-Z]')
    matches9 = pattern9.finditer(contents5)
    for match in matches9:
        print(match)


# Matching text not in range a-z and A-Z data.txt
with open("data.txt","r",encoding='utf-8') as f:
    contents6 = f.read()
    pattern10 = re.compile(r'[^a-zA-Z]')
    matches10 = pattern10.finditer(contents6)
    for match in matches10:
        print(match)


# Matching text not start with b but end with at
pattern11 = re.compile(r'[^b]at')
matches11 = pattern11.finditer(text_to_search)
for match in matches11:
    print(match)


# Matching Phone Number in data.txt
with open("data.txt","r",encoding='utf-8') as f:
    contents7 = f.read()
    pattern12 = re.compile(r'\d{3}.\d{3}.\d{4}')
    matches12 = pattern12.finditer(contents7)
    for match in matches12:
        print(match)


# Matching text that started with Mr/Mr.
pattern13 = re.compile(r'Mr\.?\s[A-Z]\w*')
matches13 = pattern13.finditer(text_to_search)
for match in matches13:
    print(match)


# Matching text that started with Mr/Mr/Ms/Mrs
pattern14 = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*')
matches14 = pattern14.finditer(text_to_search)
matches15 = pattern14.findall(text_to_search)
for match in matches14:
    print(match)
for match in matches15:
    print(match)


# Matching string start with start
pattern15 = re.compile(r'Start')
matches16 = pattern15.match(sentence)     
print(matches16)


# Search in a string
pattern16 = re.compile(r'sentence')
matches17 = pattern16.search(sentence)     
print(matches17)


# Search in a string and ignore the case
pattern17 = re.compile(r'Start',re.IGNORECASE)              # re.compile(r'Start',re.I)
matches18 = pattern17.search(sentence)      
print(matches18)


emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''


# Matches email
pattern18 = re.compile(r'[a-zA-Z0-9.-]+@[a-zA-Z-]+\.(com|edu|net)')
matches19 = pattern18.finditer(emails)
for match in matches19:
    print(match)


urls = '''
https://www.google.com
http:// bansal.com
https://youtube.com
https://www.nasa.gov
'''

# Matches url
pattern19 = re.compile(r'https?://(www\.)?\w+\.\w+')
matches20 = pattern19.finditer(urls)
for match in matches20:
    print(match)


# Making a group in url
pattern20 = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
matches21 = pattern20.finditer(urls)
for match in matches21:
    print(match.group(3))


# Substitute in a group
pattern21 = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
subbed_urls = pattern21.sub(r'\2\3',urls)
print(subbed_urls)