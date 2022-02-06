import numpy as np


def lhs(n_dim, n_sample, init_array=None):
    grid_array = np.linspace(0, n_sample-1, n_sample)
    
    def _sample_from_idx(lhs_idx):
        _n_sample = lhs_idx.shape[0]
        lhs_result = np.zeros([_n_sample, n_dim])
        for i in range(_n_sample):
            for j in range(n_dim):
                lhs_result[i, j] = (np.random.rand() + lhs_idx[i, j])/n_sample
        return lhs_result

    if init_array is not None:
        # get the index for the initial lhs result and the number of sample
        old_lhs_idx = np.floor(init_array / (1/n_sample)).astype('int32')
        old_n_sample = init_array.shape[0]

        new_n_sample = n_sample-old_n_sample
        new_lhs_idx = np.zeros([new_n_sample, n_dim])

        for i in range(n_dim):
            # remove the old index and permutation
            new_lhs_idx[:, i] = np.random.permutation(np.delete(grid_array, old_lhs_idx[:, i], 0))

        new_lhs_result = _sample_from_idx(new_lhs_idx)

        lhs_idx = np.concatenate([old_lhs_idx, new_lhs_idx], axis=0)
        lhs_result = np.concatenate([init_array, new_lhs_result], axis=0)

    else:
        # array for storing the index
        lhs_idx = np.zeros([n_sample, n_dim])
        for i in range(n_dim):
            lhs_idx[:, i] = np.random.permutation(grid_array)
        # array for storing values
        lhs_result = _sample_from_idx(lhs_idx)
    return lhs_result
