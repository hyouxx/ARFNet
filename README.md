# ARFNet: Enhancing Real-Time Underwater Object Detection via Adaptive Routing Fusion

> **Important**: This repository contains the official implementation of the manuscript **"ARFNet：A Dual-Backbone Network for Object Detection in Degraded Underwater Environments"** .

## 📖 Overview

ARFNet is a novel real-time underwater object detection system that achieves optimal balance among inference speed, precision, and recall. The core innovations include:


## 🎯 Performance

| Dataset | mAP@0.5 | Recall | FPS |
|---------|----------|---------|-----|
| URPC2020 | 87.2% | 80.2% | 228 |
| RUOD | 86.3% | 80.0% | 228 |

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- PyTorch 2.1.2+
- CUDA 11.8+

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/hyouxx/ARFNet.git
cd ARFNet
pip install -r requirements.txt
