import scrapy
import logging
import re
import pdb
from Scraper.items import Film
from Scraper.items import Actor
from bs4 import BeautifulSoup, SoupStrainer

class QuotesSpider(scrapy.Spider):
    name = 'quotes'

    def start_requests(self):
        urls = ['https://en.wikipedia.org/wiki/Love_Actually']
        for url in urls:
            yield scrapy.Request(url, self.parse)

    def parse(self, response):

        #parse the string text from a query
        def extractText(query):
            if query is None:
                return None
            return query.text.strip()

        soup = BeautifulSoup(response.body, 'lxml')
        content = soup.find('div',{'id':'mw-content-text'})
        prefix = 'https://en.wikipedia.org'
        nextLinks = []

        #check whether the givin link is a valid wikipedia link
        def isValidLink(link):
            if link.startswith('/wiki/'):
                return True
            return False

        ## find the born year of an actor/actress or of a film
        def findYear(string):
            res = re.compile(r"[1-9][0-9][0-9][0-9]").search(string)
            return res.group()

        ## parse the correct filmValue
        def parseFilmValue(string):
            if string is not None:
                string = string.replace(',', '')
                regex = re.compile(r"[1-9]+[0-9]*.[1-9]*").search(string)
                digits = regex.group()
                res = float(digits)
                if string.find("million") != -1:
                    res *= 1000000
                return str(res)
            else:
                return '0.0'

        # logging error when no content.
        if content is None:
            logging.error(response.url+": no content is found")

        #get main table to extract our information with less scrapping time
        table = content.find("table")

        #defing whether the given link is for an actor/actress or for a film
        isActor = False
        isFilm = False

        if table is not None:
            if table.find('th',{'scope':'row'}) is not None:
                isFilm = (extractText(table.find('th',{'scope':'row'})).find('Directed by')!=-1)
            if table.find('td', attrs={'class': 'role'}) is not None:
                isActor = (extractText(table.find('td', attrs={'class': 'role'})).find('Actor')!=-1) or (extractText(table.find('td', attrs={'class': 'role'})).find('Actress')!=-1)

        #when the scrapping link is a link for actor/actress
        if isActor:
            item = Actor()
            item['isActor'] = isActor
            item['isFilm'] = isFilm

            #get actor name
            actorName = table.find('span', attrs={'class': 'fn'})
            item['actorName'] = extractText(actorName)

            #get actor age
            year = table.find('span',{'class':'bday'})
            if year is None:
                item['year'] = '0'
            else:
                item['year'] = findYear(year.string)

            # get url and next valid link to scrap and actor casting information
            actorFilms = []
            casting = []
            temp = content.find('div',{'class':'div-col columns column-width'})
            if temp is None:
                temp = content.find('div', {'class': 'div-col columns column-count column-count-2'})
            if temp is None:
                temp = content.find_all('table',class_="wikitable")
                if len(temp) > 0:
                    temp = temp[0]
                if temp is None:
                    return
            if (not isinstance(temp,list)):
                films = temp.find_all("a", href=True)
                if films is None or len(films) <= 0:
                    return
                for film in films:
                    if isValidLink(film['href']):
                        actorFilms.append(prefix + film['href'])
                        nextLinks.append(prefix + film['href'])
                        casting.append(extractText(film).split('\n'))

            item['url'] = response.url
            item['films'] = actorFilms
            item['castings'] = casting
            yield item

        #when we are scrapping a film link
        elif isFilm:
            item = Film()
            item['isActor'] = isActor
            item['isFilm'] = isFilm

            #get film name
            filmName = table.find('th', attrs={'class': 'summary'})
            item['filmName'] = extractText(filmName)

            #get film year
            year = table.find('span',{'class': 'bday dtstart published updated'})
            if year is None:
                item['year'] = '0'
            else:
                item['year'] = findYear(year.string)

            # extract film value, url link and name for starrings and store the next possible links to scrap
            filmValue = None
            actors = []
            temp = []
            for tr in table.find_all("tr"):
                tr = BeautifulSoup(str(tr), "lxml")
                row = tr.find("th", {"scope": "row"})
                if row is not None:
                    if extractText(row).find("Starring")!=-1:
                        for actor in tr.find_all("a", href=True):
                            if isValidLink(actor['href']):
                                temp.append(extractText(actor))
                                actors.append(prefix+actor['href'])
                                nextLinks.append(prefix+actor['href'])
                    elif extractText(row).find('Box office')!=-1:
                        filmValue = extractText(tr.find("td")).split('\xa0')[0]

            item['url'] = response.url
            item['actors'] = actors
            item['filmValue'] = parseFilmValue(filmValue)
            item['starrings'] = temp
            yield item

        ##
        ## recursively scrapping links down here!
        ##
        nextLinks = list(set(nextLinks))
        for link in nextLinks:
            yield scrapy.Request(link, callback = self.parse)
