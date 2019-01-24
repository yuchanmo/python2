from graphviz import Digraph

g = Digraph('g',filename='gviz/bte2.gv',node_attr={'shape':'record'})
g.node('node0','<f0> |<f1> A|<f2> |<f3> ')
g.node('node1','<f0> |<f1> B|<f2> |<f3> ')
g.node('node2','<f0> |<f1> C|<f2> |<f3> ')



g.view()

