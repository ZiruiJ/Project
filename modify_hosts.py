path = r'C:\Windows\System32\drivers\etc\hosts'

website= 'www.cnn.com'

with open(path, 'a') as f:
    f.write(f'\n127.0.0.1 {website}')
    print('success!')