<h1 align="center"> MAEVE AUTOPILOT</h1>

An autonomous steering mechanism implementation based on the [Nvidia paper](https://images.nvidia.com/content/tegra/automotive/images/2016/solutions/pdf/end-to-end-dl-using-px.pdf) tested on a real-size car with custom hardware. 
 
<div align="center">
 
![](https://media.giphy.com/media/HUBSzphkTC2HXJf80k/giphy.gif)
![](https://media.giphy.com/media/xEgdH1FvRfpLub40tv/giphy-downsized-large.gif)
 
 </div>

Demo: TEMPORARILY DISABLED

# Implementation Details
## Data Collection
- The model of the car that was used for this project had no in-built steering angle sensor or a CAN bus - the steering angle was collected using a customized sensor. Same goes for the the steering unit. 
- Video input was recorded using a monocular camera at ~30 FPS (used in training)
- Due to the experimental nature of this project, existing datasets were used during different stages. 

## Network Architecture & Training
Apart from some changes, the network follows the original architecture described in the Nvidia paper. This is the used architecture:
- Weights are trained to minimize the MSE between the output of the network and the recorded steering angle
- 6 Convolution Layers (ReLU activation)
- Max Pooling Layers used after every Convolution Layer
- 3 Fully Connected Layers
- A single output neuron (=> steering angle), default activation

For the demo, the model is intentionally overfitted in order to make the model remember the short distances of more complex sequences it drove through more precisely. However, the model generalizes well on new data.

## Inspiration
1. [End to End Learning for Self-Driving Cars](https://images.nvidia.com/content/tegra/automotive/images/2016/solutions/pdf/end-to-end-dl-using-px.pdf)
2. [TensorFlow Implementation](https://github.com/SullyChen/Autopilot-TensorFlow)
 
## Note
Under no circumstances should this code be used for piloting a car. Tests and demonstrations were performed purerly for research, carefully observed and several precautions and safety mechanisms were in place, including an external controller for taking over the wheel and notification system of an increasing error.
It is EXTREMELY dangerous to use this software in a real car.
