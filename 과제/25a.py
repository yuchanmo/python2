#정답 : dot 이 가장 해당 문제를 표현하는데 최적화되어있음. 계층관계를 표현하기 위한 문제
#dot : 계층관계를 표현하기 위한 그래프 엔진
#neato : spring model (서로의 관계에 대해 표현할때 유용, 방향성 있음)
#fdp : spring model(neato 와 비슷, 관계에 대해 표현, 방향성 없음)
#sfdp : spring model(fdp 보다 좀 더 크게 그린것, 방향성 없음)
#twopi : 방사형 그래프를 표현(신경망 같은거에 사용)
#circo : 싸이클 관계에 있는것을 표현

def func25a_1():
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

        a.render()

func25a_1()

#redbalck tree
def func25a_2():
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
    # g.node('6')

    # g.edge('13','8')
    # g.edge('13','17')

    # g.edge('8','1')
    # g.edge('8','11')

    # g.edge('1','6')

    # g.edge('17','15')
    # g.edge('17','25')

    # g.edge('25','22')
    # g.edge('25','27')

    # g.edge('1','n1')
    # g.edge('6','n2')
    # g.edge('6','n3')
    # g.edge('11','n4')
    # g.edge('11','n5')
    # g.edge('15','n6')
    # g.edge('15','n7')
    # g.edge('22','n8')
    # g.edge('22','n9')
    # g.edge('27','n10')
    # g.edge('27','n11')

    g.view()

func25a_2()