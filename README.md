# :warning: Self-Bot para o Discord :warning:
> Antes de falar "merda", como "Pow, você apoia isto? self.bot é contra as regras do discord.", primeiramente esse repositório foi criado para fins educacional... tendo isto em mente aparti daqui "EU" não me resposabilizo pelo que irão fazer com este projeto.

Self.bot é geralmente usado para usar uma conta do discord `("sim aquela que você logar com email e senha pelo site ou aplicativo")`, invés de você usar a `"conta bot"` você irá usar aquela que você criou com email e senha, somente isto... vale resaltar que essa é uma pratica abolida do discord, a conta que for pega usando este procedimento certamente será banida permanente e apagada do discord.

*(Vale citar também, não me responsabilizo pelo o que você ou outras pessoas irão fazer com este projeto. Não é problema meu. Também não dou suporte)*
 
 ## Então chega de conversa, vamos lá.
 
 * 1° - Tenha o Python instalado, você poderia baixa-lo aparti deste [link](https://www.python.org) instale-o normamente (caso tenha duvida veja um video no youtube.
 
 * 2° - Tenha o Discord.py 0.16.12(ou superior) instalado, neste [link](https://github.com/Rapptz/discord.py) você encontrar um tutorial de como instalo corretamente.
 
 * 3° - Tenha um editor de texto de sua preferencia instalado para abrir ou editar o arquivo (eu uso o [sublime](https://sublimetext.com))
 
 ## Aqui abaixo se encontrar o script, ou se deseja baixe o script usando o "Botão verde".
 
 
 ```py
import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print(client.user.name)
    print(client.user.id)
    print('Bot Online')

@client.event
async def on_message(message):
    if message.content.startswith('!test'):
        await client.send_message(message.channel, 'Bot testado!')

#client.run('token')
#client.run('email','senha')
```

* 4° - Agora basta configura o seu bot com seu token ou email/senha da sua conta. (Caso não saiba pegar o token da conta tem video no youtube a respeito)

* 5° - Após te configurado seu bot, você irá da run nele.

* 6° - Como dou run nele? .. Simples basta "abrir" seu cmd.exe e ir na pasta do arquivo e pegar a url da pasta e digitar no cmd.exe `cd <local>`, após ter setado o local digite `python arquivo.py`.

* 7° - Pronto seu self.bot estará online.
