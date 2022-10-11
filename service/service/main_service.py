from distutils.log import ERROR
import time
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
            if self.verificaCPF(text) == True: 
                if x in [3,6]:
                    resp_vec.append('.')
                elif x==9: 
                    resp_vec.append('-')
                resp_vec.append(text[x])
            else:
                return mensagens.ERROR_CPF
        return ''.join(resp_vec)

    def verificaCPF(self,text):
        
        cpf = [int(x) for x in text]

        if len(cpf) != 11:
            return False

        if cpf == cpf[::-1]:
            return False

        for i in range(9, 11):
            value = sum((cpf[num] * ((i+1) - num) for num in range(0, i)))
            digit = ((value * 10) % 11) % 10
            if digit != cpf[i]:
                return False
        return True