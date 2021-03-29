from aws_cdk import (aws_ec2 as ec2, core)
from aws_cdk.core import Tags


class VpcPlaygroundStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        vpc = ec2.Vpc(
        self, "Adam_MyVpc",
        cidr="10.13.0.0/21",
        max_azs=2,
        nat_gateways=1,
        subnet_configuration=[
            ec2.SubnetConfiguration(name="public", cidr_mask=24, subnet_type=ec2.SubnetType.PUBLIC),
            ec2.SubnetConfiguration(name="private", cidr_mask=24, subnet_type=ec2.SubnetType.PRIVATE),
            ec2.SubnetConfiguration(name="isolated", cidr_mask=24, subnet_type=ec2.SubnetType.ISOLATED)
        ]
    )    

        Tags.of(vpc).add("Owner", "Adam")
    
