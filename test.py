import requests
import datetime

TOKEN='lsAR9Ruvmybge4MmkffRCULanDfn7dZMhV7ZGTj9HKP'
api_url='https://notify-api.line.me/api/notify'

time = datetime.datetime.now()
time = time.strftime('%Y/%m/%d  %H:%M:%S')

image_file='./868.jpg'
send_contents= 'テスト'

binary = open(image_file, mode='rb')
image_dic={'imageFile': binary}

TOKEN_dic = {'Authorization': 'Bearer' + ' ' + TOKEN}
send_dic = {'message': send_contents}
print(TOKEN_dic)
print(send_dic)

requests.post(api_url, headers=TOKEN_dic, data=send_dic, files=image_dic)