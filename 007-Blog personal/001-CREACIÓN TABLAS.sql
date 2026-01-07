/*CREACION TABLA*/

CREATE TABLE "ENTRADAS" (
	"titulo"	TEXT,
	"fecha"	TEXT,
	"autor"	TEXT,
	"contenido"	TEXT,
	"imagen"	TEXT,
	"id"	INTEGER,
	PRIMARY KEY("id")
);

/*POBLAMOS LA TABLA*/

INSERT INTO ENTRADAS (titulo, fecha, autor, contenido, imagen)
VALUES (
    'Bienvenido a mi blog',
    '2026-01-01',
    'Héctor',
    'Este blog lo he creado como proyecto personal para practicar Flask y bases de datos.',
    'blog1.jpg'
);

INSERT INTO ENTRADAS (titulo, fecha, autor, contenido, imagen)
VALUES (
    'Aprendiendo Python',
    '2026-01-03',
    'Héctor',
    'Python es un lenguaje sencillo y potente que estoy utilizando para crear aplicaciones web.',
    'python.jpg'
);

INSERT INTO ENTRADAS (titulo, fecha, autor, contenido, imagen)
VALUES (
    'Primeros pasos con Flask',
    '2026-01-05',
    'Héctor',
    'Flask permite levantar un servidor web de forma rápida y conectar con bases de datos como SQLite.',
    'flask.jpg'
);

INSERT INTO ENTRADAS (titulo, fecha, autor, contenido, imagen)
VALUES (
    'Diseño con HTML y CSS',
    '2026-01-07',
    'Héctor',
    'He usado HTML y CSS para estructurar y dar estilo a la web del blog.',
    'htmlcss.jpg'
);
