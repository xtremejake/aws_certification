import subprocess

CENSUS_1994_DATA = "https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data"

def main():
    """Prerequisites are to have installed awscli, and setup user credentials
    
    1) sudo apt install awscli
    2) navigate to the aws console at https://console.aws.amazon.com/console and create a new IAM user with credentials 
    https://console.aws.amazon.com/iamv2/home?#/users - click on add user, download .csv with credentials after creation
    3) aws configure --csv import <path/to/csv/credentials.csv> # doesn't work? I had to manually type the keys in using aws configure and following prompts
    4) aws s3 mb s3://xtremejake-cloudacademy-emr-spark-census-data
    
    TODO: Make into bash script instead of python
    # aws s3 nb help # note use q to quit ctrl+c doesn't work
    # aws s3 cp adult.data s3://cloudacademy-emr-spark-census-data
    # aws s3 ls s3://cloudacademy-emr-spark-census-data

    """
    p = subprocess.Popen(["curl", "-O", f"{CENSUS_1994_DATA}"])
    p.wait()
    p.terminate()
    # sudo apt install awscli
    # navigate to the aws console at https://console.aws.amazon.com/console and create a new IAM user with credentials 
    # https://console.aws.amazon.com/iamv2/home?#/users - click on add user
    # download .csv with credentials after creation
    # aws configure --csv import <path/to/csv/credentials.csv> # doesn't work? I had to manually type the keys in using aws configure and following prompts
    # aws s3 nb help # note use q to quit ctrl+c doesn't work
    # aws s3 mb s3://xtremejake-cloudacademy-emr-spark-census-data 
    # aws s3 cp adult.data s3://cloudacademy-emr-spark-census-data
    # aws s3 ls s3://cloudacademy-emr-spark-census-data


if __name__ == "__main__":
    main()
