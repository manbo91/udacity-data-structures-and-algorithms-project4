from math import sqrt
import heapq


def get_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))


def shortest_path(M, start, goal):
    inters = M.intersections
    roads = M.roads

    g, h = 0, get_distance(inters[start], inters[goal])
    distance_heap = [(g + h, g, h, start)]
    shortest_path = {start: None}
    visited = set()

    def traverse_roads(roads, inter, start_h, start_g, asterisk=True):
        for road in roads[inter]:
            if road not in visited:
                g = get_distance(inters[road], inters[inter]) + start_g
                h = get_distance(inters[road], inters[goal])
                f = g + h

                if not asterisk or h < start_h:
                    heapq.heappush(distance_heap, (f, g, h, road))
                    shortest_path[road] = inter
                    visited.add(road)

    while len(distance_heap) > 0:
        f, g, h, inter = heapq.heappop(distance_heap)
        visited.add(inter)

        if inter == goal:
            break

        traverse_roads(roads, inter, h, g)
        if len(distance_heap) == 0:  # If all h has increased
            traverse_roads(roads, inter, h, g, False)

    inter = goal
    path = list()
    while inter in shortest_path:
        path.append(inter)
        inter = shortest_path[inter]

    path.reverse()
    return path
