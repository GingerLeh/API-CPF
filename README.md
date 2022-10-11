# API Muda-CPF
Api onde o usuário insere um CPF qualquer no formato XXXXXXXXXXX e a Api retorna no formato XXX.XXX.XXX-XX.
A Api também verifica se o CPF digitado é válido ou não, caso não seja, retorna uma mensagem de 'CPF inválido'. 

## Getting Started

Para executar a aplicação, basta compilar o Docker e executar o mesmo com os seguintes comandos

```
docker-compose build
docker-compose up
```

Instruções adicionais podem ser encontrados na [Apresentação Swagger](https://github.ibm.com/patrick-ibm/swagger_api/blob/master/Apresenta%C3%A7%C3%A3o%20Swagger.pdf) no repositório

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Autores

* **Patrick Luiz** - *Trabalho inicial*
*  **Alessa B Santos** - *Modificação* 

## Exemplo de template copiado de: https://gist.github.com/PurpleBooth/109311bb0361f32d87a2