#!/bin/bash

model_path=$1
gpu=$2

CUDA_VISIBLE_DEVICES=$gpu python main.py --model_args pretrained=${model_path} --tasks hella
CUDA_VISIBLE_DEVICES=$gpu python main.py --model_args pretrained=${model_path} --tasks arc
CUDA_VISIBLE_DEVICES=$gpu python main.py --model_args pretrained=${model_path} --tasks truth
CUDA_VISIBLE_DEVICES=$gpu python main.py --model_args pretrained=${model_path} --tasks mmlu

