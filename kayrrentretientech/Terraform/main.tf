provider "aws" {
  region = "eu-north-1"
}

resource "aws_instance" "example" {
  ami           = "ami-0df024d681444bc53"
  instance_type = "t3.micro"

  tags = {
    Name = "entretien"
  }
}
