# Conversor de Certificados HTML para PDF

Este projeto em Python automatiza a conversão de certificados em HTML para PDF.
O script gera arquivos em modo paisagem (horizontal), preserva cores de fundo e remove cabeçalhos e rodapés do navegador.

A conversão é feita com a biblioteca **Playwright**, que renderiza o HTML localmente em uma instância invisível do Chromium.

## Dependências

É necessário ter o **Python 3** instalado.

Instale as dependências com os comandos abaixo:

1. Instale a biblioteca Playwright:
   ```bash
   pip install playwright
   ```
2. Instale o navegador Chromium utilizado pelo Playwright:
   ```bash
   playwright install chromium
   ```

> Apenas para Linux / WSL:
> ```bash
> playwright install-deps
> ```

## 📂 Estrutura do Projeto

Para que o script funcione corretamente, os arquivos devem estar organizados da seguinte maneira:


    Projeto_Certificados/
    │
    ├── conversor.py              # O script Python principal
    └── certificados_html/        # Coloque os arquivos .html aqui
        ├── certificado_01.html
        └── certificado_02.html

**Nota:** A pasta de saída dos PDFs será criada automaticamente pelo script.

## Como Usar

1. Clone ou baixe este repositório para o seu computador.

```bash
git clone https://github.com/Gabriel-E-S/conversorHTMLparaPDF.git
```

2. Certifique-se de que instalou todas as dependências citadas acima.

3. Crie uma pasta chamada certificados_html no mesmo diretório do arquivo conversor.py.

4. Coloque todos os certificados .html que deseja converter dentro da pasta certificados_html.

5. Abra o terminal na pasta do projeto e execute o script:
    ```bash
    python3 conversor.py
    ```

O script fará a leitura de todos os arquivos. Ao finalizar, uma nova pasta chamada certificados_pdf será criada automaticamente contendo todos os seus certificados formatados e prontos em formato .pdf.