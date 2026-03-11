
provider "aws" {
  region = "us-east-2"
}

resource "aws_instance" "skynet_server" {
  ami           = "ami-0f5ee92e2d63afc18"
  instance_type = "t3.micro"

  tags = {
    Name = "skynet-ops-service"
  }
}
