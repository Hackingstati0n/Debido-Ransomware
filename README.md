# Educational Ransomware Simulation

⚠️ AVISO CRÍTICO: PROJETO EXCLUSIVAMENTE EDUCACIONAL

Este software foi desenvolvido APENAS para fins educacionais e de pesquisa em segurança cibernética. O uso malicioso é estritamente proibido e pode resultar em consequências legais severas.

## Sobre o Projeto

Simulação educacional avançada de ransomware desenvolvida para demonstrar técnicas modernas de criptografia, persistência e evasão. Este projeto visa educar profissionais de segurança, estudantes e pesquisadores sobre mecanismos de defesa através da compreensão de vetores de ataque.

## Características Técnicas

### Mecanismos de Criptografia
- AES-256-GCM - Criptografia autenticada de alto desempenho
- Fernet (AES-128-CBC + HMAC) - Dupla camada de segurança
- 5 Ciclos de Encriptação - Processo multi-camadas
- Corrupção Intencional - Destruição irreversível de dados

### Suporte a Extensões
Mais de 200 tipos de arquivo suportados, incluindo:

- Documentos: .doc, .docx, .pdf, .txt, .rtf (25+)
- Planilhas: .xls, .xlsx, .csv, .ods (15+)
- Imagens: .jpg, .png, .raw, .psd, .ai (30+)
- Vídeos: .mp4, .avi, .mov, .mkv (20+)
- Áudio: .mp3, .wav, .flac, .aac (15+)
- Bancos de Dados: .sql, .mdb, .accdb, .sqlite (15+)
- Código Fonte: .py, .java, .js, .html, .cpp (40+)

### Funcionalidades Avançadas
- Auto-Persistência - Cópia automática para %TEMP%
- Inicialização Automática - Atalho na pasta Startup
- Propagação em Rede - Disseminação para shares de rede
- Anti-Recuperação - Exclusão de Shadow Copies
- Destruição Segura - Sobrescrita múltipla de dados

## Finalidade Educacional

### Objetivos de Aprendizado
- Compreender vetores de ataque ransomware
- Desenvolver estratégias de detecção
- Implementar mecanismos de prevenção
- Criar procedimentos de resposta a incidentes
- Testar soluções de backup e recuperação

### Cenários de Uso Apropriados
- Laboratórios de segurança controlados
- Pesquisa acadêmica em cibersegurança
- Treinamento de equipes SOC
- Desenvolvimento de ferramentas de detecção

## Instalação e Configuração

### Pré-requisitos
Clone o repositório:
git clone https://github.com/seu-usuario/educational-ransomware-sim.git
cd educational-ransomware-sim

Instale as dependências:
pip install pycryptodome cryptography

### Ambiente de Teste Seguro
⚠️ SEMPRE execute em ambiente isolado
Use máquinas virtuais ou containers Docker

Exemplo de ambiente seguro:
docker run -it --rm -v $(pwd):/app python:3.9 /app

## Como Usar (Ambiente Controlado)

### Execução Básica
Execute com confirmação de segurança:
python ransomware_sim.py

Saída esperada:
Iniciando processo de destruição de arquivos...
ESTE PROCESSO É IRREVERSÍVEL!
Continuar? (s/N):

## Estrutura do Código

educational-ransomware-sim/
│
├── debido.py          # Código principal
├── requirements.txt           # Dependências
├── README.md                  # Documentação
├── LICENSE                    # Licença MIT
├── test_environment.py        # Script de teste seguro


## Fluxograma de Comportamento: 
<img width="1563" height="4414" alt="deepseek_mermaid_20251127_d88f04" src="https://github.com/user-attachments/assets/385ef140-9b8f-4242-bd0a-69cad2d9cb62" />, <img width="2478" height="2937" alt="E para a função percorrer_diretorio_destrui" src="https://github.com/user-attachments/assets/e7542cba-be09-47d2-aa8c-6d2666aad880" />, <img width="1574" height="2645" alt="E para destroy_file_5x" src="https://github.com/user-attachments/assets/caf72466-33de-4258-9772-1f7c9f74bfd4" />, <img width="735" height="1212" alt="encrypt_and_corrupt" src="https://github.com/user-attachments/assets/ca04574f-382c-4fd6-87cb-50f4cca43dbb" />

## Avisos Legais e Éticos

❌ USO PROIBIDO
- Atividades maliciosas ou criminosas
- Testes em sistemas sem autorização
- Distribuição para terceiros sem contexto educacional
- Uso em ambientes de produção

✅ USO PERMITIDO
- Pesquisa acadêmica autorizada
- Treinamento de segurança em ambientes controlados
- Desenvolvimento de ferramentas defensivas
- Estudos de análise forense

## Estatísticas do Projeto

Extensões Suportadas: 200+
Python Version: 3.8+
License: MIT

## Contribuição

Contribuições são bem-vindas para fins educacionais:

1. Fork o projeto
2. Crie uma branch para sua feature (git checkout -b feature/AmazingFeature)
3. Commit suas mudanças (git commit -m 'Add some AmazingFeature')
4. Push para a branch (git push origin feature/AmazingFeature)
5. Abra um Pull Request

## Licença

Distribuído sob licença MIT. Veja LICENSE para mais informações.

## Autores

- Seu Nome - Pesquisador em Segurança - [SeuGitHub](https://github.com/seu-usuario)

---

LEMBRE-SE: CONHECIMENTO É PODER, USE-O COM RESPONSABILIDADE

Este projeto visa educar para proteger, não para causar danos.
