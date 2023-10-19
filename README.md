# Python AWS IAM Policy to CSV ETL Script

---

Created By Kevin Edmond

Repository for Python AWS IAM Policy to CSV ETL Script: Extract AWS IAM Policies and format into a CSV File

### Instructions:

1. Install `Python 3` for your system using instructions [here](https://www.python.org/downloads/).<br><br>

2. Install required packages.<br>

   ```python
   # Command:
   python3 pip install boto3
   ```

   <br>

3. Configure AWS credentials for account access. _NOTE_ This config is available if you have the [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) installed.<br>

   ```python
   # Command:
   aws configure
   ```

   <br>

4. Run the script.<br>

   ```python
   # Command:
   python3 iam_policy.py
   ```

   <br>

### Script Logic:

1. Setup Boto3 connection using `client`, variable to setup `boto.client()` method, and `response`, variable used to return boto.list_policies() method data, to retrieve AWS account IAM policies data.

2. The CSV file, filename (`aws_policies.csv`), and headers (`Policy Name`, `PolicyId`, `Arn`) are created.

3. A `for loop` is run to iterate through the `response` returned data and write each policy to a row in the `aws_policies.csv` file.

4. Notify the user that the CSV file was created.
