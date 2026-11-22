# Prompt para Formatação de Tabelas Jurídicas no Word e LaTeX

Repositório contendo ferramentas e fontes para geração de documentos editáveis em Word (`.docx`) e compilação em LaTeX (`.pdf`).

---

## 📄 Para compilar em LaTeX e obter PDF

1. **Overleaf**: Importe o projeto no Overleaf, selecione **XeLaTeX** como compilador e `main.tex` como arquivo principal.
2. **Local (TeX Live / MiKTeX)**: Execute:
   ```bash
   xelatex main.tex
   xelatex main.tex
   ```
- O arquivo `main.tex` contém todo o texto, cores, sublinhados e estrutura do documento.
- O LaTeX recompõe as linhas e páginas de acordo com a fonte disponível (procura Calibri, Carlito e Latin Modern Sans).

---

## 📝 Para gerar o documento Word editável

Requer **Python 3.8+**:

```bash
python gerar_word.py
```

- O resultado gerado será `Prompt.docx`.
- Para definir outro nome de saída:
  ```bash
  python gerar_word.py Minha_copia.docx
  ```
- O texto e a formatação residem em `fonte_word/word/document.xml`. A pasta contém estilos, numeração e componentes originais.
- As fontes para LaTeX e Word são independentes. Edite a correspondente ao formato de saída desejado.
