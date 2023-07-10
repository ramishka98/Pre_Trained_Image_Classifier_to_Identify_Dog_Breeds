#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/adjust_results4_isadog.py
#                                                                             
# PROGRAMMER: Ramishka Madhushan
# DATE CREATED:  06/29/2023                               
# REVISED DATE: 07/08/2023
#
from os import listdir

def get_pet_labels(image_dir):
    results_dic = {}

    # Get the list of filenames in image directory
    filename_list = listdir(image_dir)
    for filename in filename_list:
        if filename.startswith('.'):
            continue  # Skip files starting with a "."  

        # Split the filename into words
        word_list = filename.lower().split('_')

        pet_label = ''  # Create an empty string for the pet image label

        for word in word_list:  # Process each word in the filename
            if word.isalpha():  # Check if the word is alphabetic
                pet_label += word + ' '  # Add the word to the pet image label with a space separator
        pet_label = pet_label.strip()  # Strip leading and trailing whitespace characters from the label

        results_dic[filename] = [pet_label]  # Add the filename and pet image label to the dictionary

    return results_dic  # Return the result dictionary with pet_image_labels
