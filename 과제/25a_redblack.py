from graphviz import Digraph

g = Digraph(comment = 'Red-Black Tree',engine='dot')

g.attr('graph',ratio='.48')

g.attr('node',style='filled',color='black',shape='circle',width='.6',
        fontname='Helvetica',fontweight='bold',fontcolor='white',fontsize='24',fixedsize='true')

ns = ['13','1','11','15','25']
for i in ns:
    g.node(i)

g.attr('node',fillcolor='red')
ns2 = ['8','17','22','27']
for j in ns2:
    g.node(j)

g.attr('node',fillcolor='black',shape='record',label='NIL',width='0.4',height='.25',fontsize='16')
for i in range(1,12):
    la = 'n'+str(i)
    g.node(la)

g.attr('node',style='filled', fillcolor='red',shape='circle',label=r'\N',width='0.6',fontname='Helvetica'
       ,fontweight='bold',fontcolor='white',fontsize='24',fixedsize='true')
g.node('6')

relations = [('13','8'),('13','17'),('8','1'),('8','11')
,('1','n1'),('1','6'),('6','n2'),('6','n3'),('11','n4'),('11','n5')
,('17','15'),('15','n6'),('15','n7'),('17','25'),('25','27')
,('25','22'),('22','n8'),('22','n9'),('27','n10'),('27','n11')]

for r in relations:
    g.edge(r[0],r[1])
g.node('6')

g.edge('13','8')
g.edge('13','17')

g.edge('8','1')
g.edge('8','11')

g.edge('1','6')

g.edge('17','15')
g.edge('17','25')

g.edge('25','22')
g.edge('25','27')

g.edge('1','n1')
g.edge('6','n2')
g.edge('6','n3')
g.edge('11','n4')
g.edge('11','n5')
g.edge('15','n6')
g.edge('15','n7')
g.edge('22','n8')
g.edge('22','n9')
g.edge('27','n10')
g.edge('27','n11')

g.view()
