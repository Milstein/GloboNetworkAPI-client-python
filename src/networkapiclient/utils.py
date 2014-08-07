# -*- coding:utf-8 -*-
'''
Title: Infrastructure NetworkAPI
Author: globo.com / TQI
Copyright: ( c )  2009 globo.com todos os direitos reservados.
'''

import re
from Config import IP_VERSION

def is_valid_int_param(param):
    '''Verifica se o parâmetro é um valor inteiro válido.
    
    :param param: Valor para ser validado.
    
    :return: True se o parâmetro tem um valor inteiro válido, ou False, caso contrário.  
    '''
    if param is None:
        return False
    try:
        param = int(param)
        if param < 0:
            return False
    except (TypeError, ValueError):
        return False
    return True

def is_valid_ip(address):
    """Verifica se address é um endereço ip válido.
    
    O valor é considerado válido se tiver no formato XXX.XXX.XXX.XXX, onde X é um valor entre 0 e 9.
    
    :param address: Endereço IP.
    
    :return: True se o parâmetro é um IP válido, ou False, caso contrário.
    """
    if address is None:
        return False
    pattern = r"\b(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b"
    return re.match(pattern, address)

def is_valid_0_1(param):
    """
    Checks if param is zero or one
    """
    return param == "0" or param == "1" or param == 0 or param == 1

def get_list_map(map, key):
    """Se o mapa é diferente de None então retorna o mapa, caso contrário, cria o mapa {key:[]}.
    
    O mapa criado terá o elemento 'key' com uma lista vazia.
        
    :param map: Mapa onde o elemento tem como valor uma lista.
    :param key: Chave para criar o mapa {key:[]}
    
    :return: Retorna um mapa onde o elemento tem como valor uma lista.   
    """
    if map is None:
        return {key:[]}
    else:
        return map
    
def is_valid_version_ip(param):
    '''Checks if the parameter is a valid ip version value.
    
    :param param: Value to be validated.
    
    :return: True if the parameter has a valid ip version value, or False otherwise.  
    '''
    if param is None:
        return False

    if param == IP_VERSION.IPv4[0] or param == IP_VERSION.IPv6[0]:
        return True

    return False