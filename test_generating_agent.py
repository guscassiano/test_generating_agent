import os

from dotenv import load_dotenv
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate


load_dotenv()

def test_generator(file_path, api_key):
    with open(file_path, 'r', encoding='utf-8') as f:
        code = f.read()

    prompt = PromptTemplate(
        input_variables=["codigo"],
        template="""
Você é um gerador de testes unitários em Python usando pytest. Receba o seguinte código Python:

{code}

Gere um arquivo de testes chamado test_<nome>.py, contendo:
- import pytest na primeira linha
- funções def test_* para casos de sucesso e falha
- Os testes devem rodar corretamente com pytest
Retorne apenas o código do arquivo de testes e as importações das funções que estão em teste.
O nome do arquivo que estão as funções é {file_path}.
"""
    )

    llm = OpenAI(openai_api_key=api_key, temperature=0.1)
    response = llm.invoke(prompt.format(code=code, file_path=file_path))
    return response

if __name__ == "__main__":
    api_key = os.getenv("OPENAI_API_KEY")
    print(f"Usando chave da OpenAI: {api_key[:4]}...{api_key[-4:]}")

    file_path = os.getenv("FILE_PATH")
    print(f"Gerando testes para o arquivo: {file_path}")

    tests_code = test_generator(file_path, api_key)
    test_file_name = f"test_{os.path.basename(file_path)}"

    with open(test_file_name, "w", encoding="utf-8") as f:
        f.write(tests_code)

    print(f"Arquivo de testes gerado: {test_file_name}")
