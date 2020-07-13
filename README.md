# Learning-with-Noisy-Class-Labels-for-Instance-Segmentation
ECCV2020: Learning with Noisy Class Labels for Instance Segmentation

## Introducton

The project is based on mmdetection. We will release more details!

## Installtion

Please check [install.md](docs/install.md) for installation instructions.

## Note

You can use the file [noisy_labels_AN_Cityscapes.py](/noisy_labels_AN_Cityscapes.py) and [noisy_labels_SN_Cityscapes.py](/noisy_labels_SN_Cityscapes.py) to generate class labels with asymmetric noise and symmetric noise for Cityscapes dataset, respectively. The noise rate and the annotation file path need be set by yourself in the file. 

Our designed loss is provided in [new_combination_loss.py](/mmdet/models/losses/new_combination_loss.py). 

On Cityscapes dataset, models should be firstly trained with the config [mask_rcnn_r50_fpn_1x_cityscapes_nl_1.p](/configs/cityscapes/mask_rcnn_r50_fpn_1x_cityscapes_nl_1.py) in early stages of training. Then, in mature stages of training, the config [mask_rcnn_r50_fpn_1x_cityscapes_nl_2.p](mask_rcnn_r50_fpn_1x_cityscapes_nl_2.py) should be used to train models.
