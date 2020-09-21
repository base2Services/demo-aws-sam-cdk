#!/usr/bin/env python3

from aws_cdk import core

from demo_aws_sam_cdk.demo_aws_sam_cdk_stack import DemoAwsSamCdkStack


app = core.App()
DemoAwsSamCdkStack(app, "demo-aws-sam-cdk")

app.synth()
