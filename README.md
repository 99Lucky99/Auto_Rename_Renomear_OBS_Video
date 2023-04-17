# Auto_Rename_Renomear_OBS_Video

O Script é mediado por meio de eventos do OBS.

Quando este evento (OBS_FRONTEND_EVENT_RECORDING_STARTED) é ativo o script printa "Iniciando a Gravação".

Quando o evento (OBS_FRONTEND_EVENT_RECORDING_STOPPED) é ativo o script printa "Parando a Gravação", e inicia o processo de pegar a URL e renomear o arquivo.

A janela ativa no navegador no nosso caso "Edge" não deve ser minimizada pelo botao normal. Minimize pelo (Alt + TAB).

![image](https://user-images.githubusercontent.com/126738712/232372351-e28d5c6f-7f84-4444-a2c4-4434a391a5cd.png)


A url recebe alguns tratamentos antes de se tornar o nome do arquivo.

1 - Tratamento: So sera validado como nome do arquivo a partir do ultimo (/) encontrado na Url.

2 - Tratamento: Os caracteres invalidos para nome de arquivo do windows sao removidos, este são (/, |, <, >, *, :, “, ?).

Exemplo:

Url: https://www.test.com/????apenastestando$%%$%%$%$%$$%¨&;;>:>?

Nome Após os tratamentos: apenastestando$%%$%%$%$%$$%¨&;;

Depois é adicionado a extensao do arquivo neste caso estou usando (.mkv)

Nome do Arquivo Final: apenastestando$%%$%%$%$%$$%¨&;;.mkv


Obeservação: Caso queira usar outro navegador, mude esta linha edge = pyautogui.getWindowsWithTitle('Nome do Outro Navegador')[0]
