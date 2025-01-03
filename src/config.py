import torch
import os

MODEL_NAME = "unet_smaller_batch_size"

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

RS = 2
IN_CHANNELS = 1
OUT_CHANNELS = 1
LR = 1e-4
BATCH_SIZE = 16
MAX_EPOCHS = 200
EARLY_STOPPING_STEPS = 20
EARLY_STOPPING_MIN_DELTA = 0.001
IMAGE_WIDTH = 256
IMAGE_HEIGHT = 256

TRAIN_SIZE = 0.75
VAL_SIZE = 0.125
TEST_SIZE = 0.125

ROOT_DIR = "C:/Users/timcy/Documents/Code/Personal/U-Net/"
DF_PATH = 'data/df_full.csv'
DF_TEST_PATH = 'data/df_test.csv'
LOSS_PLOT_SAVE_PATH = f'output/{MODEL_NAME}/loss_plot.png'
HYPER_PARAM_SAVE_PATH = f'output/{MODEL_NAME}/hyper_params.json'
MODEL_SAVE_PATH = f'output/{MODEL_NAME}/trained.pth'
