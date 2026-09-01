import socket
import ssl

alvo = input("Digite o IP ou Endereco para escanear: ")

portas_abertas = []

servicos_conhecidos = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    135: "RPC",
    139: "NetBIOS",
    443: "HTTPS",
    445: "SMB",
    3306: "MySQL",
    3389: "RDP"
}
def pegar_banner(alvo,porta):
    try:
        banner_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        banner_socket.settimeout(2)

        if porta == 443:
            contexto = ssl.create_default_context()
            banner_socket = contexto.wrap_socket(banner_socket, server_hostname=alvo)


        banner_socket.connect((alvo, porta))
        pedido = b"GET / HTTP/1.1\r\nHost: " + alvo.encode() + b"\r\n\r\n"
        banner_socket.send(pedido)
        resposta = banner_socket.recv(4096)
        banner_socket.close()
        return resposta.decode(errors="ignore").split("\r\n")[0]
    except Exception as erro:
        return f"Nao foi possivel capturar banner ({erro})" 

for porta in range(1, 1001):
    meu_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    meu_socket.settimeout(0.05)
    resultado = meu_socket.connect_ex((alvo, porta))
    if resultado == 0:
        nome_servico = servicos_conhecidos.get(porta, "Desconhecido")
        banner  = pegar_banner(alvo, porta)
        portas_abertas.append((porta, nome_servico, banner))
    meu_socket.close()

print(f"Total de portas abertas: {len(portas_abertas)}")
for porta, servico, banner in portas_abertas:
    print(f"Porta {porta} está aberta! ({servico}) - banner: {banner}")