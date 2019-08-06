from numpy import asarray, dot, sort, floor, shape
import tensorflow as tf


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
            median_value, median_index, offset = self.__find_median_in_list(list(sorted_set))
            q1_value, _, _ = self.__find_median_in_list(list(sorted_set)[:median_index])
            q3_value, _, _ = self.__find_median_in_list(list(sorted_set)[median_index+offset:])
            return q1_value, median_value, q3_value
        return False

    @staticmethod
    def __find_median_in_list(information: list):
        median_value, median_index, offset = (0, 0, 0)

        if len(information) % 2 == 0:
            length = len(information)
            median_value = (information[int((length - 1) / 2)] + information[int((length- 1) / 2) + 1]) / 2
            median_index = int(length / 2)
        else:
            length = len(information)
            median_value = information[int((length - 1) / 2)]
            median_index = int(length / 2)
            offset = 1
        return median_value, median_index, offset

    def mean_squared_error(self, true, predicted):
        return tf.losses.mean_squared_error(getattr(self, true), getattr(self, predicted))




