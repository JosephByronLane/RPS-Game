# RPS-Game

![Alt Text](https://i.imgur.com/XFqZifB.png)

`NOTE:` This doesn't contain the models or the training data. Only the code to train/play the game.

## Features

- Play Rock-Paper-Scissors using real hand gestures
- Start/stop the game with thumbs up/down gestures
- Configurable game settings
- GPU acceleration support (for training)
- Model training capabilities

## Requirements

- Python 3.x
- TensorFlow 2.x with GPU support (optional but recommended)
- OpenCV
- NumPy
- Matplotlib
- PyAutoGUI
- CUDA (for GPU acceleration)

## Installation

1. Clone this repository or download the Jupyter notebook
2. Ensure you have the required Python packages installed:
   ```bash
   pip install tensorflow opencv-python numpy matplotlib pyautogui
   ```
3. For GPU acceleration, make sure CUDA and cuDNN are properly set up

## Game Settings

You can modify the following game settings in the "basic game functionality" cell:

- `thumbs_duration`: Time you need to hold a thumbs up/down gesture to activate/deactivate the game (default: 2 seconds)
- `total_turns`: Number of turns per game (default: 5)
- `countdown_time`: Time you have to choose a move (default: 5 seconds)
- `wait_between_turns`: Delay between turns (default: 2 seconds)
- `wait_after_game_end`: Delay after a game ends (default: 3 seconds)

## Usage

1. Run the Jupyter notebook cells in sequence
2. A webcam window will open showing your camera feed
3. Give a "thumbs up" gesture for 2 seconds to start the game
4. When the countdown begins, make your move (rock, paper, or scissors)
5. The computer will randomly select its move
6. The result will be displayed (who won the round)
7. After all turns complete, the final score and winner will be shown
8. Give a "thumbs down" gesture for 2 seconds to stop the game
9. Press 'q' to quit the application

## Advanced Configuration

### Model Settings

You can configure the following settings for model training:

- `generate_new_model`: Set to true to train a new model (default: True)
- `epochs`: Number of training epochs (default: 25)
- `steps_per_epoch`: Steps per epoch (default: 25)
- `image_size`: Image resolution (default: 150x150)
- `batch_size`: Batch size for training (default: 512)
- `val`: Enable validation during training (default: True)

### Data Augmentation Settings

- `make_aug_images`: Generate augmented images for training (default: False)
- `aug_image_workers`: Number of workers for image augmentation (default: CPU cores/2)
- `num_augmented_images_per_input`: Number of augmented variants per image (default: 5)

## Model Training

If you want to train your own model:

1. Set `generate_new_model = True` in the advanced settings
2. Configure the training and augmentation settings
3. Run the notebook cells
4. The model will be saved to the `rpsmodels` directory

## Pre-trained Models

No pre-trained models are provided at the moment.

## Troubleshooting

### Missing Model Error

Ensure you have a model loaded in a folder called 'rpsmodels' in the same directory as the notebook. If this notebook is in `C:/Rock paper scissors.ipynb`, make sure there's a trained model in `C:/rpsmodels/model_name.h5`.

### High CPU/GPU Usage

Make sure to set `generate_new_model` and `make_aug_images` to False in the advanced settings if you just want to play the game.

## Acknowledgments

This project was based on TensorFlow's "Build an image classifier" tutorial (ML Zero to Hero - Part 4) with additional customizations and improvements to support GPU acceleration and a custom neural network architecture.
