# -*- coding: utf-8 -*-
import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLO
# from ultralytics import RTDETR

if __name__ == '__main__':
    # model = RTDETR("rtdetr-resnet50.yaml")
    model = YOLO(model='.yaml')
    model = YOLO(model='.pt')
    model.train(data=r'.yaml',
                imgsz=640,
                epochs=300,
                batch=16,
                workers=0,
                device='0',
                optimizer='SGD',
                close_mosaic=10,
                resume=True,
                project='runs/train',
                name='exp',
                single_cls=False,
                cache=False,
                )