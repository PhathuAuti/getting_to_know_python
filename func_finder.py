def list_all_js_function_names(path_to_js_file):
    """
    path_to_js_file is a path to a file on your hard drive
    This function will read the entire input file and then return a list of js function names as strings
    """
    names = []
    with open(path_to_js_file, 'r') as f:
        x = f.readlines()
    
    for each_element in x:
        if 'function' in each_element:
            elements = each_element.split(" ")
            
            for i, each_char in enumerate(elements):
                if elements[2] == "function(){":
                   names.append(elements[0])
                if elements[0] == 'function':
                   names.append(elements[1])
    firstfunc = (names[0].split("()"))[0]
    return [firstfunc, names[-1]]        

print(list_all_js_function_names("newfile.js"))
