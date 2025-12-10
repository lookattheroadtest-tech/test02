#!/bin/bash


set -e


TOKEN=$(cat auth_file)
export TOKEN


python3 replay.py


echo "Running nuclei..."
nuclei -t nuclei-template.yaml -var token=$TOKEN -o nuclei_output.txt


echo "Done. Logs saved."
