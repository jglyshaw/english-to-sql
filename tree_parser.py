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

def eval_tree(t):
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
    source = list(t.find_data("source"))
    source = source[0].children[0]
    sql_text += " FROM " + source 

    #-------conditions-------#
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
        sql_text += " WHERE " + insert_separator(condition_list," and ")

    #-------ordering-------#
    order = list(t.find_data("order"))
    if(len(order) > 0):
        order_column = order[0].children[0]
        sql_text += " ORDER BY " + order_column + " "
        if(order[0].children[1] == None):
            sql_text += "desc"
        else:
            sql_text += order[0].children[1].data
        
    return sql_text