#############################################################################################
# Created by Kevin Edmond.
#
#
# This script is used to extract IAM policies from the configured AWS account and stores the
# data in a new CSV file named 'aws_policies.csv'. The retrieved policy data is filtered to
# only return attached permissions policies. Data returned from the query is written to the
# CSV file using the policyName, policyId, Arn fields extracted from the dataset.
#
#
# Please read README.md for full notes on script.
#
#############################################################################################


import csv
import boto3

# Setup Boto3 service client using default session
client = boto3.client('iam')

# Get AWS IAM policies using list_policies() method
response = client.list_policies(
    Scope='All',
    OnlyAttached=True,  # Return only the attached policies
    PolicyUsageFilter='PermissionsPolicy'
)

# Uncomment to check
# print(response['Policies'][0])

# Create CSV

# Create CSV file variables
csv_filename = "aws_policies.csv"
# Columns: Policy Name | PolicyId | Arn
csv_headers = ["Policy Name", "PolicyId", "Arn"]

with open(csv_filename, "w", newline='') as file:
    # Set CSV writer object
    writer = csv.writer(file)
    # Write header to CSV
    writer.writerow(csv_headers)

    # Iterate through the policy response data
    for policy in response['Policies']:
        writer.writerow(
            [policy['PolicyName'], policy['PolicyId'], policy['Arn']])


# Notify user of CSV creation
print(f"Your {csv_filename} file has been created.")
