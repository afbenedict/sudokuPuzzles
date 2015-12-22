import urllib2
from bs4 import BeautifulSoup

#get the html from the url
#parse the puzzle
#return it as an array

levels = {
        "easy" : 1,
        "medium" : 2,
        "hard" : 3,
        "evil" : 4 }


def GetPuzzle(level):
    p = [ 0 for i in range(81)]
    response = urllib2.urlopen('http://view.websudoku.com/?level=' + str(level))
    content = response.read()
    
    soup = BeautifulSoup(content)
    table = soup.find("table", id="puzzle_grid")
    input = table.find_all("input")
    
    for i in range( len(input)):
        val = input[i].get("value")
        if(val is not None):
            p[i] = int(val)
    
    return p




