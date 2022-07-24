from constructs import Construct
from aws_cdk import (
    Duration,
    Stack,

)


class PipelinesStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

