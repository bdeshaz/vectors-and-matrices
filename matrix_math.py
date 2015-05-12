class ShapeException(Exception):
    pass

def shape_vectors(vector):

    return (len(vector), )


def vector_add(vector_1, vector_2):

    vector_add_checks_shapes(vector_1, vector_2)

    added_vector = [vector_1[idx] + vector_2[idx] for idx in range(len(vector_1))]

    return added_vector

def vector_add_is_communicative(vector_1, vector_2):
    if vector_add(vector_1, vector_2) == vector_add(vector_2, vector_1):
        return

def vector_add_checks_shapes(vector_1, vector_2):
    if shape_vectors(vector_1) != shape_vectors(vector_2):
        raise ShapeException

def vector_sub(vector_1, vector_2):

    vector_sub_checks_shapes(vector_1, vector_2)

    subtracted_vector = [vector_1[idx] - vector_2[idx] for idx in range(len(vector_1))]

    return subtracted_vector

def vector_sub_checks_shapes(vector_1, vector_2):

    return vector_add_checks_shapes(vector_1, vector_2)

def vector_sum(*args):
    # Need Explaining
    # 1. Why does the args need to be a list
    # 2. Why does it do what it does when it isn't
    # Formula from Ben 

    list_of_vectors = list(args)

    summed_vectors =
     [sum([row[idx] for row in list_of_vectors])
     for idx in range(len(list_of_vectors[0]))]

    return summed_vectors





if __name__ == "__main__":
    pass
