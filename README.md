# Master

# MEC_RNIS

---

Criar um ambiente virtual para desenvolver um projeto é crucial, pois proporciona isolamento de dependências, reprodutibilidade e consistência no ambiente de desenvolvimento. Isso evita conflitos entre diferentes versões de bibliotecas, facilita a colaboração em equipe, previne a poluição do sistema operacional com dependências desnecessárias, e oferece suporte para diferentes versões do Python. Além disso, a utilização de ambientes virtuais simplifica a manutenção do projeto, a execução de testes e a integração com ferramentas de desenvolvimento, contribuindo para um desenvolvimento mais eficiente e organizado.


# Ambiente virtual

  comando:

    sudo pip3 install virtualenv  --user 
 
  ou:

    sudo apt install python3-virtualenv


# Criando o ambiente:

  comando:

    virtualenv amb --python=python3.8

# Para acessar o ambiente use o comando:

  comando:
    
    source amb/bin/activate

# Para desativar o ambiente

  comando:
    
    deactivate

# Bibliotecas

  comando:

    pip3 install Flask

    pip3 install Flask-Restful

    pip3 install connexion

pip3 install pika

# Para criar um requirements e simples

  comando:

    pip3 freeze > requirements.txt

# Para instalar as dependências de um “requirements.txt” usamos o seguinte comando

  comando:

    pip3 install -r requirements.txt

