#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/adjust_results4_isadog.py
#                                                                             
# PROGRAMMER: Ramishka Madhushan
# DATE CREATED:  06/29/2023                               
# REVISED DATE: 07/08/2023
#import the time and sleep
from time import time, sleep

# Imports print functions that check the lab and functions created for this program
from print_functions_for_lab_checks import *
from get_pet_labels import get_pet_labels
from get_input_args import get_input_args
from adjust_results4_isadog import adjust_results4_isadog
from calculates_results_stats import calculates_results_stats
from classify_images import classify_images
from print_results import print_results
#
#Main program function are defined
def main():
    #Measures total program runtime by collecting start time
    start_time = time()  
    in_arg = get_input_args()
    #Function that checks command line arguments using in_arg
    check_command_line_arguments(in_arg)  



    results = get_pet_labels(in_arg.dir)
    # Function that checks Pet Images in the results Dictionary using results
    check_creating_pet_image_labels(results)  

    classify_images(in_arg.dir, results, in_arg.arch)
    check_classifying_images(results)  # Function that checks Results Dictionary using results


    adjust_results4_isadog(results, in_arg.dogfile)



    check_classifying_labels_as_dogs(results)  # Function that checks Results Dictionary for is-a-dog adjustment using results
    
    results_stats = calculates_results_stats(results)
    print_results(results, results_stats, in_arg.arch, True, True)

    # Measure total program runtime by collecting end time
    end_time = time()

    # Compute overall runtime in seconds & print it in hh:mm:ss format  
    tot_time = end_time - start_time  
    print("\n** Total Elapsed Runtime:",
          str(int((tot_time / 3600))) + ":" + str(int((tot_time % 3600) / 60)) + ":"
          + str(int((tot_time % 3600) % 60)))



if __name__ == "__main__":
    # Call to the main function to run the program
    main()
