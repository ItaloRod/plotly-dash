import connection as conn
import pandas as pd

def getProfessionalsByBond():
    '''
        tras todos os profissionais pelo vinculo
        retorna:
            Pandas DataFrame
    '''
    df = conn.getProfessionalsCsv() # Carrega os dados
    df = df[df['cns'] != ''] # remove valores vazios
    df = df[df['cbodescricao'].str.match('MEDICO')] # Pega quem é médico 
    df = df.groupby(['cns']).count() # Agrupa por CNS e conta
    df['vinculos'] = df.cnes 
    df = df.groupby(['vinculos'], as_index = False).count() # Agrupa pelo Vínculo e conta, o Index=False nos permite ter acesso a coluna agrupada.    
    newdf = pd.DataFrame({
    'x': df['vinculos'],
    'y': df['nome']
    })
    return newdf