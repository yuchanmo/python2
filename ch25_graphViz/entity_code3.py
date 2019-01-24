from graphviz import Graph


g = Graph(filename='gviz/entity.gv',engine='neato')

g.attr('node',shape='box')
g.node('course')
g.node('institute')
g.node('student')

g.attr('node',shape='ellipse')
g.node('name0',label='name')
g.node('name1',label='name')
g.node('name2',label='name')
g.node('code')
g.node('grade')
g.node('number')

g.attr('node',shape='diamond',style='filled',color='lightgrey')
g.node('c-i')
g.node('s-c')
g.node('s-i')

g.edge('name0','course')
g.edge('code','course')
g.edge('course','c-i',label='n',len='1.00')
g.edge('institute','name1')
g.edge('institute','s-i',label='1',len='1.00')
g.edge('s-i','student',label='n',len='1.00')
g.edge('student','grade')
g.edge('student','name2')
g.edge('student','number')
g.edge('student','s-c',label='m',len='1.00')
g.edge('s-c','course',label='n',len='1.00')

g.view()

