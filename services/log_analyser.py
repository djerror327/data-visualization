import matplotlib.pyplot as plt


def create_chart():
    x_error = []
    y_error = []
    x_info = []
    y_info = []
    x_debug = []
    y_debug = []
    error_type, debug_type, info_type = get_categorized_types()
    # error type chart
    for error in error_type:
        y_error.append(error[0])
        x_error.append(error[1])
    for debug in debug_type:
        y_debug.append(debug[0])
        x_debug.append(debug[1])
    for info in info_type:
        y_info.append(info[0])
        x_info.append(info[1])
    plt.plot(x_error, y_error)
    plt.plot(x_info, y_info)
    # plt.plot(x_debug, y_debug)
    plt.xlabel('Log type by time')
    plt.ylabel('Count')
    plt.title('Log Analysis')
    # plt.show()

    return x_error, y_error, x_info, y_info


def get_categorized_types():
    grouped_data = []
    with open('../recources/app.log-analysis') as file:
        data_set = []
        for line in file:
            data_set.append(line[0:27])
        for data in data_set:
            count = 0
            for data2 in data_set:
                if data == data2:
                    count += 1
                    # grouped_data.add([count, data[0:27]])
            grouped_data.append([count, data[0:27]])
        # print(grouped_data)
    # filter DEBUG, ERROR, INFO
    error_type = []
    debug_type = []
    info_type = []

    # remove duplicates
    distinct_grouped_data = []
    for i in grouped_data:
        if i not in distinct_grouped_data:
            distinct_grouped_data.append(i)
    # print(distinct_grouped_data)

    for log_type in distinct_grouped_data:
        if (log_type[1])[0:5] == 'DEBUG':
            debug_type.append(log_type)
        elif (log_type[1])[0:5] == 'ERROR':
            error_type.append(log_type)
        elif (log_type[1])[0:4] == 'INFO':
            info_type.append(log_type)
    return error_type, debug_type, info_type


def get_chart_data():
    x_error, y_error, x_info, y_info = create_chart()
    data = {'x_error': [x_error, y_error], 'x_info': [x_info, y_info]}
    print(data)
    # data.append(x_info, y_info)
    return data


get_chart_data()
