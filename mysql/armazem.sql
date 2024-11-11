CREATE DATABASE IF NOT EXISTS db;
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
    FuncionarioID int,
    ItemID int,
    PRIMARY KEY (ID),
    FOREIGN KEY (ItemID) REFERENCES armazem(ItemID),
    FOREIGN KEY (FuncionarioID) REFERENCES funcionarios(ID)
);

INSERT INTO  armazem(Item,estoque)
VALUES("Madeira Tipo A",5),("Madeira tipo B",10),("Madeira tipo C",15),
("Tinta Tipo A",4),("Tinta Tipo B",10),("Ceramica Tipo C",20);

INSERT INTO  funcionarios(nome,trabalhando)
VALUES("joao",'1'),("carlos",'1'),("mathews",'1'),
("fallen",'1'),("coldzera",'1'),("fnx",'1');

INSERT INTO  servicos(cliente,descricao,FuncionarioID,ItemID)
VALUES("Pedro","Pintura Parede 4 metros",1,4),("Marcia","Mesa madeira tipo A com Verniz",2,1),
("josefino","Cadeira rustica madeira Tipo B",3,2),("lira","Porta 2 metros madeira tipo C",4,3),
("adriano","Reforma guarda roupa C/madeira A",5,1),("gabriel","Montagem palco 5x5 madeira tipo B",6,2);

