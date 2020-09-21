from aws_cdk import core
from aws_cdk.core import CfnParameter
from demo_aws_sam_cdk.functions.fruit.cfn import Fruit
from demo_aws_sam_cdk.functions.veggies.cfn import Veggies

class Api(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        
        environment = CfnParameter(self, "Environment", type="String", default="dev",
            description="environment name")

        parameters = {
            'environment': environment.value_as_string
        }

        fruit = Fruit(self, parameters)
        fruit.function()

        veggies = Veggies(self, parameters)
        veggies.function()