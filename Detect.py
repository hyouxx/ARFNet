import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO(model='./runs/train/exp/weights/best.pt') # select your model.pt path
    model.predict(source='./datasets/URPC2020/test/images/000003.jpg',
                  imgsz=640,
                  project='runs/detect',
                  name='exp',
                  save=True,
                  # classes=1, # 是否指定检测某个类别.
                )