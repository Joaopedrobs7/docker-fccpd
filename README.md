# Docker FCCPD
Este projeto é um sistema de gerenciamento que implementa operações CRUD para itens, serviços e funcionários de uma marcenaria, desenvolvido com o objetivo de aprender a orquestrar serviços usando Docker Compose.

![Docker](https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white)
![MySql](https://img.shields.io/badge/MySQL-005C84?style=for-the-badge&logo=mysql&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

## Instalação
Baixe o Docker em sua máquina [Docker desktop](https://www.docker.com/products/docker-desktop/).

Baixe a imagem do Python e do Mysql:
```bash
docker pull python
```
```bash
docker pull mysql
```

Clone o repositório em sua máquina:

```bash
https://github.com/Joaopedrobs7/docker-fccpd.git
```

## Executando
Abra 2 Terminais, um para o Mysql e o outro para o Python

#### Inicie o docker em segundo plano:
```bash
docker-compose up -d mysql
```

#### Inicie o Python em modo interativo:
```bash
docker-compose run pythonapp
```

------------------
Executar apenas Container SQL:
```bash
docker exec -it docker-fccpd-mysql-1 mysql -uroot -proot
```

