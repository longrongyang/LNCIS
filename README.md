# Learning-with-Noisy-Class-Labels-for-Instance-Segmentation
The code for implementing the [LNIS](https://www.ecva.net/papers/eccv_2020/papers_ECCV/papers/123590035.pdf).

## 1. Introducton

Instance segmentation has achieved siginificant progress in the presence of correctly annotated datasets. Yet, object classes in largescale datasets are sometimes ambiguous, which easily causes confusion. In addition, limited experience and knowledge of annotators can also lead to mislabeled object classes. To solve this issue, a novel method is proposed in this paper, which uses different losses describing different roles of noisy class labels to enhance the learning. Specifically, in instance segmentation, noisy class labels play different roles in the foregroundbackground sub-task and the foreground-instance sub-task. Hence, on the one hand, the noise-robust loss (e.g., symmetric loss) is used to prevent incorrect gradient guidance for the foreground-instance sub-task. On the other hand, standard cross entropy loss is used to fully exploit correct gradient guidance for the foreground-background sub-task.

![Overview](Illustration/Overview.png)

The project is based on mmdetection v2.2.0. Main results in the paper are based on older mmdetection (v1.0rc0).

More details will be released.

## 2. Main Results

On Cityscapes dataset:

![Cityscapes](Illustration/Cityscapes.png)

On COCO dataset:

![COCO](Illustration/COCO.png)

## 3. Usage
### 3.1. Installtion

  Please check [install.md](docs/install.md) for installation instructions.

### 3.2. Data Generation

  For symmetric noise:
  1. Open the file [noisy_labels_SN_Cityscapes.py](https://github.com/longrongyang/LNCIS/blob/master/noisy_labels_SN_cityscapes.py).
  2. Modify the noise rate r, the annotation path p_a and the store path p_g.
  3. Run the file [noisy_labels_SN_Cityscapes.py](https://github.com/longrongyang/LNCIS/blob/master/noisy_labels_SN_cityscapes.py).
  
  For asymmetric noise:
  1. Open the file [noisy_labels_AN_Cityscapes.py](https://github.com/longrongyang/LNCIS/blob/master/noisy_labels_AN_Cityscapes.py).
  2. Modify the noise rate r， the annotation path p_a and the store path p_g.
  3. Run the file [noisy_labels_AN_Cityscapes.py](https://github.com/longrongyang/LNCIS/blob/master/noisy_labels_AN_Cityscapes.py).
  
  Similarly, noise under other datasets can be set.

### 3.3. Stage-Wise Training

  For Cityscapes dataset:
  1. For the first stage, models should be trained with the config [mask_rcnn_r50_fpn_1x_cityscapes_nl_1.py](/configs/cityscapes/mask_rcnn_r50_fpn_1x_cityscapes_nl_1.py).
  2. For the second stage, models should be trained with the config [mask_rcnn_r50_fpn_1x_cityscapes_nl_2.py](/configs/cityscapes/mask_rcnn_r50_fpn_1x_cityscapes_nl_2.py):
  ```shell
  ./tools/dist_train.sh ${CONFIG_FILE} ${GPU_NUM} --resume-from ${MODEL_PATH}
  ```
  The second stage needs use the model trained in the first stage.
  
  Other datasets should apply similar settings.

### 3.4. Evaluation
  
  Please check [getting_started.md](docs/getting_started.md) for details.

## 4. Designed Loss

  1. Our designed loss is provided in [new_combination_loss.py](/mmdet/models/losses/new_combination_loss.py). 
  - PON is not the key contribution of this paper and it brings marginal increase. You can select to use it or not.
  - When the dataset type is changed, the label assigned for background is changed. The corresponding change should be set in the file.
  2. Symmetric cross entropy loss is provided in [symmetric_cross_entropy_loss.py](/mmdet/models/losses/symmetric_cross_entropy_loss.py) 
  3. Generalized cross entropy loss is provided in [generalized_cross_entropy_loss.py](/mmdet/models/losses/generalized_cross_entropy_loss.py).
  
## 5. Citations
Please consider citing our paper in your publications if the project helps your research. BibTeX reference is as follows.

```
@InProceedings{Yang_2020_ECCV,
  title   = {Learning with Noisy Class Labels for Instance Segmentation,
  author  = {Longrong, Yang and Fanman Meng and Hongliang Li and Qingbo, Wu and Qishang, Cheng},
  booktitle = {European Conference on Computer Vision (ECCV)},
  year={2020}
}
```
