#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/adjust_results4_isadog.py
#                                                                             
# PROGRAMMER: Ramishka Madhushan
# DATE CREATED:  06/29/2023                               
# REVISED DATE: 07/08/2023
#
def adjust_results4_isadog(results_dic, dogfile):
    # Read dog names from dogfile and create a set of dog names
    with open(dogfile, 'r') as file:
        dog_names = set(file.read().splitlines())
    #
    #
    #
    # Iterate through the results dictionary
    for key in results_dic:
        # Check if pet image label is of-a-dog
        if results_dic[key][0] in dog_names:
            results_dic[key].append(1)  # Append 1 if the pet image label is a dog
        else:
            results_dic[key].append(0)  # Append 0 if the pet image label is not a dog
     #   
        # Check if classifier label is of-a-dog
        if results_dic[key][1] in dog_names:
            results_dic[key].append(1)  # Append 1 if the classifier label is a dog
        else:
            results_dic[key].append(0)  # Append 0 if the classifier label is not a dog