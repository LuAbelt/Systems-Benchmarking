from statistics import mean

from signal_processing_algorithms.energy_statistics import energy_statistics


def jump_detection(time_series, relative_threshold = 0.05):
    jump_points = []

    idx=1
    last_point = time_series[0]

    for current_point in time_series[1:]:
        relative_change = abs((current_point/last_point)-1)

        if relative_change > relative_threshold:
            jump_points.append(idx)

        idx+=1
        last_point = current_point

    return jump_points

def trend_detection(time_series, window_length,threshhold):
    jump_points = []

    idx = window_length
    while idx < len(time_series):
        moving_average = mean(time_series[idx-window_length:idx-1])

        relative_change = abs((time_series[idx] / moving_average) - 1)

        if relative_change > threshhold:
            jump_points.append(idx)

        idx+=1

    return jump_points

def e_divisive_analysis(time_series):
    change_points = energy_statistics.e_divisive(time_series, pvalue=0.1, permutations=100)
    if len(change_points) == 0:
        return dict()

    result = dict()

    for idx in range(1,len(time_series)):
        print(idx)
        partial_changepoints = energy_statistics.e_divisive(time_series[:idx], pvalue=0.1, permutations=100)

        for cp in change_points:
            if cp in result:
                continue

            if cp in partial_changepoints:
                result[cp] = idx

    return result