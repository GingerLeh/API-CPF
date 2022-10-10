import time
import re
import json
from loguru import logger
from service.constants import mensagens
import pandas as pd

    
class mudaCPF():

    def __init__(self):
        logger.debug(mensagens.INICIO_LOAD_SERVICO)
        self.load_model()

    def load_model(self):
        """"
        Formata CPF para o padrao XXX.XXX.XXX-XX
        """

        logger.debug(mensagens.FIM_LOAD_SERVICO)

    def executar_rest(self, texts):
        response = {}

        logger.debug(mensagens.INICIO_SERVICO)
        start_time = time.time()
    
        response_text = [self.alteracao(text) for text in texts['textoMensagem']]

        logger.debug(mensagens.FIM_SERVICO)
        logger.debug(f"Fim da alteração em {time.time()-start_time}")

        df_response = pd.DataFrame(texts, columns=['textoMensagem'])
        df_response['predict'] = response_text

        df_response = df_response.drop(columns=['textoMensagem'])

        response = {
                     "listaCPF": json.loads(df_response.to_json(
                                                                            orient='records', force_ascii=False))}

        return response

    def alteracao(self,text):
        resp_vec = []
        for x in range(len(text)):
            if x in [3,6]:
                resp_vec.append('.')
            elif x==9: 
                resp_vec.append('-')
            resp_vec.append(text[x])
        return ''.join(resp_vec)
