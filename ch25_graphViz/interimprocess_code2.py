from graphviz import Digraph

f =Digraph('finite state machine',filename ='gviz/fsm.gv')
f.attr(rankdir='LR',size='8,5')

f.attr('node',shape='doublecircle')
f.node('LR_0')
f.node('LR_3')
f.node('LR_4')
f.node('LR_8')

f.attr('node',shape='circle')
f.edge('LR_0','LR_2',label='SS(B)')
f.edge('LR_0','LR_1',label='SS(S)')
f.edge('LR_1','LR_3',label='S($end))')
f.edge('LR_2','LR_6',label='SS(b)')
f.edge('LR_2','LR_5',label='SS(a)')
f.edge('LR_2','LR_4',label='S(A)')
f.edge('LR_5','LR_7',label='S(b)')
f.edge('LR_0','LR_2',label='S(a)')
f.edge('LR_0','LR_2',label='S(b)')

f.

f.view()
