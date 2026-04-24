import math

graph = {}
graph["START"]     = {}
graph["START"]["ParkingLot_A"] = 2
graph["START"]["ParkingLot_B"] = 6
graph["START"]["ParkingLot_C"] = 2
graph["ParkingLot_A"] = {}  
graph["ParkingLot_A"]["Library"] = 10
graph["Library"] = {} 
graph["Library"]["ParkingLot_B"] = 4
graph["ParkingLot_B"] = {}  
graph["ParkingLot_B"]["ParkingLot_D"] = 10
graph["ParkingLot_C"] = {}
graph["ParkingLot_C"]["ParkingLot_D"] = 5
graph["ParkingLot_D"] = {} 
graph["ParkingLot_D"]["FINISH"] = 2
graph["FINISH"] = {}


infinity = math.inf
costs = {}
costs["ParkingLot_A"] = 2
costs["ParkingLot_B"] = 6
costs["ParkingLot_C"] = 2
costs["ParkingLot_D"] = infinity
costs["Library"] = infinity
costs["FINISH"] = infinity

parents = {}
parents["ParkingLot_A"] = "START"
parents["ParkingLot_B"] = "START"
parents["ParkingLot_C"] = "START"
parents["ParkingLot_D"] = None
parents["Library"] = None
parents["FINISH"] = None



processed = []
def find_lowest_cost_node(costs):
    lowest_cost = infinity
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

node = find_lowest_cost_node(costs)

while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)

print("Cost to FINISH:", costs["FINISH"])