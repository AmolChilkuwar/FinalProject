from aws_cdk import (
    # Duration,
    Stack, aws_s3 as _s3
    # aws_sqs as sqs,
)
import aws_cdk as cdk
from constructs import Construct


class S3(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        _s3.Bucket(self,
                   "myfirstbucket",
                   bucket_name='s3newpiyusbhomale1999',
                   versioned=True,
                   removal_policy=cdk.RemovalPolicy.DESTROY)  # Destroy S3 when cloud is destroyed if empty
