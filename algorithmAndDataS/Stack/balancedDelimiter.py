from linkliststack import Stack

test_string = """
         int sumList( int theList[], int size )
   {
         int sum = 0;
         int i = 0;
         while( i < size ) {
           sum += theList[ i ];
           i += 1;
         }
         return sum;
    }
"""


def delimiter_test( data ):
    delimiter = Stack()
    for string in data:
        if string == "(":
            delimiter.push(")")
            print(string)
        elif string == "[":
            delimiter.push("]")
            print(string)
        elif string =="{":
            delimiter.push("}")
            print(string)
        else:
            pass
        
        if string == ")" or string == "]" or string =="}":
            cur = delimiter.pop()
            print cur
            assert cur == string, "Delimiters are not balanced"
        else:
            pass
    print "Balanced Delimiter"

def delimiter_book_code( srcfile ):
    s = Stack()
    for line in srcfile:
        for token in line:
            if token in "{[(":
                s.push( token )
            elif token in "}])":
                if s.isEmpty():
                    return False
                else:
                    left = s.pop()
                    if (token == "}" and left != "{") or \
                       (token == "]" and left != "[") or \
                       (token == ")" and left != "("):
                       return False 
    return s.isEmpty()

if __name__ == "__main__":
    delimiter_test(test_string)
    print delimiter_book_code(test_string)
