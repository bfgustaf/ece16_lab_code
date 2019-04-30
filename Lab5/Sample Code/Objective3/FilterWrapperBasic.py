import scipy.signal as sig


# Filter object to filter data given as np array
class Filter:

    # sampling_frequency:   sampling frequency of the data (in Hz)
    # filter_frequency:     cutoff frequency of the desired filter (in Hz)
    # filter_type:          type of filter, either 'low' (lowpass) or 'high' (highpass).
    # filter_order:         order of the desired filter. Default is 3.
    def __init__(self, sampling_frequency, filter_frequency, filter_type, filter_order=3):

        # Calculate b and a of the Butterworth filter
        # Calculate the initial zi (not scaled for data)


            
    # Filter the data coming in
    # data_in:      np array
    # returns:      filtered value as a np array
    def process_data(self, data_in):
        # If this is the first time this function is called, scale zi
        #    hint: you could use a variable that keeps track of whether it is the first time or not (and initialize it in __init__)
        # Apply the Butterworth filter with the calculated b,a to data_in



