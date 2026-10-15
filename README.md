# Estudos de Python e Orientação a Objetos

## Sobre
- Meu objetivo com este repositório é compartilhar meu aprendizado autodidata em Python e paralelamente estudando Engenharia de Software, afim de demonstrar meu interesse na linguagem de programação e compreender o paradigma da Orientação a Objetos com Python
- Durante o percurso de estudos, demonstrei técnicas de Aprendizado de Máquina, pequenos exercícios de Python e POO.

## Conteúdos estudados
- Fundamentos da linguagem Python
- Classes, objetos e encapsulamento
- Herança, abstração e polimorfismo
- Tratamento de erros e manipulação de arquivos
- Padrões de projeto
- Projetos práticos

## Projetos em destaque

- **PyBank** (`projetos/pyBank.py`): sistema bancário de linha de comando com clientes, contas corrente e poupança, operações de depósito e saque, transferência e persistência de dados em JSON. Demonstra classes, herança, composição e encapsulamento.

- **Tratamento de erros** (`fundamentos/tryExceptFinally.py`): exemplos de uso de `try`, `except`, `else` e `finally` para lidar com entradas inválidas, divisão por zero e tipos incompatíveis. Inclui também uma demonstração interativa com widgets.

- **Estudos de aprendizado de máquina** (`inteligencia-artificial/aprendizadoMaquina.py` e `inteligencia-artificial/aprendizadoMaquina2.py`): exercícios de preparação de dados com Pandas e Scikit-learn, incluindo divisão entre conjuntos de treino e teste, tratamento de valores ausentes e normalização.

- **Padrão Factory Method** (`orientacao-a-objetos/designPatterns.py`): exemplo de criação de notificações por diferentes canais, como e-mail e SMS, usando classes abstratas e o padrão Factory Method.

- **Coleções e arquivos** (`projetos/colecoesArquivos.py`): leitura e gravação de arquivos de texto, processamento de notas e uso de listas e dicionários para organizar os resultados.

- **Arrays em Python** (`fundamentos/arraysPython.py`): explora listas, o módulo `array` e estruturas de bibliotecas como NumPy, Pandas e SciPy. O exemplo apresenta arrays unidimensionais e multidimensionais, operações matemáticas e matrizes esparsas.

## Como executar

1. Instale o Python 3.
2. Abra um terminal na pasta do repositório.
3. Crie e ative um ambiente virtual:

   ```powershell
   py -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

4. Instale as bibliotecas necessárias para os exemplos de arrays e aprendizado de máquina:

   ```powershell
   python -m pip install numpy pandas scipy scikit-learn matplotlib ipywidgets
   ```

5. Execute um arquivo pelo terminal, por exemplo:

   ```powershell
   python orientacao-a-objetos/interfacePython.py
   ```

   Para executar outro exemplo, substitua o caminho pelo arquivo desejado, como `projetos/pyBank.py` ou `fundamentos/arraysPython.py`.

## Observação
Este repositório reúne exercícios e projetos de estudo; o conteúdo evolui conforme novos conceitos são aprendidos.