from numpy import asarray, dot, sort, floor


class LocalDataset:

    def __init__(self, **dataset):
        """ Creates a local dataset based off of the keys and values of those keys given by the user"""
        for key, value in dataset.items():
            insertion_information = asarray(value)
            setattr(self, key, insertion_information)

    def perform_matrix_multiplication(self, arg1, arg2):
        """ Takes in arguments of the function and return their dot product """
        return dot(getattr(self, arg1), getattr(self, arg2))

    def q_information(self, arg1):
        """ Returns quartile information about the dataset """
        operating_dataset = getattr(self, arg1)
        if operating_dataset.dtype == 'int32' and operating_dataset.size > 3:
            sorted_set = sort(operating_dataset)
            if type(sorted_set.size / 2) == 'int':
                median_value = ((sorted_set.tolist()[floor(sorted_set.size / 2)] + sorted_set.tolist()[
                    floor(sorted_set.size) / 2 + 1]) / 2)
            else:
                median_value = sorted_set.tolist()[sorted_set.size / 2]
            if type(sorted_set.size / 4) == 'int':
                q1_value = (sorted_set.tolist()[floor(sorted_set.size / 4)] + sorted_set.tolist()[
                    floor(sorted_set.size) / 4 + 1]) / 2
            else:
                median_value = sorted_set.tolist()[sorted_set.size / 4]
            return median_value, q1_value
        return False

    #def mean_squared_error(self, arg1, arg2):




