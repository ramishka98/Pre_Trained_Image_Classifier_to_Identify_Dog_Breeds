#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/adjust_results4_isadog.py
#                                                                             
# PROGRAMMER: Ramishka Madhushan
# DATE CREATED:  06/29/2023                               
# REVISED DATE: 07/08/2023
#
def calculates_results_stats(results_dic):
    # Creates empty dictionary for results_stats_dic
    results_stats_dic = {}  
    
    # Sets all counters to initial values of zero
    results_stats_dic['n_images'] = 0
    results_stats_dic['n_dogs_img'] = 0
    results_stats_dic['n_notdogs_img'] = 0
    results_stats_dic['n_match'] = 0
    results_stats_dic['n_correct_dogs'] = 0
    results_stats_dic['n_correct_notdogs'] = 0
    results_stats_dic['n_correct_breed'] = 0
    
    # Process through the results dictionary
    for key in results_dic:
        results_stats_dic['n_images'] += 1  # Increment count for each image
        
        if results_dic[key][2] == 1:
            results_stats_dic['n_match'] += 1  # Increment count for each image where labels match
        
        # Pet Image Label is a Dog
        if results_dic[key][3] == 1:
            results_stats_dic['n_dogs_img'] += 1  # Increment count for each dog image
            
            # Classifier classifies image as Dog
            if results_dic[key][4] == 1:
                results_stats_dic['n_correct_dogs'] += 1  # Increment count for each correctly classified dog
        
        # Pet Image Label is NOT a Dog
        else:
            results_stats_dic['n_notdogs_img'] += 1  # Increment count for each non-dog image
            
            # Classifier classifies image as NOT a Dog
            if results_dic[key][4] == 0:
                results_stats_dic['n_correct_notdogs'] += 1  # Increment count for each correctly classified non-dog
        
        # Pet_Image_Label is a Dog AND Labels match
        if results_dic[key][3] == 1 and results_dic[key][2] == 1:
            results_stats_dic['n_correct_breed'] += 1  # Increment count for each correctly classified dog breed
    
    # Calculate the percentages
    results_stats_dic['pct_match'] = (results_stats_dic['n_match'] / results_stats_dic['n_images']) * 100
    results_stats_dic['pct_correct_dogs'] = (results_stats_dic['n_correct_dogs'] / results_stats_dic['n_dogs_img']) * 100
    results_stats_dic['pct_correct_notdogs'] = (results_stats_dic['n_correct_notdogs'] / results_stats_dic['n_notdogs_img']) * 100
    results_stats_dic['pct_correct_breed'] = (results_stats_dic['n_correct_breed'] / results_stats_dic['n_dogs_img']) * 100
    
    #
    #
    #
    # Returns the results
    return results_stats_dic  
