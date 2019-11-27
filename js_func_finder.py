def list_all_js_function_names(path_to_js_file):
    """
    path_to_js_file is a path to a file on your hard drive
    This function will read the entire input file and then return a list of js function names as strings
    """
    func_names = []
    start_row_list =[]
    output = []
    with open(path_to_js_file) as f:
        for i, each_line in enumerate (f.readlines()):
            if "function" in each_line:
                if "function" not in each_line.split(" ")[0] :
                    func_names.append(each_line.split(" ")[0])
                    start_row_list.append(i + 1)
                else:
                    func_names.append(each_line.split("()")[0]
                           .split("(")[0]
                           .split("function")[-1]
                           .split(" ")[1])
                    start_row_list.append(i + 1)
    for index, value in enumerate(func_names):
        output.append({"name": value, "start_row": start_row_list[index]})

    return output

print(list_all_js_function_names("newfile.js"))