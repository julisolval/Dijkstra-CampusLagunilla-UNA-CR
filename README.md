## Project Overview  
Ever wondered how Waze or Google Maps finds the fastest route to your destination? That's Dijkstra's Algorithm in action. This project applies the same logic to a real map, the campus of Sede Lagunilla, Universidad Nacional (UNA), Costa Rica, finding the shortest walking path from the main building to the main entrance.

## Visual Walkthrough  
The campus is modeled as a weighted graph where:
- Nodes = campus locations
- Edges = paths between locations
- Weights = distance (relative units)

The following diagrams were hand-drawn to show a step-by-step understanding of how the algorithm works, including the 3 hash tables (Graph, Costs, Parents) and how they update at each iteration.

<img width="804" height="1512" alt="image" src="https://github.com/user-attachments/assets/a12b9313-1884-47c8-8ae9-cb5cbf85c76f" />
Note: Some iterations show no update, this happens when the newly calculated cost to reach a neighbor is equal to or greater than the cost already recorded. The algorithm only updates when it finds a strictly cheaper path.

## Future Improvements  
- Implement **A\* (A-Star) Algorithm** as an optimized alternative to Dijkstra. A\* uses a heuristic function to prioritize nodes closer to the destination, making it significantly faster for large maps. This is the actual algorithm used by Google Maps and Waze in production.
- Add real GPS coordinates for each campus location
- Accept dynamic user input to choose start and finish points

## Reference  
Bhargava, A. (2024). Grokking Algorithms, 2nd Edition. Manning Publications.
