# Video2Music: Music Generation to Match Video using an Affective Multimodal Transformer model

This repository contains the code and dataset accompanying the paper "Video2Music: Suitable Music Generation from Videos using an Affective Multimodal Transformer model" by Dr. Jaeyong Kang, Prof. Soujanya Poria, and Prof. Dorien Herremans.

- Demo: [https://amaai-lab.github.io/AIMuVi/](https://amaai-lab.github.io/AIMuVi/)
- Dataset (Muvi-Sync)
  * Muvi-Sync [(5 MB)]()
  * Muvi-Sync (audio, video) (optional) [(5 MB)]()
  
## Introduction
we propose a novel AI-powered multimodal music generation framework called Video2Music. This framework uniquely uses video features as conditioning input to generate matching music using a Transformer architecture. By employing cutting-edge technology, our system aims to provide video creators with a seamless and efficient solution for generating tailor-made background music.

![](framework.png)

If you find this resource useful, [please cite the original work](https://arxiv.org/abs/XXX):

      @article{XXX,
        title={Music Generation to Match Video using an Affective Multimodal Transformer model},
        author={Kang, Jaeyong and Poria, Soujanya and Herremans, Dorien},
        journal={arXiv preprint arXiv:XXX},
        year={2023}
      }

  Kang, J., Poria, S. & Herremans, D. (2023). Music Generation to Match Video using an Affective Multimodal Transformer model. arXiv preprint arXiv:XXX.


## Directory Structure

* `saved_models/`: saved model files
* `utilities/`
  * `run_model_vevo.py`: training script, take a npz as input music data to train the model
  * `run_model_regression.py`: training script, take a npz as input music data to train the model
* `model/`: code of affective multimodal transformer (AMT) model 
  * `video_music_transformer.py`: Affective Multimodal Transformer (AMT) model 
  * `video_regression.py`: Bi-GRU regression model used for predicting note density/loudness
  * `positional_encoding.py`: code for Positional encoding
  * `rpr.py`: code for RPR (Relative Positional Representation)
* `dataset/`: 
  * `vevo_dataset.py`: Dataset loader
* `train.py`: training script
* `evaluate.py`: evaluation script
* `generate.py`: inference script

## Preparation

* Clone this repo

* Obtain the dataset:
  * Muvi-Sync [(5 MB)]()
  * Muvi-Sync (audio, video) (optional) [(5 MB)]()
 
* Put all directories started with `vevo` in the dataset under this folder (`dataset/`) 

* Download the processed training data `AMT.zip` from [HERE](https://drive.google.com/file/d/1ZPQiTyz8wqxwPdYxYSCEtq4MLbR5s9jh/view?usp=drive_link) and extract the zip file and put the extracted two files directly under this folder (`saved_models/AMT/`) 

* Install dependencies `pip install -r requirements.txt`
  * Choose the correct version of `torch` based on your CUDA version

## Training

  ```shell
  python train.py
  ```

## Inference

  ```shell
  python generate.py
  ```

