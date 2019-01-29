#%%
from graphviz import Digraph, Graph, render
from pydot import Subgraph

dot = Digraph(comment = 'The Round Table')

dot.node('a',label='aa')
dot.node('b',label='bb')
dot.edges(['ab','ba'])
dot.render('test.gv')

ps = Digraph(name='pet-shop',node_attr={'shape':'plaintext'})
ps.node('parrot')
ps.node('dead')
ps.edge('parrot','dead')

ps.graph_attr['rankdir'] = 'LR'
ps.edge_attr.update(arrowhead='vee',arrowsize='2')
ps.render('pet-shop')


p = Graph(name='parent')
p.edge('spam','eggs')

c = Graph(name='child',node_attr={'shape':'box'})
c.edge('foo','bar')
p.subgraph(c)
p.render('subgraph')