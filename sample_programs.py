from lark import Lark
from tree_parser import eval_tree

#get the grammar
my_grammar = open("grammar.txt","r")
my_grammar = my_grammar.read()
parser = Lark(my_grammar)

programs = []

#program 1
english = "give me rows from the people table where age is more than 10 and name is mark ordered by height ascending"
expected = "SELECT * FROM people WHERE age > 10 and name = 'mark' ORDER BY height asc"
programs.append([english, expected])

#program 2
english = "when score is 15 i want items from players with columns username and score"
expected = "SELECT username, score FROM players WHERE score = 15"
programs.append([english, expected])

#program 3
english = "delete entries from table music when length is 15 and also cost is less than 20"
expected = "DELETE FROM music WHERE length = 15 and cost < 20"
programs.append([english, expected])

#program 4
english = "how many rows are in people when age is 24 and name is Tom"
expected = "SELECT COUNT(*) FROM people WHERE age = 24 and name = 'Tom'"
programs.append([english, expected])

#program 5
english = "with columns lives and score i want 20 items from players when lives is greater than 3 order by score"
expected = "SELECT lives, score FROM players WHERE lives > 3 ORDER BY score desc LIMIT 20"
programs.append([english, expected])

#program 6
english = "give me 3 items from the states table"
expected = "SELECT * FROM states LIMIT 3"
programs.append([english, expected])

for index, [program,expected] in enumerate(programs):
    parse_tree = parser.parse(program)
    sql_text = eval_tree(parse_tree)
    print("-----------------Program " + str(index+1) + "-----------------")
    print("English statement:", program)
    print("SQL statement:", sql_text, "\n")
    if(sql_text != expected):
        raise Exception("Translated SQL statement does not equal expected value")


   