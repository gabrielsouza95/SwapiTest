# SwapiTest
<p>Projeto de teste para acesso a <a href="https://swapi.dev/">API Swapi</a> com informações sobre <i>Star Wars</i>.</p>

<h2>Como rodar o programa</h2>
<p>Foi utilizado o <a href="https://pipenv-fork.readthedocs.io/en/latest/basics.html#example-pipfile-pipfile-lock">pipenv</a>, então basta clonar o repositório e executar pipenv install estando no diretório do projeto.</p>

<p>Depois de instalado, basta executar o programa utilizando o nome do arquivo para ter como retorno os valores básicos da API. Pode também ser passado o valor do recurso desejado e o Id também.</p>
<p>Exemplo: 'python SwapiConnection.py' ou 'python SwapiConnection.py planets' ou 'python SwapiConnection.py planets 1'.</p>
<p>Imagem a seguir mostra o retorno de uma execução simples do programa sem parâmetros.</p>
<span><img style="max-width:50%; max-height:50%;" src="https://github.com/gabrielsouza95/SwapiTest/blob/main/teste_simples.PNG" alt="imagem_teste_programa">
</span>

<p>Também é possível obter o resultado traduzido para Wookiee, para isso precisa passar o recurso e Id do objeto desejado e mais 'wookiee'.</p>
<p>Exemplo: 'python SwapiConnection.py planets 1 wookiee'.</p>

<p>Obs 1: Para saber os recursos disponíveis e mais informações sobre a API, acesse <a href = "https://swapi.dev/documentation">esse link</a>.</p>
<p>Obs 2: Passar somente valores inteiros positivos como Id para o programa.</p>
