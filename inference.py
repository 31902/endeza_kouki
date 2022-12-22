import cv2
import torch
import json
# Model Load
model = torch.hub.load('.', 'custom', path='./best.pt', source='local') 
model.conf = 0.5 

WIDTH = 640
HEIGHT = 640
FPS = 30
cap = cv2.VideoCapture(0)
#cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M','J','P','G'))
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('Y','U','Y','V'))
cap.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)
cap.set(cv2.CAP_PROP_FPS, FPS)

def inference(img):
  result = model(img)
  obj = result.pandas().xyxy[0]
  result.render() # Making the Result Image
  r_img = result.ims[0]

  return json.loads(obj.to_json(orient="records")), r_img

while (True):
    ret, img = cap.read() #カメラ画像取得
    if not ret:
        continue
    cv2.imshow("capture",img) #JPEG画像imgを表示する　処理速度は落ちる
    if cv2.waitKey(10) & 0xFF == ord(' '):
        break #スペースキーが入力されたらwhileループを抜ける
#cv2.imwrite("captureImage.jpg",img) #JPEG画像imgをファイルとして保存する
cv2.destroyAllWindows() #ウィンドウを閉じる
# Image Load
#img = cv2.imread('./868.JPG')
# Inference
r_json, r_img = inference(img)
print(' ')
# JSON Output
#for data in r_json:
    #print(data)
r_class = [d.get('class') for d in r_json] #Class data selection
#print(r_class)
if 0 in r_class:
    if not (1 in r_class):
        print('No Glove!')
    if not (2 in r_class):
        print('No Vest!')
    if not (3 in r_class):
        print('No Helmet!')
else:
    print('No Person!!!')
# Result Image Output
#cv2.imshow('result', r_img)
#cv2.waitKey(0)
cv2.imwrite('result.jpg', r_img) 
