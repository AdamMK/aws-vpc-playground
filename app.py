#!/usr/bin/env python3

from aws_cdk import core

from vpc_playground.vpc_playground_stack import VpcPlaygroundStack


app = core.App()
VpcPlaygroundStack(app, "vpc-playground")

app.synth()
