class TreeEnsemble():
    def __init__(self, x, y, n_trees, sample_sz, min_left=5):
        np.random.seed(42)
        self.x, self.y, self.sample_sz
