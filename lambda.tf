resource "aws_lambda_function" "PutViewerCount" {
    filename = null
    image_uri = ""
    function_name = "lambda_PutViewerCount"
    role = "arn:aws:iam::220664688409:role/LambdaExecutionRole"
    handler = "lambda_PutViewerCount.lambda_handler"
    runtime = "python3.12"
    publish = null
}

resource "aws_lambda_function" "getViewerCount" {
    filename = null
    image_uri = ""
    function_name = "getViewerCount"
    role = "arn:aws:iam::220664688409:role/LambdaExecutionRole"
    handler = "getViewerCount.lambda_handler"
    runtime = "python3.12"
    publish = null
}