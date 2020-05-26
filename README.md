# Improvement of Skin Disease Identification System using Generative AI

This is the official code release for the paper titled -
### "Improvement of skin disease identification system using Generative AI"

## Abstract of the Paper 
Identification of skin diseases, such as leprosy, Tinea
Versicolor, and Vitiligo from the normal skin is one of the
challenging tasks due to having all but similar kind of nature
and variation of skin types and its color. Therefore, success rate
for identification of the disease is comparatively poor compared
to the other computer vision tasks. Traditional deep learning
models are not successful in this domain due to the lack of a huge
number of data. To address the problem, in the present work,
we introduced a customized Generative Adversarial Network
(GAN) to generate synthetic data. With data augmentation, we
found maximum 94.25% recognition accuracy using DensenNet-
121, which is 10.95% better than the accuracy achieved without
augmentation.

### Packages Required
This repository containes the implementation of described methodology in `Python` language with the help of `PyTorch` Deep Learning framework.

The details requirement is [here](requirements.txt)

We recommend creating a virtual `conda` environment first, then proceed further.
```bash
conda create -n <env_name> python=3.7.3
conda activate <env_name>
pip install -r requirements.txt # It will install required dependencies.
```
## Repository Structure

**"GCN"** : It contains the implementation of preprocessing steps, for e.g. `global contrast normalization`.

**"WGAN_GP"** : It contains the implemenation of Wasserstien GAN (Generative Adversarial Network) with Gradient penalty. And a code to generate synthetic samples from random noise vector.

**"assets"** : Contains a subset of original dataset, & related images for markdown files.


Copyright 2019, Bisakh Mondal, Nibaran Das, K.C. Sontosh, Mita Nasipuri, All rights reserved.
