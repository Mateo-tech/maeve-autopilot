# MAEVE
An autonomous steering mechanism implementation based on a [Nvidia paper](https://images.nvidia.com/content/tegra/automotive/images/2016/solutions/pdf/end-to-end-dl-using-px.pdf).
Written in Python using TensorFlow.

## Important
Under no circumstances should this code be used for piloting a car.
Tests and demonstrations that have been performed were purerly for research, carefully observed and several precautions measures were in place.

It is extremely dangerous to use this software in a real car.

## Inspiration
1. [End to End Learning for Self-Driving Cars](https://images.nvidia.com/content/tegra/automotive/images/2016/solutions/pdf/end-to-end-dl-using-px.pdf)
2. [TensorFlow Implementation](https://github.com/SullyChen/Autopilot-TensorFlow)

## Data Collection
- Steering angle was being read using a DIY sensor
- Video input was recorded using a monocular camera at ~30 FPS (used in training)
- Existing datasets were used during different stages

## Network Architecture
- Weights are trained to minimize MSE between the predicted steering angle and the actual steering angle
- 9 Layers - Normalization Layer, 5 Convolutional Layers, 3 Fully Connected Layers
- 