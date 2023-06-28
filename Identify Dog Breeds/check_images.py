#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/check_images.py
#
# TODO 0: Add your information below for Programmer & Date Created.
# PROGRAMMER: Ramishka Madhushan
# DATE CREATED: 26/06/2023
# REVISED DATE:
# PURPOSE: Classifies pet images using a pretrained CNN model, compares these
#          classifications to the true identity of the pets in the images, and
#          summarizes how well the CNN performed on the image classification task.
#          Note that the true identity of the pet (or object) in the image is
#          indicated by the filename of the image. Therefore, your program must
#          first extract the pet image label from the filename before
#          classifying the images using the pretrained CNN model. With this
#          program, we will be comparing the performance of 3 different CNN model
#          architectures to determine which provides the 'best' classification.

# Imports python modules
from time import time
from get_input_args import get_input_args
from get_pet_labels import get_pet_labels
from classify_images import classify_images
from adjust_results4_isadog import adjust_results4_isadog
from calculates_results_stats import calculates_results_stats
from print_results import print_results

def main():
    start_time = time()

    in_arg = get_input_args()

    results = get_pet_labels(in_arg.dir)

    classify_images(in_arg.dir, results, in_arg.arch)

    adjust_results4_isadog(results, in_arg.dogfile)

    results_stats = calculates_results_stats(results)

    print_results(results, results_stats, in_arg.arch, True, True)

    end_time = time()

    tot_time = end_time - start_time
    print("\n** Total Elapsed Runtime:",
          str(int((tot_time / 3600))) + ":" + str(int((tot_time % 3600) / 60)) + ":"
          + str(int((tot_time % 3600) % 60)))


if __name__ == "__main__":
    main()
