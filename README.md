# Super Portfólio

## Contexto

> Neste projeto foi criada uma API e um banco de dados para um site de portfólios. A aplicação permite fazer o CRUD (Create, Read, Updated e Delete) para criar, ler, atualizar e deletar um perfil, um projeto, um certificado e um instituição certificadora utilizando o DRF(Django Rest Framework).

## Tecnologias usadas

- Django;
- DRF (Django Rest Framework);
- MySQL;
- Docker;
- JWT.

## Instalação do projeto

<details>
  <summary><strong>Dependências Necessárias</strong></summary><br />
1. Este projeto usa dependências que não são funcionais em todas as versões do Python. Por isso, recomendamos que seu Python esteja na versão `3.10.0` ou superior. Você pode usar o `Pyenv`, basta seguir nosso tutorial sobre [instalação e uso do Pyenv](https://app.betrybe.com/learn/course/5e938f69-6e32-43b3-9685-c936530fd326/module/f04cdb21-382e-4588-8950-3b1a29afd2dd/section/aa76abc8-b842-40d9-b5cc-baa960952129/lesson/0fe67ea0-1046-4b55-a37c-44afcfa9ed0a).
  
> ⚠️ **ATENÇÃO: NUNCA REMOVA VERSÕES ANTIGAS INSTALADAS DO PYTHON. SEU SISTEMA OPERACIONAL PODE DEPENDER DELAS!** ⚠️

2. Para conseguir instalar a dependência `mysqlclient` você precisa garantir a existência de algumas bibliotecas no seu sistema operacional:

- **Debian/Ubuntu**
```bash
sudo apt-get install python3-dev default-libmysqlclient-dev build-essential pkg-config
```

- **Mac**
```bash
brew install mysql pkg-config
```
</details>


1. Primeiro abra o terminal e crie um diretório com o comando <strong>mkdir</strong>:
``` 
 mkdir projetos
```

2. Entre no diretório que acabou de criar e clone o projeto:
``` 
cd projetos
git clone git@github.com:tryber/python-028-python-projeto-super-portfolio.git
```

3. Crie o ambiente virtual

```bash
python3 -m venv .venv
```

4. Ative o ambiente virtual

```bash
source .venv/bin/activate
```

5. Instale as dependências no ambiente virtual

```bash
python3 -m pip install -r dev-requirements.txt
```

6. Para rodar o MySQL via Docker execute os seguintes comandos na raiz do projeto:

  ```bash
docker build -t super-portfolio-db .
docker run -d -p 3306:3306 --name=super-portfolio-mysql-container -e MYSQL_ROOT_PASSWORD=password -e MYSQL_DATABASE=super_portfolio_database super-portfolio-db
  ```

7. Entre no diretório do projeto e rode o serviço com o comando:

    ```bash
    python3 manage.py runserver
    ```
    
8. Crie as migrações:
   
    ```bash
    python3 manage.py makemigrations
    ```

   
