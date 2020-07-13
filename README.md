# Learning-with-Noisy-Class-Labels-for-Instance-Segmentation
ECCV2020: Learning with Noisy Class Labels for Instance Segmentation

## Introducton

The project is based on mmdetection v2.2.0. More details will be released! The results in the paper are mainly based on older mmdetection (v1.0rc0).

## Installtion

Please check [install.md](docs/install.md) for installation instructions.

## Data Generation

Files [noisy_labels_AN_Cityscapes.py](/noisy_labels_AN_Cityscapes.py) and [noisy_labels_SN_Cityscapes.py](/noisy_labels_SN_Cityscapes.py) can be used to generate class labels with asymmetric noise and symmetric noise for Cityscapes dataset, respectively. The noise rate and the annotation file path need be set in these files. 

## Designed Loss

Our designed loss is provided in [new_combination_loss.py](/mmdet/models/losses/new_combination_loss.py). Symmetric cross entropy loss and generalized cross entropy loss are also provided in [symmetric_cross_entropy_loss.py](/mmdet/models/losses/symmetric_cross_entropy_loss.py) and [generalized_cross_entropy_loss.py](/mmdet/models/losses/generalized_cross_entropy_loss.py), respectively.

## Stage-wise Training

On Cityscapes dataset, models should be firstly trained with the config [mask_rcnn_r50_fpn_1x_cityscapes_nl_1.p](/configs/cityscapes/mask_rcnn_r50_fpn_1x_cityscapes_nl_1.py) in early stages of training. Then, in mature stages of training, the config [mask_rcnn_r50_fpn_1x_cityscapes_nl_2.p](mask_rcnn_r50_fpn_1x_cityscapes_nl_2.py) is used to train models.
