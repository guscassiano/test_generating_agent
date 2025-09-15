# Gerador Automático de Testes Unitários com LangChain + OpenAI

Este projeto utiliza LangChain e OpenAI para gerar automaticamente arquivos de testes unitários em Python usando a biblioteca pytest.

## Funcionalidade

- O agente recebe um arquivo Python contendo funções como entrada.
- Utiliza a API da OpenAI para gerar um arquivo de testes (`test_<nome_do_arquivo>.py`) com funções de teste para casos de sucesso e falha.
- Os testes são compatíveis com pytest.

## Estrutura dos Arquivos

- `<nome_do_arquivo>.py`: Arquivo de funções Python a serem testadas.
- `test_generating_agent.py`: Script principal que gera o arquivo de testes.
- `.env`: Arquivo de configuração com variáveis de ambiente.
- `test_<nome_do_arquivo>.py`: Arquivo gerado automaticamente com os testes.

## Como Usar

1. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure o arquivo `.env`:**
   Crie (ou edite) o arquivo `.env` na raiz do projeto com o seguinte conteúdo:
   ```env
   OPENAI_API_KEY='sua-chave-openai-aqui'
   FILE_PATH='functions.py'
   ```
   - Substitua `'sua-chave-openai-aqui'` pela sua chave da OpenAI.
   - O `FILE_PATH` deve apontar para o arquivo Python que contém o código a ser testado.

3. **Execute o gerador de testes:**
   ```bash
   python test_generating_agent.py
   ```
   O arquivo `test_functions.py` (ou conforme o nome do arquivo definido em `FILE_PATH`) será criado automaticamente.

4. **Execute os testes com pytest:**

   ```bash
   pytest test_functions.py
   ```

## Observações
- Certifique-se de que o arquivo especificado em `FILE_PATH` existe e contém funções válidas.
- O agente utiliza a API da OpenAI, portanto é necessário ter uma chave válida.
- Os testes gerados podem ser ajustados conforme necessário.

## Exemplo

O arquivo `functions.py` é apenas um exemplo de arquivo com funções matemáticas simples para gerar o arquivo de teste.

---

Desenvolvido para facilitar a geração automática de testes unitários em projetos Python.
