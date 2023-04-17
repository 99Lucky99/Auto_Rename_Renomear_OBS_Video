import obspython as obs
import os
import shutil
import time
import pyautogui
import time
import clipboard


def script_load(settings):
	obs.obs_frontend_add_event_callback(on_event)

def script_unload():
	obs.obs_frontend_remove_event_callback(on_event)


def on_event(event):
	if event == obs.OBS_FRONTEND_EVENT_RECORDING_STARTED:
		print("Iniciando a Gravação")

	if event == obs.OBS_FRONTEND_EVENT_RECORDING_STOPPED:
		print("Parando a Gravação")
		# Esperar 5 segundos para a gravação terminar
		time.sleep(3)
				# Encontre a janela do Edge
		edge = pyautogui.getWindowsWithTitle('Edge')[0]
		edge.activate()

		# Selecione a guia desejada
		pyautogui.hotkey('ctrl', '1')  # Substitua '1' pelo número da guia desejada

		# Simule as teclas Ctrl+L para selecionar a barra de endereço
		pyautogui.hotkey('ctrl', 'l')
		time.sleep(0.5)  # Espere um pouco para garantir que a barra de endereço foi selecionada

		# Simule as teclas Ctrl+C para copiar a URL
		pyautogui.hotkey('ctrl', 'c')
		time.sleep(0.5)  # Espere um pouco para que a URL seja copiada para a área de transferência

		# Obtenha a URL da área de transferência
		url = clipboard.paste()
		vetor = []
		for i in url:
			if i == '/':
				vetor = []
			elif i == '|':
				vetor.append('')
			elif i == '<':
				vetor.append('')
			elif i == '>':
				vetor.append('')
			elif i == '*':
				vetor.append('')
			elif i == ':':
				vetor.append('')
			elif i == '?':
				vetor.append('')
			elif i == '“':
				vetor.append('')
			else:
				vetor.append(i)

		# Diretório onde o arquivo de gravação será salvo
		recording_dir = os.path.join(os.path.expanduser("~"), "Videos")
		# Obter o nome do arquivo de gravação mais recente
		newest_file = None
		newest_time = 0
		for filename in os.listdir(recording_dir):
			if filename.endswith(".mkv"):
				file_path = os.path.join(recording_dir, filename)
				file_time = os.path.getctime(file_path)
				if file_time > newest_time:
					newest_file = filename
					newest_time = file_time

		if newest_file is None:
			print("Não foi possível encontrar o arquivo de gravação mais recente")
			exit()

		# Definir o novo nome de arquivo e extensão
		new_filename = ''.join(vetor) + ".mkv"

		# Caminho completo do arquivo de gravação mais recente
		old_file_path = os.path.join(recording_dir, newest_file)

		# Caminho completo do novo arquivo de gravação
		new_file_path = os.path.join(recording_dir, new_filename)

		# Renomear o arquivo de gravação
		shutil.move(old_file_path, new_file_path)

		# Imprimir uma mensagem informando que o nome do arquivo foi alterado
		print("O nome do arquivo foi alterado de {} para {}".format(newest_file, new_filename))