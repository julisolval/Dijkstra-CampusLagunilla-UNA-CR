## Project Overview  
Ever wondered how Waze or Google Maps finds the fastest route to your destination? That's Dijkstra's Algorithm in action. This project applies the same logic to a real map — the campus of Sede Lagunilla, Universidad Nacional (UNA), Costa Rica — finding the shortest walking path from the main building to the main entrance.

## Visual Walkthrough  
The campus is modeled as a weighted graph where:
Nodes = campus locations
Edges = paths between locations
Weights = distance (relative units)


The following diagrams were hand-drawn to show a step-by-step understanding of how the algorithm works — including the 3 hash tables (Graph, Costs, Parents) and how they update at each iteration.

<img width="804" height="1512" alt="image" src="https://github.com/user-attachments/assets/a12b9313-1884-47c8-8ae9-cb5cbf85c76f" />

## Reference  
Bhargava, A. (2024). Grokking Algorithms, 2nd Edition. Manning Publications.
This project is part of a series of real-world algorithm implementations based on the book.
