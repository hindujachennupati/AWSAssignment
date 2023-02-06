import boto3

# Initialize the clients for S3 and ECS
s3 = boto3.client("s3")
ecs = boto3.client("ecs")

def list_files_in_bucket(bucket_name):
    """
    Lists all files in the specified S3 bucket
    """
    response = s3.list_objects(Bucket=bucket_name)
    for obj in response.get("Contents", []):
        print(obj["Key"])

def list_task_definition_versions(service_name):
    """
    Lists all versions of the specified ECS task definition
    """
    response = ecs.list_task_definitions(serviceName=service_name)
    for task_definition in response["taskDefinitionArns"]:
        print(task_definition)

if __name__ == "__main__":
    # Parse the command line arguments
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=["list_files", "list_versions"])
    parser.add_argument("--bucket_name", default="my-bucket")
    parser.add_argument("--service_name", default="my-service")
    args = parser.parse_args()

    # Call the appropriate function based on the command line arguments
    if args.command == "list_files":
        list_files_in_bucket(args.bucket_name)
    elif args.command == "list_versions":
        list_task_definition_versions(args.service_name)
