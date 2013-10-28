#!/usr/bin/env python

"""
^From : any string that starts with From
/bin/tcsh$ : any string that ends with /bin/tcsh
^Subject: hi$ : any string consisting solely of the string Subject: hi
the : any string containing the
\bthe: any word that starts with the
\bthe\b : matches only the word the
\Bthe : any string that contain but does not begin with the
b[aeiu]t : bat,bet,bit,but
[cr][23][dp]: a string of 3 characters: first is'c' or'r'

z.[0-9] : 'z' followed by any character then followed by a single digit
[r-u][env-y][us] : 'r''s''t''u' followed by 'e''n''v''w''x''y' followed by 'u''s'
[^aeiou] : a non-vowel character 
[^\t\n] : Not a TAB or \n
["-a] : In an ASCII system, all characters that fall between '"' and"a", that is, between originals 34 and 97

[dn]ot? :'d''n', followed by an 'o' and, at most, one 't' after that; thus, do,no,dot,not
0?[1-9] : any numeric digit, possibly perpend with a '0'. for example, the set of numeric representations of the months January to September
[0-9]{15,16} : fifteen or sixteen digits(for example, credit card numbers) 
</?[^>]+> : string that matches all valid(and invalid) HTML tags
[KQRBNP][a-h][1-8][a-h][1-8] 

\w+-\d+ : alphanumeric string and numbers separated by a hyphen
[A-Za-z]\w* : alphabetic first character; additional characters(if present) can be alphanumeric 
\d{3}-\d{3}-\d{4} : American-format telephone numbers with an area code prefix, as in 800-555-1212
\w+@\w+\.com : simple e-mail addresses of the form XXX@YYY.com

\d+(\.\d*)? : strings representing simple floating-point numbers; that is, any number of digits followed optionally by a single decimal point 
				and zero or more numeric digits, as '0.004' '2' '75.'
(Mr?s?\.)?[A-Z][a-z]*[A-Za-z-]+ :firstname and lastname , with a restricted first name(must start with uppercase; lowercase only for remaining letters,
								 if any), the full name, perpended by an optionally title of 'Mr.''Mrs.'Ms.''M.' and a flexible last name, allowing for
								 multiple words, dash, and uppercase letters

(P?<name>) 
"""
