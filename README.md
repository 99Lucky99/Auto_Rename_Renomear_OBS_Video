# Auto_Rename_Renomear_OBS_Video

O Script é mediado por meio de eventos do OBS.

Quando este evento (OBS_FRONTEND_EVENT_RECORDING_STARTED) é ativo, o script printa "Iniciando a Gravação".

Quando o evento (OBS_FRONTEND_EVENT_RECORDING_STOPPED) é ativo, o script printa "Parando a Gravação", e inicia o processo de pegar a URL e renomear o arquivo.

A janela ativa no navegador no nosso caso "Edge" não deve ser minimizada pelo botão normal. Minimize pelo (Alt + TAB).

![image](https://user-images.githubusercontent.com/126738712/232372351-e28d5c6f-7f84-4444-a2c4-4434a391a5cd.png)


A URL recebe alguns tratamentos antes de se tornar o nome do arquivo.

1 - Tratamento: Só sera validado como nome do arquivo a partir do último (/) encontrado na URL.

2 - Tratamento: Os caracteres inválidos para nome de arquivo do windows são removidos, este são (/, |, <, >, *, :, “, ?).

Exemplo:

URL: https://www.test.com/????apenastestando$%%$%%$%$%$$%¨&;;>:>?

Nome Após os tratamentos: apenastestando$%%$%%$%$%$$%¨&;;

Depois é adicionado a extensão do arquivo neste caso estou usando (.mkv)

Nome do Arquivo Final: apenastestando$%%$%%$%$%$$%¨&;;.mkv


Observação: Caso queira usar outro navegador, mude esta linha 
edge = pyautogui.getWindowsWithTitle('Nome do Outro Navegador')[0]

Observação: A pasta deve ser a mesma em que as gravações são do OBS são salvas. 
A pasta que uso é a Vídeos padrão do windows, caso queira mudar mude esta linha também 
recording_dir = os.path.join(os.path.expanduser("~"), "Videos")
