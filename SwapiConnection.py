# Esse códiogo visa responder a questão 3
# Gabriel de Souza Alves

class SwapiConection:
    import requests
    import json

    def __init__(self):
        self.conected = False

    def get_request(self, p_resource = None, p_id = None, p_wookiee = None):
        self.url = self.build_url(p_resource, p_id)
        self.payload = {'format': p_wookiee}
        self.response = self.requests.get(self.url, params=self.payload)
        return self.response.text

    def build_url(self, p_resource, p_id):
        self.base_api_url = 'http://swapi.dev/api'
        self.result_url = self.base_api_url

        if p_resource != None : #separa o tipo de recurso a ser procurado, como"films", "people","planets","species","starships"e"vehicles"
            self.result_url += f'/{p_resource}/'

        if p_id != None :
            self.result_url += f'/{p_id}/'

        return self.result_url 

    def read_result(self, p_result):
        self.result_dict = self.json.loads(p_result)
        for key in self.result_dict:
            print(f'{key} - {self.result_dict[key]}')


def main():
    import sys

    conection = SwapiConection()
    result_conection = None

    if len(sys.argv) == 1:
        result_conection = conection.get_request()
    elif len(sys.argv) == 2:
        resource_value = sys.argv[1]
        result_conection = conection.get_request(resource_value)    
    elif len(sys.argv) == 3 or len(sys.argv) == 4:
        resource_value = sys.argv[1]
        id_value = sys.argv[2]
        try:
            id_value_int = int(id_value)
        except ValueError as e:
            print("Entre com um valor inteiro positivo como argumento do Id.")
        if len(sys.argv) == 4:
            wookiee_value = sys.argv[3]
        else :
            wookiee_value = None
        result_conection = conection.get_request(resource_value, id_value_int, wookiee_value) 
    else :
        print("Execute o programa como no exemplo: 'python SwapiConnection.py' ou adicione o recurso ou até mesmo o Id do recurso. Para mais informações sobre recursos e Ids, acesse https://swapi.dev/")

    conection.read_result(result_conection)

if __name__ == "__main__": 
    main()        