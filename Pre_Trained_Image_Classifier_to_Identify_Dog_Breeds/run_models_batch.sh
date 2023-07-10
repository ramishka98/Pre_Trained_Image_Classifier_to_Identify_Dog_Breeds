#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/adjust_results4_isadog.py
#                                                                             
# PROGRAMMER: Ramishka Madhushan
# DATE CREATED:  06/29/2023                               
# REVISED DATE: 07/08/2023
#
# Command to check pet images using the resnet model and save the results to a file
python check_images.py --dir pet_images/ --arch resnet --dogfile dognames.txt > resnet_pet-images.txt

# Command to check pet images using the alexnet model and save the results to a file
python check_images.py --dir pet_images/ --arch alexnet --dogfile dognames.txt > alexnet_pet-images.txt

# Command to check pet images using the vgg model and save the results to a file
python check_images.py --dir pet_images/ --arch vgg --dogfile dognames.txt > vgg_pet-images.txt
