__author__ = 'Hilla'

import urllib.request
import itertools
import networkx as nx
#import matplotlib
#matplotlib.use('PDF')
#import matplotlib.pyplot as plt
import csv
import sys
import ast


#create a new Graph which is directed
DG=nx.Graph()
URLlist = ["http://www.instructables.com/id/Knitted-Moustache/?ALLSTEPS","http://www.instructables.com/id/Embroidery-101/?ALLSTEPS","http://www.instructables.com/id/Electronic-Embroidery/?ALLSTEPS","http://www.instructables.com/id/Crochet-super-cute-Octopus/?ALLSTEPS","http://www.instructables.com/id/Make-a-quick-box-using-box-joints/?ALLSTEPS","http://www.instructables.com/id/Simple-Storage-Box/?ALLSTEPS","http://www.instructables.com/id/String-Voodoo-Dolls/?ALLSTEPS","http://www.instructables.com/id/Wood-Whittling-101/?ALLSTEPS","http://www.instructables.com/id/Floppy-Disk-Lamp/?ALLSTEPS","http://www.instructables.com/id/Wood-Industrial-Lamp-Desk/?ALLSTEPS","http://www.instructables.com/id/Nail-String-Art-using-reclaimed-wood/?ALLSTEPS","http://www.instructables.com/id/Reclaimed-Wood-Skateboard/?ALLSTEPS","http://www.instructables.com/id/making-concrete-balls/?ALLSTEPS","http://www.instructables.com/id/Conspeakuous-Concrete-Speakers/?ALLSTEPS","http://www.instructables.com/id/DIY-Concrete-Lamp/?ALLSTEPS","http://www.instructables.com/id/Making-Wooden-Knobs-on-a-Drill-Press/?ALLSTEPS","http://www.instructables.com/id/Silk-Thread-Valentines-Card/?ALLSTEPS","http://www.instructables.com/id/Custom-Made-Wax-Candles-Cast-using-Sugru-Moulds/?ALLSTEPS","http://www.instructables.com/id/Laser-Cut-Holiday-Ribbon-Garlands/?ALLSTEPS","http://www.instructables.com/id/How-To-Make-A-Wood-Jigsaw-Puzzle/?ALLSTEPS","http://www.instructables.com/id/LED-Hula-Hoop/?ALLSTEPS","http://www.instructables.com/id/Happy-Poop-Emoji-Made-from-Clay/?ALLSTEPS","http://www.instructables.com/id/Rainbow-Rain-Wax-Art/?ALLSTEPS","http://www.instructables.com/id/LED-Frosties/?ALLSTEPS","http://www.instructables.com/id/Desktop-Printing-Press/?ALLSTEPS","http://www.instructables.com/id/Sided-childrens-apron/?ALLSTEPS","http://www.instructables.com/id/DIY-Nontoxic-Wood-Stain/?ALLSTEPS","http://www.instructables.com/id/Doll-Friends-are-easy-to-make/?ALLSTEPS","http://www.instructables.com/id/Cross-Stitch-Wood-Necklace/?ALLSTEPS","http://www.instructables.com/id/LED-meets-Wood/?ALLSTEPS","http://www.instructables.com/id/Tie-Dye-Showlaces/?ALLSTEPS","http://www.instructables.com/id/Tie-Dye-Whities/?ALLSTEPS","http://www.instructables.com/id/Dinosaur-Bookends-with-Hot-Glue/?ALLSTEPS","http://www.instructables.com/id/Spray-painted-cushions/?ALLSTEPS","http://www.instructables.com/id/Dip-Dye-Waxed-Thread-Necklace/?ALLSTEPS","http://www.instructables.com/id/Spray-Paint-Stencils/?ALLSTEPS","http://www.instructables.com/id/Thread-Lampshade/?ALLSTEPS","http://www.instructables.com/id/How-to-Sew./?ALLSTEPS","http://www.instructables.com/id/Woven-Wire-Rings/?ALLSTEPS","http://www.instructables.com/id/How-to-sew-a-light-up-plush-Tux-penguin-with-EL-wi/?ALLSTEPS","http://www.instructables.com/id/Obedient-Wood/?ALLSTEPS","http://www.instructables.com/id/Geometric-Wood-Bangle-DIY/?ALLSTEPS","http://www.instructables.com/id/Electric-Violin-1/?ALLSTEPS","http://www.instructables.com/id/Solid-wood-benchcoffee-table/?ALLSTEPS","http://www.instructables.com/id/Polymer-clay-earrings/?ALLSTEPS","http://www.instructables.com/id/DIY-Embroidered-Clay-Rings/?ALLSTEPS","http://www.instructables.com/id/Thread-Painting/?ALLSTEPS"]
#URLlist = ["http://www.instructables.com/id/Knitted-Moustache/","http://www.instructables.com/id/Let-it-Snow-Snowman-Ornament/","http://www.instructables.com/id/Embroidery-101/?ALLSTEPS","http://www.instructables.com/id/Electronic-Embroidery/","http://www.instructables.com/id/Crochet-super-cute-Octopus/","http://www.instructables.com/id/Make-a-quick-box-using-box-joints/?ALLSTEPS","http://www.instructables.com/id/Simple-Storage-Box/?ALLSTEPS","http://www.instructables.com/id/String-Voodoo-Dolls/","http://www.instructables.com/id/Wood-Whittling-101/","http://www.instructables.com/id/Floppy-Disk-Lamp/","http://www.instructables.com/id/Wood-Industrial-Lamp-Desk/?ALLSTEPS","http://www.instructables.com/id/Nail-String-Art-using-reclaimed-wood/","http://www.instructables.com/id/Reclaimed-Wood-Skateboard/?ALLSTEPS","http://www.instructables.com/id/making-concrete-balls/","http://www.instructables.com/id/Conspeakuous-Concrete-Speakers/","http://www.instructables.com/id/DIY-Concrete-Lamp/?ALLSTEPS","http://www.instructables.com/id/Making-Wooden-Knobs-on-a-Drill-Press/","http://www.instructables.com/id/Cork-Board-Project/","http://www.instructables.com/id/Custom-Made-Wax-Candles-Cast-using-Sugru-Moulds/","http://www.instructables.com/id/Pac-man-Cork-Board/?ALLSTEPS","http://www.instructables.com/id/Cork-Board-Project/","http://www.instructables.com/id/LED-Hula-Hoop/?ALLSTEPS","http://www.instructables.com/id/Happy-Poop-Emoji-Made-from-Clay/","http://www.instructables.com/id/Rainbow-Rain-Wax-Art/","http://www.instructables.com/id/LED-Frosties/?ALLSTEPS","http://www.instructables.com/id/Desktop-Printing-Press/?ALLSTEPS","http://www.instructables.com/id/Sided-childrens-apron/?ALLSTEPS","http://www.instructables.com/id/DIY-Nontoxic-Wood-Stain/","http://www.instructables.com/id/Doll-Friends-are-easy-to-make/","http://www.instructables.com/id/Cross-Stitch-Wood-Necklace/","http://www.instructables.com/id/LED-meets-Wood/","http://www.instructables.com/id/Tie-Dye-Showlaces/","http://www.instructables.com/id/Tie-Dye-Whities/","http://www.instructables.com/id/Dinosaur-Bookends-with-Hot-Glue/","http://www.instructables.com/id/Spray-painted-cushions/?ALLSTEPS","http://www.instructables.com/id/Dip-Dye-Waxed-Thread-Necklace/","http://www.instructables.com/id/Spray-Paint-Stencils/","http://www.instructables.com/id/Thread-Lampshade/?ALLSTEPS","http://www.instructables.com/id/Painting-Paper-Mache-Easter-Bunny/?ALLSTEPS"];
allSkills = ["knit","clay","ambroidery","LED","wood","sander","saw", 'dye', 'carve', 'wire', 'thread', 'concrete'];
# ,"Jigsaw"drill,"hot glue","Knife","carve","glue gun","wire","screw","Epoxy","Glue lamp","nails","wood glue","hammer","drill","concrete","electronics","wires","speakers","lamp","cast","mould","Scissors","cork","Drill","clay","wax","screwdriver","sew","stitch","tie-dye","spray paint","bulb","paper mache"

## get the subsets
def list_powerset(lst):
    # the power set of the empty set has one element, the empty set
    result = [[]]
    for x in lst:
        # for every additional element in our set
        # the power set consists of the subsets that don't
        # contain this element (just take the previous power set)
        # plus the subsets that do contain the element (use list
        # comprehension to add [x] onto everything in the
        # previous power set)
        result.extend([subset + [x] for subset in result])
    return result

# the above function in one statement
def list_powerset2(lst):
    return reduce(lambda result, x: result + [subset + [x] for subset in result],
                  lst, [[]])

def powerset(s):
    return frozenset(map(frozenset, list_powerset(list(s))))


def isPermutation(A, B):
    """
    Computes if A and B are permutations of each other.
    This implementation correctly handles duplicate elements.
    """
    # make sure the lists are of equal length
    if len(A) != len(B):
        return False

    # keep track of how many times each element occurs.
    counts = {}
    for a in A:
        if a in counts: counts[a] = counts[a] + 1
        else: counts[a] = 1

    # if some element in B occurs too many times, not a permutation
    for b in B:
        if b in counts:
            if counts[b] == 0: return False
            else: counts[b] = counts[b] - 1
        else: return False

    # None of the elements in B were found too many times, and the lists are
    # the same length, they are a permutation
    return True

def permutInNodes(A):
    for node in nx.nodes(DG):
        if isPermutation(node,A):
            return node
    return False

def makeHeuristic(G):
    def heuristic(a,b):
        As = ast.literal_eval(a)
        Bs = ast.literal_eval(b)
        subsOfA = list_powerset(As)
        if Bs in subsOfA:
            return 1000
        return 0
    return heuristic


'''
Build the graph from a default set of URLs and keywords
'''
def biuldGraph():
    for myurl in URLlist:
        req = urllib.request.Request(myurl)
        words = [""]

        with urllib.request.urlopen(req) as response:
            the_page = str(response.read())
            for skill in allSkills:
                if skill in the_page:
                    if skill not in words:
                        words.append(skill)
        #print(words)


        nodeToAdd = words
        checkOtherNode = permutInNodes(words)

        #create a node for "words" if it doesnt exists
        if checkOtherNode == False:
            DG.add_node(str(nodeToAdd), dificult = len(nodeToAdd))
        else:
            nodeToAdd = checkOtherNode


        #cteate the proper node

        # get all the subsets
        subset = list_powerset(nodeToAdd)

        for sub in subset:
            addsub = sub
            if sub:
                #if sub not in DG:
                checkOtherNode = permutInNodes(addsub)
                if not checkOtherNode:
                    DG.add_node(str(addsub), dificult = len(addsub))
                else:
                    addsub = checkOtherNode

                # add edge to grap
                DG.add_edge(str(addsub), str(nodeToAdd), keyword = myurl)
                DG[str(addsub)][str(nodeToAdd)]['weight'] = (abs(len(addsub) - len(nodeToAdd)))*2 - 1
        #print("done with building")


def getThePath(A,B):
    urlArray = []
    G= nx.astar_path(DG,str(A),str(B),makeHeuristic(DG))
    for i in range(0, len(G)-1):
        print(G[i])
        url = DG.get_edge_data(G[i],G[i+1])['keyword']
        print(url)
        if url not in urlArray:
            urlArray.append(url)
    print(G[-1])
    return urlArray

def getUserWishPath(url, skill):
    '''
    :return:
    '''
    whishProject = url
    knownSkill = skill
    req = urllib.request.Request(whishProject)
    words = []
    with urllib.request.urlopen(req) as response:
        the_page = str(response.read())
        for skill in allSkills:
            if skill in the_page:
                if skill not in words:
                    words.append(skill)

    if str([knownSkill]) in DG:
        print("its in the graph!!")
        urlArray = getThePath([knownSkill], words)
    else:
        print("ERROR")
    return urlArray

def getwords(url):
    req = urllib.request.Request(url)
    words = [""]

    with urllib.request.urlopen(req) as response:
        the_page = str(response.read())
        for skill in allSkills:
            if skill in the_page:
                if skill not in words:
                    words.append(skill)
    return words

print("start Run")
#biuldGraph()
#getUserWishPath()

# #print(DG.(str(['glue', 'Jigsaw', 'lamp', 'cast', 'mould', 'Drill'])))
# G= nx.astar_path(DG,str(['', 'sander']),(str(['', 'dye', 'thread'])),)
# print("the path is")
# for task in G:
#     print(task)
# # print(nx.nodes(DG))
# # #G = nx.all_neighbors(DG,str(['knit', 'glue', 'saw']))
# # print("the neightbors")
# print(DG.neighbors(str(['', 'wood', 'saw', 'dye', 'thread'])))
# # print("the neightbors")
# # print(DG.neighbors(str(['', 'wood', 'sander', 'saw'])))
# #
# # print("attr")
# # print(DG[str(['LED'])][str(['', 'glue', 'LED', 'wood'])]['weight'])
# #
#
# #print(nx.get_node_attributes(DG,str(['knit', 'glue', 'saw'])))
# nx.draw(DG)
#
# plt.savefig("simple_path.png") # save as png
# plt.show() # displ
# print(DG.number_of_edges())
# print(DG.number_of_nodes())