#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/adjust_results4_isadog.py
#                                                                             
# PROGRAMMER: Ramishka Madhushan
# DATE CREATED:  06/29/2023                               
# REVISED DATE: 07/08/2023
#
def print_results(results_dic, results_stats_dic, model,
                  print_incorrect_dogs=False, print_incorrect_breed=False):
    # Print model architecture
    print("Using CNN model architecture:", model)  
    print()


    # Print results
    print("Number of Images:", results_stats_dic['n_images'])
    print("Number of Dog Images:", results_stats_dic['n_dogs_img'])
    print("Number of Not-a-Dog Images:", results_stats_dic['n_notdogs_img'])
    print()
    


    # Print the percentages
    for key in results_stats_dic:
        if key.startswith('pct'):
            print(key + ":", results_stats_dic[key])
    


    print()
    


    # Print misclassified dogs if requested
    if print_incorrect_dogs:
        print("Misclassified Dog Images:")
        for key in results_dic:
            if sum(results_dic[key][3:]) == 1:
                print("Pet Image:", key)
                print("Classifier Label:", results_dic[key][1])
                print()

    # Print misclassified dog breeds if requested
    if print_incorrect_breed:
        print("Misclassified Dog Breed Images:")
        for key in results_dic:
            if sum(results_dic[key][3:]) == 2 and results_dic[key][2] == 0:
                print("Pet Image:", key)
                print("Classifier Label:", results_dic[key][1])
                print()
