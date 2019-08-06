from numpy import asarray, dot, sort, floor


class LocalDataset:

    def __init__(self, **dataset):
        for key, value in dataset:
            insertion_information = asarray(value)
            setattr(self, key, insertion_information)

    def perform_matrix_multiplication(self, arg1, arg2):
        """ Takes in arguments of the function and return their dot product """
        return dot(getattr(self, arg1), getattr(self, arg2))

    def q_information(self, arg1):
        """ Returns quartile information about the dataset """
        operating_dataset = getattr(self, arg1)
        if operating_dataset.dtype == 'int32':
            sorted_set = sort(operating_dataset)
            median_index = floor(sorted_set.size / 2)
            q1 = floor(median_index / 2)
            q3 = floor(sorted_set.size)


