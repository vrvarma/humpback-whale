import numpy as np

def map5_per_image(label, predictions):
    """Computes the precision score of one image.

    Parameters
    ----------
    label : string
            The true label of the image
    predictions : list
            A list of predicted elements (order does matter, 5 predictions allowed per image)

    Returns
    -------
    score : double
    """
    score = 0
    try:
        score = 1 / (predictions[:5].index(label) + 1)
        # print(label, score)
        return score

    except ValueError:
        return 0.0

def map5_per_set(labels, predictions):
    """Computes the average over multiple images.

    Parameters
    ----------
    labels : list
             A list of the true labels. (Only one true label per images allowed!)
    predictions : list of list
             A list of predicted elements (order does matter, 5 predictions allowed per image)

    Returns
    -------
    score : double
    """
    return np.mean([map5_per_image(l, p) for l,p in zip(labels, predictions)])
