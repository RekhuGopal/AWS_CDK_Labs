import aws_cdk as core
import aws_cdk.assertions as assertions

from democdklabspython1.democdklabspython1_stack import Democdklabspython1Stack

# example tests. To run these tests, uncomment this file along with the example
# resource in democdklabspython1/democdklabspython1_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = Democdklabspython1Stack(app, "democdklabspython1")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
