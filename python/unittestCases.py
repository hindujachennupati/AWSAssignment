import unittest
from unittest.mock import patch

class TestListFilesInBucket(unittest.TestCase):

    @patch("boto3.client")
    def test_list_files_in_bucket(self, mock_client):
        mock_s3 = mock_client.return_value
        mock_s3.list_objects.return_value = {
            "Contents": [
                {"Key": "file1"},
                {"Key": "file2"},
                {"Key": "file3"},
            ]
        }
        
        list_files_in_bucket("my-bucket")
        mock_s3.list_objects.assert_called_with(Bucket="my-bucket")

class TestListTaskDefinitionVersions(unittest.TestCase):

    @patch("boto3.client")
    def test_list_task_definition_versions(self, mock_client):
        mock_ecs = mock_client.return_value
        mock_ecs.list_task_definitions.return_value = {
            "taskDefinitionArns": [
                "arn1",
                "arn2",
                "arn3",
            ]
        }
        
        list_task_definition_versions("my-service")
        mock_ecs.list_task_definitions.assert_called_with(serviceName="my-service")
