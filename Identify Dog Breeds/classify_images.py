#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/classify_images.py
#                                                                             
# PROGRAMMER: Ramishka Madhushan
# DATE CREATED: 26/06/2023                                
# REVISED DATE: 02/07/2023
# PURPOSE: Create a function classify_images that uses the classifier function 
#          to create the classifier labels and then compares the classifier 
#          labels to the pet image labels. This function inputs:
#            -The Image Folder as image_dir within classify_images and function 
#             and as in_arg.dir for function call within main. 
#            -The results dictionary as results_dic within classify_images 
#             function and results for the functin call within main.
#            -The CNN model architecture as model wihtin classify_images function
#             and in_arg.arch for the function call within main. 
#           This function uses the extend function to add items to the list 
#           that's the 'value' of the results dictionary. You will be adding the
#           classifier label as the item at index 1 of the list and the comparison 
#           of the pet and classifier labels as the item at index 2 of the list.
#
##
# Imports classifier function for using CNN to classify images 
from classifier import classifier

def classify_images(images_dir, results_dic, model):
    """
    Creates classifier labels with the classifier function, compares pet labels to the classifier labels,
    and adds the classifier label and the comparison to the results dictionary.
    
    Parameters: 
        images_dir - The full path to the folder of images to be classified (string)
        results_dic - Results dictionary with 'key' as the image filename and 'value' as a list. 
                      The list contains the following items:
                      - index 0: pet image label (string)
                      - index 1: classifier label (string) [to be added]
                      - index 2: 1/0 (int) indicating a match between pet and classifier labels [to be added]
        model - Indicates the CNN model architecture to be used by the classifier function.
                Valid values are: 'resnet', 'alexnet', 'vgg' (string)
    """
    for key in results_dic:
        # Create the full path to the image file
        image_path = images_dir + key

        # Use the classifier function to get the classifier label
        classifier_label = classifier(image_path, model)

        # Format the classifier label to match pet image label format
        classifier_label = classifier_label.lower().strip()

        # Get the pet image label
        pet_label = results_dic[key][0]

        # Check if there is a match between the pet and classifier labels
        match = 1 if pet_label in classifier_label else 0

        # Add the classifier label and match value to the results dictionary
        results_dic[key].extend([classifier_label, match])
