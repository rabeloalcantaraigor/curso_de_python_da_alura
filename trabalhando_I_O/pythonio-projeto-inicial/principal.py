import contatos_utils

try:
    # contatos = contatos_utils.csv_para_contatos('curso_de_python/trabalhando_I_O/pythonio-projeto-inicial/dados/contatos.csv')
    
    # contatos_utils.contatos_para_pickle(contatos, 'curso_de_python/trabalhando_I_O/pythonio-projeto-inicial/dados/contatos.pickle')
    
    # contatos = contatos_utils.pickle_para_contatos('curso_de_python/trabalhando_I_O/pythonio-projeto-inicial/dados/contatos.pickle')
    
    # contatos_utils.contatos_para_json(contatos, 'curso_de_python/trabalhando_I_O/pythonio-projeto-inicial/dados/contatos.json')
    
    contatos = contatos_utils.json_para_contatos('curso_de_python/trabalhando_I_O/pythonio-projeto-inicial/dados/contatos.json')
    
    for contato in contatos:
        print(f'{contato.id} - {contato.nome} - {contato.email}')
        
except FileNotFoundError:
    print('Arquivo não encontrado.')

except PermissionError:
    print('Sem permissão de escrita.')