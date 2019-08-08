from math import sqrt


class KNN:
    def __init__(self, x, y, labels, k):
        self.x = x
        self.y = y
        self.labels = labels
        self.k = k

    def __distance_formula(self, x_point, y_point):
        return sqrt((self.x - x_point) ** 2 + (self.y - y_point) ** 2)

    def __get_label(self, distance_matrix):
        distance_label_dict = {}
        for i in list(self.labels):
            if list(self.labels[i]) in distance_label_dict:
                distance_label_dict.update({list(self.labels[i]): distance_label_dict.get(list(self.labels[i])) + 1})
            else:
                distance_label_dict.update({list(self.labels[i]): 1})

        return distance_label_dict

    def get_assigned_value(self, x_point, y_point):
        distance_matrix = self.__distance_formula(x_point, y_point)
        distance_label_dict = self.__get_label(distance_matrix)
        label = 'NULL'
        largest_label = 0
        '''for testing purposes'''
        for key, value in distance_label_dict:
            if value > largest_label:
                largest_label = value
                label = key
        print("The point at (", x_point, y_point, ") is of the label", label)


    def graph_function(self):
        pass


