path = r'C:\Windows\System32\drivers\etc\hosts'

website= 'www.youtube.com'

with open(path, 'a') as f:
    f.write(f'127.0.0.1 {website}')
    