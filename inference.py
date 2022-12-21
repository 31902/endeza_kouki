import cv2
import torch
# Model Load
model = torch.hub.load('.', 'custom', path='./best.pt', source='local') 
# Image Load
img = cv2.imread('./868.JPG')
# Inference
result = model(img)
obj = result.pandas().xyxy[0]
print(obj.to_json(orient="records")) # JSON Output
result.render() # Making the Result Image
r_img = result.ims[0]
cv2.imshow('result', r_img)
cv2.waitKey(0)
cv2.imwrite('result.jpg', r_img) # Result Image Output