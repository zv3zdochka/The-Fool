import matplotlib.pyplot as plt
import numpy as np


class Angle:
    def __init__(self):
        self.coordinates = None
        self.g_len = None
        self.end_len = None

    def draw(self):
        fig, ax = plt.subplots()

        x_coords, y_coords = zip(*self.coordinates)
        ax.plot(x_coords, y_coords, 'r', label='Отрезок')

        ax.legend()
        plt.show()

    def merge_co(self):
        mer_list = []
        flag = False
        for i in range(len(self.coordinates) - 2):
            if flag:
                flag = False
                continue
            x1, y1 = self.coordinates[i]
            x2, y2 = self.coordinates[i + 1]
            x3, y3 = self.coordinates[i + 2]

            vec1 = np.array([x1 - x2, y1 - y2])
            vec2 = np.array([x3 - x2, y3 - y2])

            angle = np.arccos(np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2)))
            angle_degrees = np.degrees(angle)
            if angle_degrees > 145:
                mer_list.append((x1, y1))
                mer_list.append((x3, y3))
                flag = True

        return self.clear(mer_list)

    @staticmethod
    def clear(get):
        unique_coordinates = []
        visited = set()
        for coordinate in get:
            if coordinate not in visited:
                unique_coordinates.append(coordinate)
                visited.add(coordinate)
        unique_coordinates.append(get[0])
        return unique_coordinates

    @staticmethod
    def convert(my_list):
        return [tuple(sublist) for sublist in my_list]

    @staticmethod
    def remove_close_points(points):
        distance = 10
        filtered_points = []
        for point in points:
            keep = True
            for f_point in filtered_points:
                if abs(point[0] - f_point[0]) <= distance and abs(point[1] - f_point[1]) <= distance:
                    keep = False
                    break
            if keep:
                filtered_points.append(point)
        return filtered_points

    def select(self):
        x_coords = [coord[0] for coord in self.coordinates]
        y_coords = [coord[1] for coord in self.coordinates]

        center_x = sum(x_coords) / len(x_coords)
        center_y = sum(y_coords) / len(y_coords)

        shifted_x = [coord[0] - center_x for coord in self.coordinates]
        shifted_y = [coord[1] - center_y for coord in self.coordinates]

        fig, ax = plt.subplots()
        ax.scatter(shifted_x, shifted_y)

        polygon = plt.Polygon(list(zip(shifted_x, shifted_y)), closed=True, fill=None)
        ax.add_patch(polygon)

        min_y_index = shifted_y.index(min(shifted_y))
        lower_edge = [(shifted_x[min_y_index], shifted_y[min_y_index]),
                      (shifted_x[min_y_index + 1], shifted_y[min_y_index + 1])]

        # print("Lower Edge co:", lower_edge)

        ax.plot([lower_edge[0][0], lower_edge[1][0]], [lower_edge[0][1], lower_edge[1][1]], 'b')

        plt.axis('equal')
        plt.show()
    @staticmethod
    def calculate_angle(line_co):
        pass

    def do(self, co):
        self.coordinates = self.convert(co)
        self.draw()
        self.coordinates = self.remove_close_points(self.coordinates)
        self.draw()
        self.end_len = len(self.coordinates)
        while True:
            m_l = self.merge_co()
            if len(m_l) == self.end_len:
                break
            else:
                self.end_len = len(m_l)
                self.coordinates = m_l
                self.draw()
            if self.end_len <= 12:
                break
        self.select()


if __name__ == "__main__":
    coordinates = [[194, 78], [193, 79], [184, 79], [183, 80], [175, 80], [174, 81], [166, 81], [165, 82], [157, 82],
                   [156, 83], [148, 83], [147, 84], [137, 84], [136, 85], [127, 85], [126, 86], [118, 86], [117, 87],
                   [109, 87], [108, 88], [100, 88], [99, 89], [91, 89], [90, 90], [79, 90], [78, 91], [71, 91],
                   [70, 92],
                   [69, 92], [68, 93], [66, 93], [64, 95], [63, 95], [60, 98], [60, 99], [58, 101], [58, 102],
                   [57, 103],
                   [57, 104], [56, 105], [56, 108], [55, 109], [55, 114], [56, 115], [56, 122], [57, 123], [57, 132],
                   [58, 133], [58, 141], [59, 142], [59, 152], [60, 153], [60, 162], [61, 163], [61, 171], [62, 172],
                   [62, 179], [63, 180], [63, 189], [64, 190], [64, 198], [65, 199], [65, 209], [66, 210], [66, 219],
                   [67, 220], [67, 228], [68, 229], [68, 237], [69, 238], [69, 246], [70, 247], [70, 255], [71, 256],
                   [71, 267], [72, 268], [72, 276], [73, 277], [73, 285], [74, 286], [74, 294], [75, 295], [75, 303],
                   [76, 304], [76, 306], [212, 306], [213, 305], [215, 305], [215, 234], [214, 233], [214, 220],
                   [213, 219],
                   [213, 209], [212, 208], [212, 195], [211, 194], [211, 181], [210, 180], [210, 177], [209, 176],
                   [209, 168], [210, 167], [209, 166], [210, 165], [209, 164], [210, 163], [208, 161], [209, 160],
                   [209, 155], [208, 154], [208, 138], [207, 137], [207, 128], [206, 127], [206, 98], [207, 97],
                   [207, 92],
                   [208, 91], [208, 88], [209, 87], [209, 86], [210, 85], [210, 84], [211, 83], [211, 82], [212, 81],
                   [212, 80], [214, 78]]
    A = Angle()
    A.do(coordinates)
