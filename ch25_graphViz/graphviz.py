

import graphviz as g
import random 



dot = g.Digraph(comment= 'The Round Table')


dot.node('A','King arthur')
dot.node('B','Sir Bedevere the Wise')
dot.node('L','Sir Lancelot the Brave')
dot.node('S','FA Team')
dot.edges(['AB','AL'])
dot.edge('B','L',constraint = 'false')
print(dot.source)


dot.render('c:/test-output/round-table.gv',view=True)


import graphviz as gv

d = gv.Digraph()
d.edge('hello','world')



import graphviz as g
dot = g.Graph(comment= 'The Round Table')


dot.node('A','King arthur')
dot.node('B','Sir Bedevere the Wise')
dot.node('L','Sir Lancelot the Brave')
dot.node('S','FA Team')
dot.edges(['AB','AL'])
dot.edges(['AS','BS'])
dot.edge('B','L',constraint = 'false')
print(dot.source)

dot.render('test-output/undirected.gv',view=True)



import graphviz as g
dot = g.Graph(comment= 'The Round Table')
with open('people.txt','r') as f:
    from functools import reduce
    for line in f:
        d = line.split(',')
        n,de = d[0],' '.join(d[1:])
        dot.node(n,de)
dot.render('test-output/undirected.gv',view=True)



import graphviz as g

ps = g.Digraph(name='pet-shop',node_attr={'shape' : 'plaintext'})
ps.node('parrot')
ps.node('dead')
ps.edge('parrot','dead')

ps.graph_attr['rankdir'] = 'BT'
ps.edge_attr.update(arrowhead='vee',arrowsize='2')
print(ps.source)
ps.render('test_output/pet-shop',view=True)



ni = Graph('ni')
ni.attr('node',shape = 'rarrow')

from graphviz import Graph,Digraph
dot = Digraph()
# dot.attr('node',shape = 'rarrow')
with open('people.txt','r') as f:    
    for line in f:
        d = line.split(',')
        n,de = d[0],' '.join(d[1:])
        dot.node(n,de)


with open('relation.txt','r') as ff:
    for line in ff:
        dot.edges(line.split(','))

dot.render('test-output/undirected.gv',view=True)


p = Graph(name = 'parent')
p.edge('spam','eggs')
c = Graph(name = 'child',node_attr={'shape':'box'})
c.edge('foo','bar')
p.subgraph(c)

p.render('test_out/parent',view=True)





import graphviz as g
import random 



dot = g.Digraph(comment= 'The Round Table',engine='circo')


dot.node('A','King arthur')
dot.node('B','Sir Bedevere the Wise')
dot.node('L','Sir Lancelot the Brave')
# dot.node('S','FA Team')
dot.edges(['AB','AL'])
dot.edge('B','L',constraint = 'false')
print(dot.source)


dot.render('c:/test-output/circo-table.gv',view=True)
