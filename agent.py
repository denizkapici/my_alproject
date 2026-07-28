import os
import subprocess
from dotenv import load_dotenv

from langchain_core.tools import tool
from langchain_groq import ChatGroq
from langchain.agents import create_agent

# ---------------------------------------------------------
# 1. ORTAM DEĞİŞKENLERİ VE GROQ MODEL KURULUMU
# ---------------------------------------------------------
load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.1
)

# ---------------------------------------------------------
# 2. ARAÇLAR (TOOLS)
# ---------------------------------------------------------

@tool
def write_file(filepath: str, content: str) -> str:
    """Belirtilen dosya yoluna verilen kod veya metin içeriğini yazar."""
    try:
        dir_name = os.path.dirname(filepath)
        if dir_name:
            os.makedirs(dir_name, exist_ok=True)
            
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        return f"Dosya başarıyla oluşturuldu: {filepath}"
    except Exception as e:
        return f"Dosya yazma hatası: {str(e)}"

@tool
def git_commit_and_push(repo_url: str, commit_message: str, branch: str = "main") -> str:
    """Yerel dizindeki değişiklikleri commit edip hedef GitHub deposuna push eder."""
    try:
        subprocess.run(["git", "init"], check=True)
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        subprocess.run(["git", "branch", "-M", branch], check=True)
        
        subprocess.run(["git", "remote", "remove", "origin"], stderr=subprocess.DEVNULL)
        subprocess.run(["git", "remote", "add", "origin", repo_url], check=True)
        
        result = subprocess.run(["git", "push", "-u", "origin", branch], capture_output=True, text=True)
        if result.returncode == 0:
            return "Proje başarıyla GitHub deposuna yüklendi!"
        else:
            return f"Push Hatası: {result.stderr}"
    except Exception as e:
        return f"Git işlemi başarısız: {str(e)}"

tools = [write_file, git_commit_and_push]

# ---------------------------------------------------------
# 3. LANGGRAPH YENİ NESİL AGENT KURULUMU
# ---------------------------------------------------------

agent = create_agent(llm, tools)

# ---------------------------------------------------------
# 4. AJANI ÇALIŞTIRMA
# ---------------------------------------------------------
if __name__ == "__main__":
   
    repo_url = "https://github.com/denizkapici/my_alproject.git"
    
    task = (
        f"  1 den yüzde kadar random sayı üreten  bir Python CLI uygulaması geliştir. "
        f"Bir main.py, bir requirements.txt ve bir README.md oluştur. "
        f"Ardından bu projeyi '{repo_url}' reposuna push et."
    )
    
    print("Agent çalıştırılıyor...\n")
    response = agent.invoke({"messages": [("user", task)]})
    
    print("\n--- Tamamlanan Görev Sonucu ---")
    print(response["messages"][-1].content)