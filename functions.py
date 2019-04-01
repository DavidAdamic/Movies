import requests
import re
import ast

api_key = '8429793f'

def get_link(title):
    """function will get the right url to get movie data from"""
    title_ = title.replace(' ','+')
    url = 'http://www.omdbapi.com' + '/?t=' + title_ + '&apikey=' + api_key
    return url

def get_list(string):
    """get a list of elements out of a string"""
    list = string.split(',')
    tab = []
    for el in list:
        if el[0] == ' ':
            tab.append(el[1:]) # leave out the first whitespace
        else:
            tab.append(el)
    return tab

def get_data(title):
    """function will gather movie data from site OMDb API using
    given title and your own api key"""
    text = requests.get(get_link(title)).text #omdbapi page return movie data in text form
    page = ast.literal_eval(text) # convert text into dictionary form
    data = []
    data.append(page['Title']) # title
    data.append(page['Released']) # release date
    data.append(page['Runtime']) # movie length
    genres = page['Genre']
    data.append(get_list(genres)) # sublist of movie genres
    directors = page['Director']
    data.append(get_list(directors)) #sublist of movie's directors
    writers = page['Writer']
    data.append(get_list(writers))  #sublist of movie's writers (screenplay and story)
    actors = page['Actors']
    data.append(get_list(actors)) # sublist of movie's main actors and acrtesses
    data.append(page['Production'])
    data.append(page['Plot'])
    return data

def present_data(table):
    """function optionally presents movie data"""
    print('{0:>12} | {1}'.format('Title', table[0]))
    print('{0:>12} | {1}'.format('Release Date', table[1]))
    print('{0:>12} | {1}'.format('Runtime', table[2]))
    line1 = ''
    for i in table[3]:
        line1 += i + ', '
    print('{0:>12} | {1}'.format('Genre', line1[:-2]))
    line2 = ''
    for i in table[4]:
        line2 += i + ', '
    print('{0:>12} | {1}'.format('Producer', line2[:-2]))
    line3 = ''
    for i in table[5]:
        line3 += i + ', '
    print('{0:>12} | {1}'.format('Writer', line3[:-2]))
    line4 = ''
    for i in table[6]:
        line4 += i + ', '
    print('{0:>12} | {1}'.format('Cast', line4[:-2]))
    print('{0:>12} | {1}'.format('Production', table[7]))
    print('{0:>12} | {1}'.format('Plot', table[8]))

def combine_genres(list1, list2, list3):
    """combines three lists of movie genres, counts them and puts them in a dictionary form"""
    genres = {}
    for el1 in list1:
        genres[el1] = 1
    for el2 in list2:
        if el2 in genres.keys():
            genres[el2] += 1
        else:
            genres[el2] = 1
    for el3 in list3:
        if el3 in genres.keys():
            genres[el3] += 1
        else:
            genres[el3] = 1
    return genres

def combine_data(foo, bar, baz):
    """function combines 3 lists of movie datas"""
    combined = []

    titles = []
    titles.append(foo[0])
    titles.append(bar[0])
    titles.append(baz[0])
    combined.append(titles)

    # release date doesn't matter in movie data comparing

    runtime_avg = (int(foo[2].split(' ')[0]) + int(bar[2].split(' ')[0]) + int(baz[2].split(' ')[0]))//3
    combined.append(runtime_avg)

    genres1 = foo[3]
    genres2 = bar[3]
    genres3 = baz[3]
    genres = combine_genres(genres1, genres2, genres3)
    combined.append(genres)

    producers = set()
    producers.update(foo[4])
    producers.update(bar[4])
    producers.update(baz[4])
    combined.append(producers)

    writers = set()
    for wr in foo[5]:
        if wr == 'N/A':
            break
        list = wr.split(' ')
        writer = list[0] + ' ' + list[1]
        writers.add(writer)
    for wr in bar[5]:
        if wr == 'N/A':
            break
        list = wr.split(' ')
        writer = list[0] + ' ' + list[1]
        writers.add(writer)
    for wr in baz[5]:
        if wr == 'N/A':
            break
        list = wr.split(' ')
        writer = list[0] + ' ' + list[1]
        writers.add(writer)
    combined.append(writers)

    actors = set()
    for ac1 in foo[6]:
        if ac1 == 'N/A':
            break
        actors.add(ac1)
    for ac2 in bar[6]:
        if ac2 == 'N/A':
            break
        actors.add(ac2)
    for ac3 in baz[6]:
        if ac3 == 'N/A':
            break
        actors.add(ac3)
    combined.append(actors)

    productions = set()
    if foo[7] != 'N/A':
        productions.add(foo[7])
    if bar[7] != 'N/A':
        productions.add(bar[7])
    if baz[7] != 'N/A':
        productions.add(baz[7])
    combined.append(productions)

    # plots don't matter in movie data comparing

    return combined

def get_titles(url):
    """gets all the movie titles from given IMDb movie list"""
    page = requests.get(url).text
    table = re.split("https://www.rottentomatoes.com/m/", page)[3::3]
    list_underscore = []
    for el1 in table:
        stuff = el1.split('/')
        list_underscore.append(stuff[0])
    list = []
    for el2 in list_underscore:
        if el2[-4:] == '2018':
            el2 = el2[:-5]
        title = el2.replace('_', ' ')
        list.append(title)
    return list

def compare(data, combined):
    """compares the combined data of 3 given movies and current movie from 2018 list"""
    score = 0
    #compare runtimes
    if abs(int(data[2].split(' ')[0]) - combined[1]) < 15:
        score += 5
    #compare genres
    for gen in data[3]:
        if gen in combined[2].keys():
            score += combined[2][gen]**2
    #compare producers
    for prod in data[4]:
        if prod in combined[3]:
            score += 10
    #compare writers
    for wri in data[5]:
        if wri in combined[4]:
                score += 6
    #compare actors
    for act in data[6]:
        if act in combined[5]:
            score += 10
    for pro in data[7]:
        if pro in combined[6]:
            score += 5
    return score