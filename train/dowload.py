from rutube import Rutube
from io import BytesIO

rt = Rutube('https://rutube.ru/video/9710a030d62d0e197dda190638f6e9b5/')

print(rt.playlist)  # [Nature 4k (272x480), Nature 4k (408x720), Nature 4k (608x1080)]

video = rt.playlist[-1]
video.download()