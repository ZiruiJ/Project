path = r'C:\Windows\System32\drivers\etc\hosts'

website= 'www.cnn.com'

with open(path, 'w') as f:
    f.write(f'\n #127.0.0.1 {website}')
    print('success!')