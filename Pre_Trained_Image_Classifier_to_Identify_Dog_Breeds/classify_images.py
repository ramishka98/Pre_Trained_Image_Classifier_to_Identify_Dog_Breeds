#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/adjust_results4_isadog.py
#                                                                             
# PROGRAMMER: Ramishka Madhushan
# DATE CREATED:  06/29/2023                               
# REVISED DATE: 07/08/2023
#import the classifier
from classifier import classifier


def classify_images(images_dir, results_dic, model):
    for key in results_dic:
        image_path = images_dir + key
        classifier_label = classifier(image_path, model)
        
        # Process the classifier label
        classifier_label = classifier_label.lower().strip()
        

        # Update the results dictionary with the classifier label
        results_dic[key].append(classifier_label)
        
        #Compare the pet image_label with the classifier_label
        pet_label = results_dic[key][0]  
        match = 1 if pet_label in classifier_label else 0
        results_dic[key].append(match)
