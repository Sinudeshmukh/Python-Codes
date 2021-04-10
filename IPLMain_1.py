#Approach 1

#from package import module
from IPL2021 import venue

venue.printVenue()
venue.printStadium()

# Approach2

#from package.module import func
from IPL2021.venue import printVenue
printVenue()