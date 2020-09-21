#!/usr/bin/env python3

from aws_cdk import core
from demo_aws_sam_cdk.api import Api

app = core.App()

api = Api(app, 'Api')
app.synth()
