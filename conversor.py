import os
from playwright.sync_api import sync_playwright

pasta_origem = "certificados_html" # Pasta onde você deve colocar os  arquivos HTML
pasta_destino = "certificados_pdf" # Pasta que o script vai criar para salvar os PDFs


os.makedirs(pasta_destino, exist_ok=True)

def renderizar_certificados():
    with sync_playwright() as p:

        browser = p.chromium.launch()
        page = browser.new_page()

        for arquivo in os.listdir(pasta_origem):

            if arquivo.endswith(".html"):

                caminho_html = os.path.abspath(os.path.join(pasta_origem, arquivo))
                nome_pdf = arquivo.replace(".html", ".pdf")
                caminho_pdf = os.path.join(pasta_destino, nome_pdf)

                print(f"Gerando PDF: {arquivo} -> {nome_pdf}...")
                
                page.goto(f"file://{caminho_html}", wait_until="networkidle")
                
                page.pdf(
                    path=caminho_pdf,
                    format="A4",
                    landscape=True,  
                    print_background=True,
                    display_header_footer=False, 
                    margin={
                        "top": "15mm",
                        "right": "15mm",
                        "bottom": "15mm",
                        "left": "15mm"
                    }
                )

        browser.close()
        print("Sucesso! Todos os certificados foram convertidos.")

if __name__ == "__main__":
    renderizar_certificados()