from graphviz import Digraph

layout_engine = ['dot','neato','fdp','sfdp','twopi','circo']
for i in layout_engine:
    f = 'gviz/7th Edition'+i
    a = Digraph(filename = f,comment='7th Edition',engine=i)
    a.node_attr.update(color='goldenrod2',style='filled',size='7,5')

    a.edge('7th Edition','32V')
    a.edge('7th Edition','V7M')
    a.edge('7th Edition','Xenix')
    a.edge('7th Edition','UniPlus+')

    a.edge('32V','3 BSD')
    a.edge('3 BSD','4 BSD')
    a.edge('4 BSD','4.1 BSD')

    a.edge('4.1 BSD','8th Edition')
    a.edge('8th Edition','9th Edition')

    a.edge('4.1 BSD','4.2 BSD')
    a.edge('4.2 BSD','Ultrix-32')
    a.edge('4.2 BSD','4.3 BSD')

    a.edge('4.1 BSD','2.8 BSD')
    a.edge('1 BSD','2 BSD')
    a.edge('2 BSD','2.8 BSD')
    a.edge('2.8 BSD','2.9 BSD')
    a.edge('2.8 BSD','Ultrix-11')

    a.render(view=True)


