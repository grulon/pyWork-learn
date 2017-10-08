# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 16:53:04 2017
Weather App from the 
@author: glrulon
"""
import requests
import bs4
import collections

WeatherReport = collections.namedtuple('WeatherReport','cond,temp,scale,loc')

def main():
    # print the header
    print_header()
    
    # get zipcode from user
    code = input('What zipcode do you want the weather for? ')
    
    # get html from web  use request
    html = get_html_from_web(code)
    
    # parse the html
    report = get_weather_from_html(html)
    
    # display the forcast
    print('The weather in {} is {} and {}{}'.format(
          report.loc,report.cond,report.temp,report.scale))
    
    
def print_header():
    print('--------------------')    
    print('    WEATHER APP')   
    print('--------------------')   
    print()   
    

def get_html_from_web(zipcode):
    url = 'https://www.wunderground.com/weather-forecast/{}'.format(zipcode)
    response = requests.get(url)
    #print(response.status_code)
    #print(response.text[0:250])
    return response.text
    
    
    
    
def get_weather_from_html(html):
    #cityCss = '.region-content-header h1'
    #weatherScaleCss = '.wu-unit-temperature .wu-label'
    #weatherTempCss = '.wu-unit-temperature .wu-value'
    #weatherConditionCss = '.condition-icon'
    
    soup = bs4.BeautifulSoup(html, 'html.parser')
    loc = soup.find(class_='region-content-header').find('h1').get_text()
    condition = soup.find(class_='condition-icon').get_text()
    temp = soup.find(class_='wu-unit-temperature').find(class_='wu-value').get_text()
    scale = soup.find(class_='wu-unit-temperature').find(class_='wu-label').get_text()

    loc = find_pieces_of_location(cleanup_text(loc))
    condition = cleanup_text(condition)
    temp = cleanup_text(temp)
    scale = cleanup_text(scale)
    
    #print(condition, temp, scale, loc)
    #return condition, temp, scale, loc
    report = WeatherReport(cond=condition, temp=temp, scale=scale, loc=loc)
    return report
    
def find_pieces_of_location(loc : str):
    pieces = loc.split(',')
    return pieces[0].strip()

def cleanup_text(text : str):
    if not text:
        return text
        
    text = text.strip()
    return text
    
     
if __name__ == '__main__':
    main()


