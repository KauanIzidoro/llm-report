from graphviz import Digraph


dot = Digraph(comment="Exemplo de Grafo")
dot.node('A', 'Etapa 1')
dot.node('B', 'Etapa 2')
dot.node('C', 'Etapa 3')
dot.edge('A', 'B', 'Transição')
dot.edge('B', 'C', 'Concluir')
dot.render('diagrama_teste', format='png', cleanup=True)  

