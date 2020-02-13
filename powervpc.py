#
#
# main() será executado quando você chamar essa ação
#
# @param As ações do Cloud Functions aceitam um único parâmetro, que deve ser um objeto JSON.
#
# @return A saída dessa ação, que deve ser um objeto JSON.
#
#
import sys
import requests
def main(dict):


    headers = {
        'Authorization': dict['token']
    }
    
    params = (
        ('version', '2020-01-28'),
        ('generation', dict['generation'])
    )
    
    data = '{"type": "'+dict['action']+'"}'
    url = 'https://'+dict['region']+'.iaas.cloud.ibm.com/v1/instances/'dict['instance_id']'/actions'
    response = requests.post(url, headers=headers, params=params, data=data)
    return { 'message': 'Hello world' }
