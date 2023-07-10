#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/adjust_results4_isadog.py
#                                                                             
# PROGRAMMER: Ramishka Madhushan
# DATE CREATED:  06/29/2023                               
# REVISED DATE: 07/08/2023
#import argparse
import argparse


def get_input_args():
    parser = argparse.ArgumentParser()
    # Create command line arguments


    parser.add_argument('--dir', type=str, default='pet_images/', help='Folder that contains the pet images')
    parser.add_argument('--arch', type=str, default='vgg', help='CNN model architecture to use')
    parser.add_argument('--dogfile', type=str, default='dognames.txt', help='File that contains the list of valid dognames')
    
    # Return parsed_argument_collection
    return parser.parse_args()
