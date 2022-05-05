# pylint: disable=missing-docstring
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
    raise Exception("Invalid comparison type")

def get_source(tree):
    source = list(tree.find_data("table_name"))
    if(len(source) == 0):
        raise Exception("Could not find table name")
    return source[0].children[0]

def get_conditions(tree):
    conditions = list(tree.find_data("conditions"))
    if(len(conditions) > 0):
        condition_list = []
        for condition in conditions[0].children:
            if(condition is None):
                break
            condition_type = condition.data
            lhs = condition.children[0]
            rhs = condition.children[1]
            if(not rhs.isnumeric()):
                rhs = "'" + rhs + "'"
            condition_list.append(lhs + " " + get_comparison_symbol(condition_type) + " " + rhs)
        return " WHERE " + insert_separator(condition_list," and ")
    return ""

def eval_tree(tree):
    command_type = tree.children[0].data
    if(command_type == "select"):
        return eval_select(tree)
    if(command_type == "count"):
        return eval_count(tree)
    if(command_type == "delete"):
        return eval_delete(tree)
    
    raise Exception("Invalid command type")

def eval_count(tree):
    sql_text = "SELECT COUNT(*)"
    sql_text += " FROM " + get_source(tree) 
    sql_text += get_conditions(tree)
    return sql_text

def eval_delete(tree):
    sql_text = "DELETE"
    sql_text += " FROM " + get_source(tree) 
    sql_text += get_conditions(tree)
    return sql_text

def eval_select(tree):
    sql_text = "SELECT"

    #-------columns-------#
    columns = list(tree.find_data("selected_columns"))
    column_list = []
    if(len(columns) > 0):
        for column in columns[0].children:
            column_list.append(column)
        sql_text += " " + insert_separator(column_list,", ")
    else:
        sql_text += " *"

    #-------table source-------#
    sql_text += " FROM " + get_source(tree) 

    #-------conditions-------#
    sql_text += get_conditions(tree)

    #-------ordering-------#
    order = list(tree.find_data("order"))
    if(len(order) > 0):
        order_column = order[0].children[0]
        sql_text += " ORDER BY " + order_column + " "
        if(order[0].children[1] is None):
            sql_text += "desc"
        else:
            sql_text += order[0].children[1].data

    #row limit
    row_limit = list(tree.find_data("row_limit"))
    if(len(row_limit) > 0):
        sql_text += " LIMIT " + row_limit[0].children[0]

    return sql_text