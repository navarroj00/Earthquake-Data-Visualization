'''
This program reads the given processed files and informs the user of how many earthquakes exist, the largest and smallest magnitudes, and returns different attributes (mean, median, mode, and range) of the given magnitudes. In terms of plotting, the program generates a window that plots magnitudes with different colors according to their intensities.
Authors: Jordan Navarro and Bridger Rives
CS 111, Fall 2018
Date: 12 October 2018
'''

# Imported Python graphics and statistics (https://docs.python.org/3/library/statistics.html) libraries to gain ability to generate windows and calculate mode of data set.
from graphics import *
from statistics import mode

def processFile(f):
    '''
    Reads the data in a file and stores it into an accessable list.

    PARAMETER:
        f - This is the name of the file.

    RETURN VALUE:
        The expected return value is a list containing data from the file.
    '''
    # Create the "lst" array and read through each line of the file, stripping each line of extra characters, converting each string into a float, and appending it to the array. Afterwards, close the file and return the array.
    lst = []
    infile = open(f, "r")
    for line in infile:
        line = line.strip()
        value = float(line)
        lst.append(value)

    infile.close()
    return lst

def plotLocations(lats, longs):
    '''
    Plots the earthquakes according to their latitudes and longitudes, with different colors being representative of different intensities of magnitudes.

    PARAMETERS:
        lats - This is the latitude of the earthquake.
        longs - This is the longitude of the earthquake.

    RETURN VALUE:
        None, besides a positioning on the image we have used as a world map. 
    '''
    # Create the graphics window applied with an image of a world map.
    mags = processFile("magnitudesMonth.txt")
    win = GraphWin("Month's Earthquakes", 448, 266)
    win.setCoords(-180, -90, 180, 90)
    earth = Image(Point(0, 0), "worldmap.gif")
    earth.draw(win)

    # Draw each latitude and longitude on the world map in turn, labeling them as colors according to their intensities.
    for i in range(len(lats)):
        pt = Point(lats[i], longs[i])
        loc = Circle(pt, 1)
        if mags[i] == min(mags):
            loc.setFill("dark green")
            loc.draw(win)
        elif mags[i] == max(mags):
            loc.setFill("purple")
            loc.draw(win)
        elif mags[i] < 3:
            loc.setFill("yellow")
            loc.draw(win)
        elif mags[i] >= 3 and mags[i] < 5:
            loc.setFill("orange")
            loc.draw(win)
        elif mags[i] >= 5 and mags[i] < 7:
            loc.setFill("red")
            loc.draw(win)
        elif mags[i] > 7:
            loc.setFill("brown")
            loc.draw(win)
        
    # Keep the graphics window open until we close it.    
    win.getMouse()
    win.close()

def mean(lst):
    '''
    Calculates the average value within a list of values.

    PARAMETER:
        lst - This is the list of values.

    RETURN VALUE:
        The expected return value is the average of the list of values in the data set.
    '''
    # Accumulates the sum depending on the value of each item in the list.
    sum = 0
    numItems = len(lst)
    for value in lst:
        sum = sum + value

    # Calculates the average by dividing the sum over the number of items in the list.
    avg = sum / numItems
    return avg

def median(lst):
    '''
    Calculates the median value within a list of values.
    
    PARAMETER:
        lst - This is the list of values.

    RETURN VALUE:
        The expected return value is the median of the list of values in the data set.
    '''
    # Sorts the list lexicographically and calculates the median by firstly checking for a remainder of 0 (to ensure that the median is a division of two median values) or not 0 (to ensure that the median is one value).
    lst.sort()
    numItems = len(lst)
    midIndex = numItems // 2
    if (numItems % 2 == 0):
        sum = lst[midIndex] + lst[midIndex - 1]
        med = sum / 2
    else:
        med = lst[midIndex]
    return med

def main():
    # Read the designated files for each variable and stores them in the "lst" list array that was defined earlier in the program.
    mags = processFile("magnitudesMonth.txt")
    lats = processFile("latitudesMonth.txt")
    longs = processFile("longitudesMonth.txt")

    # Prints out the amount of earthquakes in the data set, the largest magnitude in the data and which earthquake owns that magnitude, and the smallest magnitude in the data and which earthquake owns that magnitude (it prints the lowest index earthquake in the case of multiple entities).
    print ("There are", len(mags), "earthquakes in this data set.\n")
    print ("The largest magnitude in the data set is", max(mags), "and earthquake", (mags.index(max(mags)) + 1), "has this magnitude.\n")
    print ("The smallest magnitude in the data set is", min(mags), "and earthquake", (mags.index(min(mags)) + 1), "has this magnitude.\n")

    # Prints out the mean, median, mode, and range of the magnitudes stored in the "lst" list array that was defined earlier in the program.
    print("Mean of Magnitudes:", mean(mags))
    print("Median of Magnitudes:", median(mags))
    print("Mode of Magnitudes:", mode(mags))
    print("Range of Magnitudes:", max(mags) - min(mags))
    
    # Applies the placement of the earthquakes according to their latitudes and longitudes.
    plotLocations(longs, lats)

main()
