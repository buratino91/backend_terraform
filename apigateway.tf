resource "aws_apigatewayv2_api" "getViewCount" {
  name          = "getViewCount"
  protocol_type = "HTTP"
  tags = {}

  cors_configuration {
    allow_credentials = true
    allow_headers = []
    allow_methods = ["GET", "POST"]
    allow_origins = ["https://my-b4d3-resume.com"]
    expose_headers = []
    max_age = 300
  }
}

resource "aws_apigatewayv2_api" "UpdateCounter" {
  name          = "UpdateCounter"
  protocol_type = "HTTP"
  tags = {}

  cors_configuration {
    allow_credentials = true
    allow_headers = ["content-type"]
    allow_methods = ["POST"]
    allow_origins = ["https://my-b4d3-resume.com"]
    expose_headers = []
    max_age = 300
  }

}

resource "aws_apigatewayv2_integration" "getViewCount" {
  api_id           = var.api_id_get
  integration_type = "AWS_PROXY"
  integration_uri  = "arn:aws:lambda:us-east-1:220664688409:function:getViewerCount"
  payload_format_version = "2.0"
}

resource "aws_apigatewayv2_integration" "UpdateCounter" {
  api_id           = var.api_id_post
  integration_type = "AWS_PROXY"
  integration_uri  = "arn:aws:lambda:us-east-1:220664688409:function:lambda_PutViewerCount"
  payload_format_version = "2.0"
}

