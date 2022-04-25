def insert_separator(items, separator):
    return_text = ""
    first_items = items[0:-1]
    for item in first_items:
        return_text += str(item)
        return_text += separator
    return_text += str(items[-1])
    return return_text

def get_comparison_symbol(text):
    if text == "greater":
        return ">"
    if text == "less":
        return "<"
    if text == "equality":
        return "="

def get_source(t):
    source = list(t.find_data("table_name"))
    return source[0].children[0]

def get_conditions(t):
    conditions = list(t.find_data("conditions"))
    if(len(conditions) > 0):
        condition_list = []
        for condition in conditions[0].children:
            if(condition == None):
                break
            condition_type = condition.data
            lhs = condition.children[0]
            rhs = condition.children[1]
            if(not rhs.isnumeric()):
                rhs = "'" + rhs + "'"
            condition_list.append(lhs + " " + get_comparison_symbol(condition_type) + " " + rhs)
        return " WHERE " + insert_separator(condition_list," and ")
    return ""

def eval_tree(t):
    command_type = t.children[0].data
    if(command_type == "select"):
        return eval_select(t)
    if(command_type == "count"):
        return eval_count(t)

def eval_count(t):
    sql_text = "SELECT COUNT(*)"
    sql_text += " FROM " + get_source(t) 
    sql_text += get_conditions(t)
    return sql_text


def eval_select(t):
    sql_text = "SELECT"

    #-------columns-------#
    columns = list(t.find_data("selected_columns"))
    column_list = []
    if(len(columns) > 0):
        for column in columns[0].children:
            column_list.append(column)
        sql_text += " " + insert_separator(column_list,", ")
    else:
        sql_text += " *"


    #-------table source-------#
    sql_text += " FROM " + get_source(t) 

    #-------conditions-------#
    sql_text += get_conditions(t)
    
    #-------ordering-------#
    order = list(t.find_data("order"))
    if(len(order) > 0):
        order_column = order[0].children[0]
        sql_text += " ORDER BY " + order_column + " "
        if(order[0].children[1] == None):
            sql_text += "desc"
        else:
            sql_text += order[0].children[1].data

    #row limit
    row_limit = list(t.find_data("row_limit"))
    if(len(row_limit) > 0):
        sql_text += " LIMIT " + row_limit[0].children[0]
        
    return sql_text