# ENGG*3130 - Modeling Complex Systems
## Final Project

import io
import networkx as nx
import numpy as np
import json
import string
import matplotlib.pyplot as plt

from itertools import combinations 

# Import MapQuest API Libraries from https://github.com/MapQuest/directions-api-python-client somehow
from RouteOptions import RouteOptions
from AdvancedRouteOptions import AdvancedRouteOptions
from RouteShapeOptions import RouteShapeOptions
from RouteService import RouteService
%matplotlib inline

static_lat_longs={'origin'=(43.488369,-80.207687),
                  'a1'=(43.63656,-79.39722),
                  'a2'=(43.64136,-79.37962),
                  'a3'=(43.64788,-79.3885),
                  'a4'=(43.64835,-79.38149),
                  'a5'=(43.64882,-79.37307),
                  'a6'=(43.64961,-79.37098),
                  'a7'=(43.6497,-79.37157),
                  'a8'=(43.65156,-79.37241),
                  'a9'=(43.65671,-79.37609),
                  'a10'=(43.65769,-79.3815)
                 }

"""MapQuest API is used to find potential routes between any two points in the lat-long array"""

#altRoute = service.alternateRoute(locations=['Lancaster, PA', 'York, PA'])

def calc_edge(l1, l2, factor=None):
    """Calculate the edge weight based on certain factors"""
    lat_1 = static_lat_longs[static_lat_longs.get(l1)][0]
    long_1 = static_lat_longs[static_lat_longs.get(l1)][1]
    lat_2 = static_lat_longs[static_lat_longs.get(l2)][0]
    long_2 = static_lat_longs[static_lat_longs.get(l2)][1]
    
    options = RouteOptions()
    service = RouteService('YOUR_MAPQUEST_DEVELOPER_API_KEY')
    
    if factor is None or factor is 'dist':
      # MapQuest distance from l1 to l2
      route = RouteService.directions(lat_1,long_1,lat_2,long_2)
    return route.distance
      
    elif factor is 'time':
      route = RouteService.directions(lat_1,long_1,lat_2,long_2)
      return route.realTime
    
    elif factor is 'dist/time'
      # MapQuest time divided by distance
      
    elif factor is 'fuel':
      # Mapquest distance from l1 to l2 
      # Taking weight into account for fuel efficiency
      # Use the weight_point_for_load() method
      
def weight_point_for_load(point):
    """Takes a delivery destination. Incorporates
    a load size based on a specified weighing factor. (changes the
    effective distance from this point to all others)"""

    load_factor_weight = 0.5 #experiment with different weights of this factor
    
    return weighted_loc
  
def create_graph(nodes:
  G = nx.DiGraph()
  G.add_nodes_from(nodes)
  drive_times = {}
  all_nodes = static_lat_longs.keys()
  all_combs = combinations(all_nodes, 2) 
  for i in len(list(all_combs)):
      drive_times.add(list(all_combs)[i], calc_edge(list(all_combs)[i][0],list(all_combs)[i][1]), 'dist')
  G.add_edges_from(drive_times)
  # nx.shortest_path() investigation
