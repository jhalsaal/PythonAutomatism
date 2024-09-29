from pytube import YouTube
url = 'https://youtu.be/n_BP8EWkcDI?si=tMhvb1c9_BasS3GR'
try:
    yt = YouTube(url)
    print(f'Titulo: {yt.title}')
except:
    print('Error de conexión')

download_video = yt.streams.get_by_resolution('720p')
try:
    download_video.download(',')
except:
    print('Error en la descarga')

print('descarga completa')