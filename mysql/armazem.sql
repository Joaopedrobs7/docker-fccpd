use db;


create table armazem(
    ItemID int not null AUTO_INCREMENT,
    Item varchar(100) NOT NULL,
    estoque int not null,
    PRIMARY KEY (ItemID)
);

create table funcionarios(
    ID int not null AUTO_INCREMENT,
    nome varchar(100) NOT NULL,
    trabalhando ENUM('0', '1') NOT NULL,
    PRIMARY KEY (ID)
);

create table servicos(
    ID int not null AUTO_INCREMENT,
    cliente varchar(100) NOT NULL,
    descricao varchar(100) NOT NULL,
    nome varchar(100) NOT NULL,
    PRIMARY KEY (ID)
);

INSERT INTO  armazem(Item,estoque)
VALUES("Martelo",5),("Madeira tipo A",10),("Madeira tipo B",15);

INSERT INTO  funcionarios(nome,trabalhando)
VALUES("joao",'1'),("carlos",'0'),("mathews",'1');

INSERT INTO  servicos(cliente,descricao,nome)
VALUES("Pedro","Contrucao piscina","mathews"),("Marcia","Mesa madeira tipo A com Verniz","joao");

