from graphviz import Digraph

der = Digraph('Diagrama Entidade-Relacionamento', node_attr={'shape': 'plaintext'})

der.node('Cliente', '''<
    <table border="1" cellborder="1" cellspacing="0">
        <tr><td bgcolor="lightblue"><b>Cliente</b></td></tr>
        <tr><td>ID_Cliente</td></tr>
        <tr><td>Nome</td></tr>
        <tr><td>Email</td></tr>
    </table>
>''')

der.node('Pedido', '''<
    <table border="1" cellborder="1" cellspacing="0">
        <tr><td bgcolor="lightblue"><b>Pedido</b></td></tr>
        <tr><td>ID_Pedido</td></tr>
        <tr><td>Data</td></tr>
        <tr><td>Valor</td></tr>
    </table>
>''')

der.node('Produto', '''<
    <table border="1" cellborder="1" cellspacing="0">
        <tr><td bgcolor="lightblue"><b>Produto</b></td></tr>
        <tr><td>ID_Produto</td></tr>
        <tr><td>Nome</td></tr>
        <tr><td>Preço</td></tr>
    </table>
>''')

der.node('Estoque', '''<
         <table border="1" cellborder="1" cellspacing="0">
            <tr><td bgcolor="lightblue"><b>Estoque</b></td></tr>
            <tr><td>ID_Produto</td></tr>
            <tr><td>Nome</td></tr>
            <tr><td>Preço</td></tr>
            <tr><td>Hora</td></tr>
         </table>
         >''')

der.node('Faz', '''<
    <table border="1" cellborder="1" cellspacing="0">
        <tr><td bgcolor="lightgrey"><b>Faz</b></td></tr>
    </table>
>''', shape='none')
der.node('Contém', '''<
    <table border="1" cellborder="1" cellspacing="0">
        <tr><td bgcolor="lightgrey"><b>Contém</b></td></tr>
    </table>
>''', shape='none')

der.edge('Cliente', 'Faz', label='1', arrowhead='none')
der.edge('Faz', 'Pedido', label='N', arrowhead='none')
der.edge('Pedido', 'Contém', label='1', arrowhead='none')
der.edge('Contém', 'Produto', label='N', arrowhead='none')
der.render('resultados/der_tabelas', format='png', cleanup=True)