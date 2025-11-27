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


## 📊 Fluxograma de Comportamento

<div align="center" style="overflow-x: auto; white-space: nowrap; padding: 20px; background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%); border-radius: 15px; border: 2px solid #e1e8ed;">
  
  <div style="display: inline-flex; gap: 25px; padding: 15px;">
    
    <!-- Fluxograma 1 - encrypt_and_corrupt -->
    <div style="display: inline-block; text-align: center;">
      <div style="background: white; padding: 15px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
        <h4 style="margin: 0 0 10px 0; color: #2c3e50;">🔐 encrypt_and_corrupt</h4>
        <img 
          width="350" 
          height="578" 
          alt="Fluxograma encrypt_and_corrupt" 
          src="https://github.com/user-attachments/assets/34325bac-de23-4629-bd7f-248de9ab4319" 
          style="border: 2px solid #3498db; border-radius: 8px;"
        />
      </div>
    </div>

    <!-- Fluxograma 2 - destroy_file_5x -->
    <div style="display: inline-block; text-align: center;">
      <div style="background: white; padding: 15px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
        <h4 style="margin: 0 0 10px 0; color: #2c3e50;">💥 destroy_file_5x</h4>
        <img 
          width="400" 
          height="672" 
          alt="Fluxograma destroy_file_5x" 
          src="https://github.com/user-attachments/assets/f7ad1491-2533-454f-b23b-ca55e7a2d62c" 
          style="border: 2px solid #e74c3c; border-radius: 8px;"
        />
      </div>
    </div>

    <!-- Fluxograma 3 - percorrer_diretorio_destruir -->
    <div style="display: inline-block; text-align: center;">
      <div style="background: white; padding: 15px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
        <h4 style="margin: 0 0 10px 0; color: #2c3e50;">📁 percorrer_diretorio_destruir</h4>
        <img 
          width="450" 
          height="533" 
          alt="Fluxograma percorrer_diretorio_destruir" 
          src="https://github.com/user-attachments/assets/9c525885-e36b-4960-8e8e-a0a643957fcb" 
          style="border: 2px solid #27ae60; border-radius: 8px;"
        />
      </div>
    </div>

    <!-- Fluxograma 4 - Fluxograma Principal -->
    <div style="display: inline-block; text-align: center;">
      <div style="background: white; padding: 15px; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
        <h4 style="margin: 0 0 10px 0; color: #2c3e50;">🚀 Fluxograma Principal</h4>
        <img 
          width="500" 
          height="1412" 
          alt="Fluxograma Principal" 
          src="https://github.com/user-attachments/assets/5063a0f1-01f6-494b-a19c-0260fe1eca8d" 
          style="border: 2px solid #9b59b6; border-radius: 8px;"
        />
      </div>
    </div>

  </div>
</div>

<div style="text-align: center; margin-top: 15px;">
  <small style="color: #7f8c8d;">
    🖱️ <em>Use a barra de rolagem horizontal para visualizar todos os fluxogramas</em> 🖱️
  </small>
</div>



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
