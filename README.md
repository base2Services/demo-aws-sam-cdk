# AWS SAM With AWS CDK

This is a simple api that returns a random food selection for either /veggies or /fruit.

The cloudformation is written in python using the aws-cdk library and transformed into a sam tempate. from that point the sam-cli is used to managed the stacks and local testing 

*NOTE: All the following shell commands are in the context of the root of the repository directory unless specified*

## Requirements

1. aws-cdk - [install](https://docs.aws.amazon.com/cdk/latest/guide/getting_started.html#getting_started_install)
2. sam-cli - [install](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)

## Setup Python Environment

1. clone and cd into the repo

2. setup the python environment

    ```sh
    python -m venv .env
    source .env/bin/activate
    ```

3. install depencies

    ```sh
    pip install -r requirements.txt
    ```

## Deploying

1. transfor the cdk to a SAM cloudformation template

    ```sh
    cdk synth > template.yaml
    ```

2. build the sam functions

    ```sh
    sam build
    ```

3. deploy the stack

    ```sh
    sam deploy
    ```

## SAM Local Tests

1. transfor the cdk to a SAM cloudformation template

    ```sh
    cdk synth > template.yaml
    ```

2. build the sam functions

    ```sh
    sam build
    ```

3. test a function

    ```sh
    $ sam local invoke FruitFunction
    ```

    Output 

    ```sh
    Invoking app.lambda_handler (python3.8)
    Image was not found.
    Building image................................................................................................................................................................................................................................................................................................................................................................................................................................................................
    Failed to download a new amazon/aws-sam-cli-emulation-image-python3.8:rapid-1.0.0 image. Invoking with the already downloaded image.
    Mounting /Users/gus/src/demo/demo-aws-sam-cdk/.aws-sam/build/FruitFunction as /var/task:ro,delegated inside runtime container
    START RequestId: a997f24f-5b57-1163-caf3-2e96acff1dde Version: $LATEST
    END RequestId: a997f24f-5b57-1163-caf3-2e96acff1dde
    REPORT RequestId: a997f24f-5b57-1163-caf3-2e96acff1dde	Init Duration: 219.56 ms	Duration: 5.11 ms	Billed Duration: 100 ms	Memory Size: 128 MB	Max Memory Used: 24 MB

    {"statusCode":200,"body":"{\"selection\": \"kiwi fruit\"}"}
    ```

## PyTest

1. install test dependencies

    ```sh
    pip install -r requirements-dev.txt
    ```

2. run unit tests

    ```sh
    python -m pytest
    ```