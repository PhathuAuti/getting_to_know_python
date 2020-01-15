def list_all_js_function_names(path_to_js_file):
    """
    path_to_js_file is a path to a file on your hard drive
    This function will read the entire input file and then return a list of js function names as strings
    """
    # names = []
    dictionary_array = []
    with open(path_to_js_file, 'r') as f:
        lines_list = f.readlines()
    for each_element in lines_list:
        if 'function' in each_element and '=' in each_element:
            func_line_list = each_element.split("=")
            func_name = func_line_list[0];
            # names.append(func_line_list[0])
            line_num =  lines_list.index(each_element) + 1

            funct_dict = {}
            funct_dict['name'] = func_name

            func_start_line = line_num
            funct_dict['start_row'] = func_start_line
            end_line = 0
            for i in range(line_num, len(lines_list)):
                current_line = lines_list[i]
                if current_line[0] == '}':
                    end_line = i + 1
                    break
            funct_dict['end_row'] = end_line
            dictionary_array.append(funct_dict)

        else:
            if 'function' in each_element and '=' not in each_element:
                func_line_list = each_element.split(" ")
                func_name = func_line_list[1].split("(")[0]
                line_num =  lines_list.index(each_element) + 1
                funct_dict = {}

                funct_dict['name'] = func_name

                func_start_line = line_num
                funct_dict['start_row'] = func_start_line
                end_line = 0
                for i in range(func_start_line, len(lines_list)):
                    current_line = lines_list[i]
                    if current_line[0] == '}':
                        end_line = i + 1
                        break
                funct_dict['end_row'] = end_line
                dictionary_array.append(funct_dict)
            # names.append(func_name)
            # dictionary_array.pop()
    return dictionary_array

print(list_all_js_function_names("newfile.js"))