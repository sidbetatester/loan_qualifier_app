# -*- coding: utf-8 -*-
"""Helper functions to write and save new CSV data.

This contains a helper function for writing and saving CSV files.

"""
import csv
from pathlib import Path

def save_csv(qualifying_loan_data, new_csv_path_and_filename):
    """Saves the qualifying loans to a CSV file.

    Args:
        data (list of lists): The qualifying bank loans.
        path and file name
    """

    # Set the output header
    header = ["Lender", "Max Loan Amount", "Max LTV", "Max DTI", "Min Credit Score", "Interest Rate"]
    
    # Set a Path to a new CSV file
    #csvpath = Path("qualifing_loan_data.csv")
    csvpath = Path(new_csv_path_and_filename)


    # Open the CSV File
    with open(csvpath, 'w', newline='') as csvfile:     
        csvwriter = csv.writer(csvfile, delimiter=",")
    
        # Write the header to the CSV file
        csvwriter.writerow(header)

        # Write each item in bank_data_filtered as a row in the CSV file   
        for item in qualifying_loan_data:
            csvwriter.writerow(item)
    print("Successfully saved the qualifying data to qualifing_loan_data.csv file")