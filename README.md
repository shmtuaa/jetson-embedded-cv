# Jetson
jetson大创存盘

G20210604 基于Jetson的自主口罩检查机器人

成员：李梁裕 邓明 王啸凡 朱嘉俊 王周怡

指导老师：董一琳


## 运行

准备好jetson nano 4GB 或相同以上配置\
打开终端输入git clone https://github.com/pjreddie/darknet.git \
cd darknet \
输入vi Makefile编辑编译文件GPU=1 ,CUDNN=1 ,OPENCV=1 , NVCC=PATH（PATH为设备上nvcc的位置，一般在usr/local/cuda-x/bin/nvcc） \
保存退出后 输入make开始编译 \
编译完成后输入./darknet测试 若出现usage: ./darknet <function>则安装成功 \
将start.sh中的exprot的路径分别改为darknet所在路径和该目录所在路径 \
在 https://pjreddie.com/media/files/darknet53.conv.74 下载 darknet53.conv.74模型到darknet安装目录中 \
在终端中输入./datainit.py 运行脚本。 \
终端中输入./start.sh即可运行人脸口罩识别系统 \
若遇到camera类错误请修改start.sh文件中 -c 1 改为-c 0 该程序目前仅支持usb摄像头 \

软件环境配置 \
参考yolov5 requirements.txt
## Base ----------------------------------------
matplotlib>=3.2.2\
numpy>=1.18.5\
opencv-python>=4.1.2\
Pillow>=7.1.2\
PyYAML>=5.3.1\
requests>=2.23.0\
scipy>=1.4.1\
torch>=1.7.0\
torchvision>=0.8.1\
tqdm>=4.41.0
## Logging -------------------------------------
tensorboard>=2.4.1\
wandb
## Plotting ------------------------------------
pandas>=1.1.4\
seaborn>=0.11.0
## Export --------------------------------------
coremltools>=4.1  # CoreML export\
onnx>=1.9.0  # ONNX export\
onnx-simplifier>=0.3.6  # ONNX simplifier\
scikit-learn==0.19.2  # CoreML quantization\
tensorflow>=2.4.1  # TFLite export\
tensorflowjs>=3.9.0  # TF.js export\
openvino-dev  # OpenVINO export
## Extras --------------------------------------
albumentations>=1.0.3\
Cython  # for pycocotools https://github.com/cocodataset/cocoapi/issues/172 \
pycocotools>=2.0  # COCO mAP\
roboflow\
thop  # FLOPs computation
