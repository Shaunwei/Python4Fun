#!/usr/bin/python
import sys
import csv

TENOR_LIST = ['006M', '012M', '024M', '036M', '048M', '060M', '072M', '084M', '120M', '240M', '360M']    

def next_tenor():
    i = 0
    while True:
        ind = i % len(TENOR_LIST)
        yield TENOR_LIST[ind]
        i += 1

def clean_csv(file_name, new_file_name):
    """Using csv.Dialect to make up all rows
    check each row if it has tenor Tenor_List in order just copy it
    if not copy the data from previous row w/o Spread
    """
    with open(file_name, 'rU') as rcsvfile, open(new_file_name, 'w') as wcsvfile:
        reader = csv.DictReader(rcsvfile)
        writer = csv.DictWriter(wcsvfile, reader.fieldnames, lineterminator='\n')
        writer.writeheader()
        
        previous_row = {}
        current_row = reader.next()
        flag = True
        tenor_gen = next_tenor()

        row = None
        tenor_item = None
        while(flag):
            tenor_item = tenor_gen.next()
            row = current_row
            if tenor_item == current_row['Tenor']:
                try:
                    previous_row, current_row = current_row, reader.next()
                except StopIteration:
                    row = previous_row
                    row['Tenor'] = tenor_item
                    flag = False
            else:
                row = previous_row
                row['Tenor'] = tenor_item

            writer.writerow(row)

        tenor_last_item = TENOR_LIST[-1]
        while(tenor_item != tenor_last_item):
            row = previous_row
            row['Tenor'] = tenor_item
            writer.writerow(row)
            tenor_item = tenor_gen.next()
        else:
            row['Tenor'] = tenor_item
            writer.writerow(row)
        

if __name__=='__main__':
    length = len(sys.argv)
    if length == 1:
        clean_csv('exp.csv', 'tmp.csv')
    elif length == 2:
        clean_csv('exp.csv', sys.argv[1])
    elif length == 3:
        clean_csv(sys.argv[1], sys.argv[2])
