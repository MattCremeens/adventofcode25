from typing import List


if __name__ == '__main__':

    def merge(intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        # Sort the intervals based on the starting points
        intervals.sort(key=lambda x: x[0])

        merged_intervals = [intervals[0]]

        for current in intervals[1:]:
            last_merged = merged_intervals[-1]

            # If the current interval overlaps with the last merged interval, merge them
            if current[0] <= last_merged[1]:
                last_merged[1] = max(last_merged[1], current[1])
            else:
                # Otherwise, add the current interval to the merged list
                merged_intervals.append(current)

        return merged_intervals

    f = open('./data/input5.txt')
    lines = f.readlines()
    id_ranges = []
    ids = []
    for line in lines:
        if '-' in line:
            id_ranges.append(line.replace('\n', ''))
        elif line != '\n':
            ids.append(line.replace('\n', ''))

    intervals = []
    for id_range in id_ranges:
        left_endpoint = int(id_range.split('-')[0])
        right_endpoint = int(id_range.split('-')[1])
        intervals.append([left_endpoint, right_endpoint])

    merged_intervals = merge(intervals)
    print(merged_intervals)
    cnt = 0
    for i in merged_intervals:
        cnt += i[1] - i[0] + 1

    print(cnt)













