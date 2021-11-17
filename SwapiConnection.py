# Esse códiogo visa responder a questão 3
# Gabriel de Souza Alves

class SwapiConection:
    import requests

    def __init__(self):
        self.conected = False

    def get_request(self, p_resource = None, p_id = None):
        self.url = self.build_url(p_resource, p_id)
        self.response = self.requests.get(self.url)
        print(self.response.json())

    def build_url(self, p_resource, p_id):
        self.base_api_url = 'http://swapi.dev/api'
        self.result_url = self.base_api_url

        if p_resource != None : #separa o tipo de recurso a ser procurado, como"films", "people","planets","species","starships"e"vehicles"
            self.result_url += f'/{p_resource}/'

        if p_id != None :
            self.result_url += f'/{p_id}/'

        return self.result_url 


def main():
    import sys

    conection = SwapiConection()
    if len(sys.argv) == 1:
        conection.get_request()
        return
    if len(sys.argv) == 2:
        resource_value = sys.argv[1]
        conection.get_request(resource_value)
        return    
    if len(sys.argv) == 3:
        resource_value = sys.argv[1]
        id_value = sys.argv[2]
        try:
            id_value_int = int(id_value)
        except ValueError as e:
            print("Entre com um valor inteiro positivo como argumento do Id.")
            return
        conection.get_request(resource_value, id_value_int)
        return 

    print("Execute o programa como no exemplo: 'python SwapiConnection.py' ou adicione o recurso ou até mesmo o Id do recurso. Para mais informações sobre recursos e Ids, acesse https://swapi.dev/")

if __name__ == "__main__": 
    main()        