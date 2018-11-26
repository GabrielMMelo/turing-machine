turing-machine
==============

Módulo desenvolvido por ``Gabriel Marques de Melo`` e ``Bruno Queiroz Santos`` para a disciplina de Teoria da Computação-GCC108 do curso de Ciência da Computação da Universidade Federal de Lavras.

O módulo implementa uma máquina de turing determinística para computação de funções numéricas.

.. toctree::
   :maxdepth: 3

   patterns
   reader
   tm

Leitura e validação do arquivo de entrada
-----------------------------------------

O módulo ``reader`` é o responsável por ler, validar e sumarizar o conteúdo do arquivo de entrada fornecida como argumento na execução do programa.

Cada tipo de dado do arquivo de entrada é verificada utilizando padrões em regexp implementados no módulo ``patterns``.


