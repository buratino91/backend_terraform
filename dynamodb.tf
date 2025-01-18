resource "aws_dynamodb_table" "ViewerCounter" {
    name = "ViewerCounter"
    hash_key = "id"
    billing_mode = "PROVISIONED"
    read_capacity = 10
    write_capacity = 5

    attribute {
      name = "id"
      type = "S"
    }
}