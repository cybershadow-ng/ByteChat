Perfeito! Aqui está o **README completo pronto para copiar e colar**, sem nada a alterar:

````markdown
# ByteChat

![Python](https://img.shields.io/badge/python-3.x-blue) ![License](https://img.shields.io/badge/license-MIT-green)

**ByteChat** é uma ferramenta de chat TCP **peer-to-peer** para redes locais (LAN), desenvolvida em Python.  
Inspirado no conceito minimalista do Netcat, permite comunicação direta entre cliente e servidor sem necessidade de internet, com **autenticação opcional por senha**.

> Comunicação simples. Direta. Sem intermediários.

---

## ✨ Features

- Modos **Servidor** e **Cliente**
- Comunicação **TCP via LAN**
- **Autenticação opcional por senha**
- Interface simples em **terminal (CLI)**
- Projeto **educacional**, ideal para aprender sobre sockets em Python

---

## 🛠 Requisitos

- Python **3.x**
- Sistema operacional com suporte a **TCP sockets**
- Linux/Unix recomendado (funciona em Windows, mas com ajustes mínimos)

---

## 🚀 Como Usar

### 1. Clonar o repositório

```bash
git clone https://github.com/seuusuario/ByteChat.git
cd ByteChat
````

### 2. Rodar o programa

```bash
python3 bytechat.py
```

> O programa exibirá um menu para iniciar como **Servidor** ou **Cliente**.

---

### 3. Funcionalidades

#### Servidor

* Configure **IP** e **porta** (padrões: `127.0.0.1` e `8080`)
* Ative ou não a **senha de autenticação**
* Aguarde conexões de clientes na rede local
* Troque mensagens em tempo real

#### Cliente

* Informe o **IP** e a **porta** do servidor
* Insira a **senha**, se habilitada
* Envie e receba mensagens diretamente do servidor

---

## 💡 Exemplo de Uso

```
╔════════════════════╗
║     Chat Local     ║
║ Conectado: 192.168.0.10:8080 ║
╚════════════════════╝
You: Olá, tudo bem?
(192.168.0.10): Olá! Tudo certo!
```

---

## 📚 Aprendizado

ByteChat é um projeto **educacional** perfeito para:

* Entender **sockets TCP** em Python
* Praticar **comunicação peer-to-peer** em LAN
* Aprender sobre **autenticação básica**

---

## ⚖️ Licença

MIT License – veja o arquivo [LICENSE](LICENSE) para mais detalhes.
