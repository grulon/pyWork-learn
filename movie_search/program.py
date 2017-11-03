# -*- coding: utf-8 -*-
"""
Movie search... Error Handling

Created on Fri Nov  3 13:49:21 2017

@author: glrulon
"""
import movie_svc
import requests.exceptions

def main():
    print_header()
    search_event_loop()
    
    
def print_header():
    print('-----------------------------------------')    
    print('      MOVIE SEARCH APP')    
    print('-----------------------------------------')
 


def search_event_loop():
    search = 'ONCE_THROUGH_LOOP'
    
    while search != 'x':
        try:
            search = input('Movie search text (x to exit): ')
            if search != 'x':
                results = movie_svc.find_movies(search)
                print("Found {} results.".format(len(results)))
                for r in results:
                    print('{} -- {}'.format(
                          r.year, r.title))
                print()
        except ValueError:
            print("Error: Search text is required.")
        except requests.exceptions.ConnectionError:
            print("Error: Your network is down.")
        except Exception as x:
            print("Unexpected error. Please share these details with Support: {}".format(x))
            
    print('exiting...')


if __name__ == '__main__':
    main()
