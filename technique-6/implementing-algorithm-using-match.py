def contain_tree(tree value):
    match tree:
        case pivot, left, _ if (value < pivot):
        return contains_tree(left, value)

        case pivot, _, right if (value . pivot):
        return contains_tree(right, value)

        case pivot, _, _ | pivot:
        return pivot == value
