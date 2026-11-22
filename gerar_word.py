"""Gera um .docx editável usando as partes Office Open XML na pasta fonte_word."""
from pathlib import Path
from tempfile import NamedTemporaryFile
from zipfile import ZIP_DEFLATED, ZipFile
import argparse
import re


def compilar(destino):
    pasta = Path(__file__).resolve().parent / "fonte_word"
    if not (pasta / "word" / "document.xml").is_file():
        raise FileNotFoundError("Mantenha a pasta fonte_word ao lado de gerar_word.py.")
    destino = Path(destino).resolve()
    destino.parent.mkdir(parents=True, exist_ok=True)
    with NamedTemporaryFile(dir=destino.parent, suffix=".docx", delete=False) as auxiliar:
        temporario = Path(auxiliar.name)
    try:
        with ZipFile(temporario, "w", compression=ZIP_DEFLATED) as arquivo:
            for entrada in sorted(pasta.rglob("*")):
                if not entrada.is_file():
                    continue
                nome = entrada.relative_to(pasta).as_posix()
                dados = entrada.read_bytes()
                if nome == "word/document.xml":
                    # Retira apenas a indentação inserida entre elementos.
                    # Preserva os espaços dentro de w:t e a declaração XML original.
                    declaracao, separador, corpo = dados.partition(b"\n")
                    dados = declaracao + separador + re.sub(
                        rb">\r?\n[ \t]*(?=<)", b">", corpo
                    )
                arquivo.writestr(nome, dados)
        temporario.replace(destino)
    finally:
        temporario.unlink(missing_ok=True)
    return destino


if __name__ == "__main__":
    argumentos = argparse.ArgumentParser(description=__doc__)
    argumentos.add_argument("saida", nargs="?", default="Prompt.docx")
    print(compilar(argumentos.parse_args().saida))
