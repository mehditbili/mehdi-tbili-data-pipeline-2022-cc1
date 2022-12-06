resource "aws_instance" "ec2_vm" {
  ami           = "ami-02384a901b5df8024"
  instance_type = "t3.micro"
  key_name      = "mykey"
  tags = {
    Name = "selim.bouhassatine@etu.u-pec.fr"
    Owner = "selim_dev"
  }
  vpc_security_group_ids = ["${aws_security_group.default.id}"]
}

# Default ec2 user is "ec2-user"
