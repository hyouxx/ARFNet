# ARFNet: Enhancing Real-Time Underwater Object Detection via Adaptive Routing Fusion

> **Important**: This repository contains the official implementation of the manuscript **"ARFNet: Enhancing Real-Time Underwater Object Detection via Adaptive Routing Fusion"** submitted to **The Visual Computer** (Submission ID: `88276d92-2806-4e59-9274-78584b48ca75`).

## 📖 Overview

ARFNet is a novel real-time underwater object detection system that achieves optimal balance among inference speed, precision, and recall. The core innovations include:

- **Shared Channel-Split Dual-Backbone (SCS-DB)**: Enables multi-scale feature reuse with reduced computational redundancy
- **DualPath-iA Module**: Leverages adaptive window attention mechanism to enhance model generalization  
- **SPD-Conv Replacement Strategy**: Preserves fine-grained features for small target detection

## 🎯 Performance

| Dataset | mAP@0.5 | Recall | FPS |
|---------|----------|---------|-----|
| URPC2020 | 87.2% | 80.2% | 228 |
| RUOD | 86.3% | 80.0% | 250 |

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
