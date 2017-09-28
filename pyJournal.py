""" 
Personal Journal App
"""
import pyJournal_datawork  #prefer this method because it is obvious where comes from... retain namespace
#from pyJournal_datawork import load, save  # can also do import * which brings in all functions of import (can be confusing)

def main():
    print_header()
    run_event_loop()
    
    
def print_header():
    print('--------------------------------------')
    print('           JOURNAL APP')
    print('--------------------------------------')


def run_event_loop():
    print('What do you want to do with your journal?')
    cmd = 'EMPTY'
    journal_name = 'default'
    journal_data = pyJournal_datawork.load(journal_name)     # pyJournal_datawork.load()  #[]  # list()
    
    while cmd != 'x' and cmd:
        cmd = input('[L]ist entries, [A]dd an entry, E[x]it: ')
        cmd = cmd.lower().strip()
        
        if cmd == 'l':
            list_entries(journal_data)
        elif cmd == 'a':
            add_entry(journal_data)
        elif cmd != 'x' and cmd:
            print("Sorry, we don't understand '{}'.".format(cmd))
        
    print('Done, goodbye.')
    pyJournal_datawork.save(journal_name, journal_data)

def list_entries(data):
    print('Your journal entries: ')
    entries = reversed(data)
    for idx, entry in enumerate(entries):
        print(' * [{}] {}'.format(idx+1,entry))

    
def add_entry(data):
    text = input('Type your entry, <enter> to exit: ')
    pyJournal_datawork.add_entry(text, data)
    # data.append(text)

        
#  main()  not a proper way to run it... because it means this file cannot be a library. can't import it.
print('__file__: ' + __file__)
print('__name__: ' + __name__)

if __name__ == '__main__':
    main()









