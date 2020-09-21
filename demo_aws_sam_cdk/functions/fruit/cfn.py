from aws_cdk import core, aws_sam
import os 

class Fruit():

    def __init__(self, app, parameters):
        self.app = app
        self.env = parameters.get('environment')

    def function(self):
        function = aws_sam.CfnFunction(self.app, 'FruitFunction',
            code_uri=f"{os.path.dirname(os.path.realpath(__file__))}/src",
            handler='app.lambda_handler',
            runtime='python3.8',
            events={
                'FruitGet': aws_sam.CfnFunction.EventSourceProperty(
                    properties=aws_sam.CfnFunction.ApiEventProperty(
                        method="get",
                        path="/fruit"
                    ),
                    type='HttpApi'
                )
            },
            tags={
                'Environment': self.env
            }
        )

        return function