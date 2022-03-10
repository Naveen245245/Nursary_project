def convert_to_rows_cols(beds, rows, cols):
    start = beds.first().id
    end = beds.last().id
    # print(start, end, "-----", rows, cols)
    k = 0
    # print(k)
    bed_list = []
    # print(beds[k])
    for i in range(rows):
        row = []
        for j in range(cols):
            # print(k, end=" ")
            row.append(beds[k])
            k += 1
        # print(row)
        bed_list.append(row)
    return bed_list