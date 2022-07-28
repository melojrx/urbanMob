-- ################
-- #    SCHEMA    #
-- ################

CREATE SCHEMA cidade;

-- ################
-- #  SEQUENCES   #
-- ################

CREATE SEQUENCE cidade.usuario_seq
  INCREMENT 1
  MINVALUE 1
  MAXVALUE 9223372036854775807
  START 1
  CACHE 1;


CREATE SEQUENCE cidade.categoria_seq
  INCREMENT 1
  MINVALUE 1
  MAXVALUE 9223372036854775807
  START 1
  CACHE 1;

  CREATE SEQUENCE cidade.subcategoria_seq
  INCREMENT 1
  MINVALUE 1
  MAXVALUE 9223372036854775807
  START 1
  CACHE 1;

  
  CREATE SEQUENCE cidade.evento_seq
  INCREMENT 1
  MINVALUE 1
  MAXVALUE 9223372036854775807
  START 1
  CACHE 1;

  CREATE SEQUENCE cidade.evento_historico_seq
  INCREMENT 1
  MINVALUE 1
  MAXVALUE 9223372036854775807
  START 1
  CACHE 1;

  CREATE SEQUENCE cidade.status_evento_seq
  INCREMENT 1
  MINVALUE 1
  MAXVALUE 9223372036854775807
  START 1
  CACHE 1;

-- ################
-- #    TABLES    #
-- ################

CREATE TABLE cidade.tb_usuario_usu (
	id_usuario_usu integer NOT NULL DEFAULT nextval('cidade.usuario_seq'::regclass),
	txt_nome_usu varchar(200) NOT NULL,
	txt_email_usu varchar(200) NOT NULL,
	txt_password_usu varchar(128) NOT NULL,
	CONSTRAINT usuario_pkey PRIMARY KEY (id_usuario_usu)
);

CREATE TABLE cidade.tb_categoria_cat (
	id_categoria_cat integer NOT NULL DEFAULT nextval('cidade.categoria_seq'::regclass),
	txt_categoria_cat varchar(50) NOT NULL,
	dat_inicio_cat timestamp without time zone NOT NULL,
	dat_fim_cat timestamp without time zone,
	CONSTRAINT categoria_pkey PRIMARY KEY (id_categoria_cat)
);

CREATE TABLE cidade.tb_status_evento_sev (
	id_status_evento_sev integer NOT NULL DEFAULT nextval('cidade.status_evento_seq'::regclass),
	txt_status_evento_sev varchar(50) NOT NULL,
	dat_inicio_sev timestamp without time zone NOT NULL,
	dat_fim_sev timestamp without time zone,
	CONSTRAINT status_evento_pkey PRIMARY KEY (id_status_evento_sev)
);

CREATE TABLE cidade.tb_subcategoria_sub (
	id_subcategoria_sub integer NOT NULL DEFAULT nextval('cidade.subcategoria_seq'::regclass),
  id_categoria_sub integer NOT NULL,
	txt_subcategoria_sub varchar(50) NOT NULL,
	dat_inicio_sub timestamp without time zone NOT NULL,
	dat_fim_sub timestamp without time zone,
	CONSTRAINT subcategoria_pkey PRIMARY KEY (id_subcategoria_sub)
);
ALTER TABLE cidade.tb_subcategoria_sub ADD CONSTRAINT categoria_fkey FOREIGN KEY (id_categoria_sub) REFERENCES cidade.tb_categoria_cat (id_categoria_cat);

CREATE TABLE cidade.tb_evento_eve (
	id_evento_eve integer NOT NULL DEFAULT nextval('cidade.evento_seq'::regclass),
  id_subcategoria_eve integer NOT NULL,
	txt_problema_eve varchar(1000) NOT NULL,
	dat_inicio_eve timestamp without time zone NOT null default now(),
	dat_fim_eve timestamp without time zone default null,
	CONSTRAINT evento_pkey PRIMARY KEY (id_evento_eve)
);
ALTER TABLE cidade.tb_evento_eve ADD CONSTRAINT subcategoria_fkey FOREIGN KEY (id_subcategoria_eve) REFERENCES cidade.tb_subcategoria_sub (id_subcategoria_sub);

CREATE TABLE cidade.tb_evento_historico_ehi (
	id_evento_historico_ehi integer NOT NULL DEFAULT nextval('cidade.evento_historico_seq'::regclass),
  id_evento_ehi integer NOT NULL,
	id_status_evento_ehi integer NOT NULL,
	dat_inicio_ehi timestamp without time zone NOT null default now(),
	dat_fim_eehi timestamp without time zone default null,
	CONSTRAINT evento_historico_pkey PRIMARY KEY (id_evento_historico_ehi)
);
ALTER TABLE cidade.tb_evento_historico_ehi ADD CONSTRAINT evento_fkey FOREIGN KEY (id_evento_ehi) REFERENCES cidade.tb_evento_eve (id_evento_eve);
ALTER TABLE cidade.tb_evento_historico_ehi ADD CONSTRAINT status_fkey FOREIGN KEY (id_status_evento_ehi) REFERENCES cidade.tb_status_evento_sev (id_status_evento_sev);

-- ####################################
-- #        INSERTS PARA TESTES       #
-- ####################################

INSERT INTO cidade.tb_categoria_cat(txt_categoria_cat, dat_inicio_cat, dat_fim_cat)VALUES('Urbanismo', now(), null);
INSERT INTO cidade.tb_categoria_cat(txt_categoria_cat, dat_inicio_cat, dat_fim_cat)VALUES('Paisagismo', now(), null);

INSERT INTO cidade.tb_subcategoria_sub(id_categoria_sub, txt_subcategoria_sub, dat_inicio_sub, dat_fim_sub)VALUES(1, 'Buraco', now(), null);
INSERT INTO cidade.tb_subcategoria_sub(id_categoria_sub, txt_subcategoria_sub, dat_inicio_sub, dat_fim_sub)VALUES(1, 'Calçada Irregular', 'now()', null);

INSERT INTO cidade.tb_subcategoria_sub(id_categoria_sub, txt_subcategoria_sub, dat_inicio_sub, dat_fim_sub)VALUES(2, 'Pixações', now(), null);
INSERT INTO cidade.tb_subcategoria_sub(id_categoria_sub, txt_subcategoria_sub, dat_inicio_sub, dat_fim_sub)VALUES(2, 'Placas de Publicidade', 'now()', null);

INSERT INTO cidade.tb_status_evento_sev (txt_status_evento_sev, dat_inicio_sev, dat_fim_sev) VALUES('Status 1', now(), null);
INSERT INTO cidade.tb_status_evento_sev (txt_status_evento_sev, dat_inicio_sev, dat_fim_sev) VALUES('Status 2', now(), null);
