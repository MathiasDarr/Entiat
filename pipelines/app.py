#!/usr/bin/env python3

import aws_cdk as cdk

from pipelines.pipelines_stack import PipelinesStack


app = cdk.App()
PipelinesStack(app, "pipelines")

app.synth()
