# Learning-with-Noisy-Class-Labels-for-Instance-Segmentation
ECCV2020: Learning with Noisy Class Labels for Instance Segmentation

## Introducton

The project is based on mmdetection. We will release more details soon!

## Installtion

Please check [install.md](docs/install.md) for installation instructions.

## Note

You can use the file [noisy_labels_AN_COCO.py](/noisy_labels_AN_COCO.py) and [noisy_labels_SN_COCO.py](/noisy_labels_SN_COCO.py) to generate class labels with asymmetric noise and symmetric noise for COCO dataset, respectively. The noise rate and the annotation file path need be set by yourself in the file. 

Our designed loss is provided in mmdet/models/losses/new_combination_loss.py. 
