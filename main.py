from lark import Lark
from sql_runner import run_code
from tree_parser import eval_tree

#get the grammar
my_grammar = open("grammar.txt","r")
my_grammar = my_grammar.read()
parser = Lark(my_grammar)

while(True):
    #get user input
    request = input("give me a request, or press enter to quit: ")
    if(request == ""):
        break

    try:
        #get a tree from input and convert it into sql
        parse_tree = parser.parse(request)
        sql_text = eval_tree(parse_tree)

        #run the converted sql command
        print("sql command:", sql_text)
        run_code(sql_text)
    except Exception as e:
        print(e)
    
    
