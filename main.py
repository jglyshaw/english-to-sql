from lark import Lark
from sql_runner import run_code
from tree_parser import eval_tree

my_grammar = open("grammar.txt","r")
my_grammar = my_grammar.read()

request = input("give me a request: ")
#program = open("p1.txt","r").read()
program = request

parser = Lark(my_grammar)
parse_tree = parser.parse(program)
sql_text = eval_tree(parse_tree)


#print("english command:", program)
print("sql command:", sql_text)
run_code(sql_text)

