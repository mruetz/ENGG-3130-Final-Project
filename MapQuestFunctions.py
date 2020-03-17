#Taken from the MapQuest Directions API documentation.

#This file contains MapQuest functions that could be valuable.

from RouteOptions import RouteOptions
from AdvancedRouteOptions import AdvancedRouteOptions
from RouteShapeOptions import RouteShapeOptions
from RouteService import RouteService

if __name__ == '__main__':
    options = RouteOptions()
    service = RouteService('YOUR_MAPQUEST_DEVELOPER_API_KEY') # our key is "dAGkCaPVqA3OcC5ws2Lfv8wsR9ro45oe"

    location_list = ['Lancaster, PA', 'York, PA'] #First convert given addresses to Lat/Long values.
    #latLon values can be given in list form using JSONs
    
    # eg.  location_list=[{'latLng':{'lng':43.488369,'lat':-80.207687}},{'latLng':{'lng':43.63656,'lat':-79.39722}}]

    multi_location_list = ['Lancaster, PA', 'State College, PA', 'York, PA']

    # directions
    dirRoute1 = RouteService.directions(locations=['Lancaster, PA', 'York, PA'])

    dirRoute2 = RouteService.directions(locations=['Lancaster, PA', 'York, PA'], options=options)

    dirRoute3 = RouteService.directions(locations=location_list)
    
    multiDirRoute = RouteService.directions(locations=multi_location_list, options=options)
    
    # alternate route
    
    #This function can be used to get a SET of possible routes, which can be compared using
    #additional factors like load weight applied.
    altRoute = RouteService.alternateRoute(locations=['Lancaster, PA', 'York, PA'])
    altRouteWithOptions = RouteService.alternateRoute(locations=['Lancaster, PA', 'York, PA'], maxRoutes=2, timeOverage=26)
    
    altRouteWithDefaultOptions = RouteService.alternateRoute(locations=locations, options=options)
    altRouteWithDefaultAndCustomOpts = RouteService.alternateRoute(locations=locations, maxRoutes=2, timeOverage=26, options=options)


    # route matrix
    
    #This function can create a MATRIX of distances between points in the locations.
    #Each ROW and COL in the matrix can be multiplied by the factor of how important
    #the load weight is, multiplied by the specific load weight for that drop.
    routeMatrix = RouteService.routeMatrix(locations=locations,allToAll=True)

