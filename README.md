# SwapiTest
Projeto de teste para acesso a <a href="https://swapi.dev/">API Swapi</a> com informações sobre <i>Star Wars</i>.

<h2>Como rodar o programa</h2>
Foi utilizado o <a href="https://pipenv-fork.readthedocs.io/en/latest/basics.html#example-pipfile-pipfile-lock">pipenv</a>, então basta clonar o repositório e executar pipenv install estando no diretório do projeto.

Depois de instalado, basta executar o programa utilizando o nome do arquivo para ter como retorno os valores básicos da API. Pode também ser passado o valor do recurso desejado e o Id também.
Exemplo: 'python SwapiConnection.py' ou 'python SwapiConnection.py planets' ou 'python SwapiConnection.py planets 1'.

Obs 1: Para saber os recursos disponíveis e mais informações sobre a API, acesse <a href = "https://swapi.dev/documentation">esse link</a>.
Obs 2: Passar somente valores inteiros positivos como Id para o programa.
