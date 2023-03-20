export DARKNET=$HOME/darknet
export PRJ_PATH=$HOME/Desktop/mask

cd $DARKNET
./darknet detector demo \
$PRJ_PATH/mask.data \
$PRJ_PATH/yolov4-tiny-custom.cfg \
$PRJ_PATH/backup/yolov4-tiny-custom_last.weights \
 -thresh .5 -c 1
