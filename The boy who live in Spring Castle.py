import requests
from bs4 import BeautifulSoup

import urllib.request
from urllib.parse import urlparse

count = 0

menu = int(input("Enter the Download Menu (1: ico, 2:icos, 3:png):    "))

for i in range(1, 5):
    URL = "http://www.iconarchive.com/show/super-mono-3d-icons-by-double-j-design." + str(i) + ".html"
    
    print(URL)
    print("Page Analyzing", i, "step to 4 steps")
    
    print("===================================================================")
    client = requests.session()
    view = urllib.request.urlopen(URL)

    source = view.read().decode('utf-8')
    SoupSource = BeautifulSoup(source, 'html.parser')

    #print(SoupSource)
    #input()

    A1 = SoupSource.select('contentbox')
    
    if menu == 1:
        imageList = SoupSource.select('div > div.detail > a:nth-child(1)')
        #print("1")
    elif menu == 2:
        imageList = SoupSource.select('div > div.detail > a:nth-child(2)')
        #print("2")
    else:
        imageList = SoupSource.select('div > div.detail > a.lastitem')
        #print("3")
        
    for ico in imageList:
        count += 1
        if menu == 1:
            iconAddress = "http://www.iconarchive.com/" + ico.get('href')
        else:
            iconAddress = ico.get('href')

        #print(iconAddress)
        #Image Path 자르기
        path = urlparse(iconAddress).path
        path = path.replace("/", "-")
        
        #print(path)
        
        icoList = list()
        position_number = 0
        startpoint = 0
        
        
        while position_number<10:
            path = path[startpoint:]
            
            try :
                intersection = path.index("-")
                
            except:
                break;

            icoList.append(path[ : intersection].rstrip("-"))
            startpoint = intersection+1
            position_number += 1
            
            #print(intersection, ": intersection")
            #icoList.append(position_number)
            #print(icoList[position_number])
            #print(startpoint, ":startpoint") 
            
            
            #savename = './image/' + 'imgs' + str(i) + '/' + '3Dcon-' + path
            savename = './pngs/' + 'pngs' + str(i) + '/' + '3Dcon-' + path
    
        urllib.request.urlretrieve(iconAddress, savename)
        print(savename, "으로 저장 완료")

    print("===================================================================")

        
