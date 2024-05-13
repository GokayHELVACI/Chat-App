# How to run this application

### Step 1 Installing Docker
- sudo yum update -y
- sudo yum install -y docker
- sudo service docker start
- sudo usermod -a -G docker ec2-user
- docker ps

### Step 2 Building Docker Image and Run On EC2 Server

- Go to the Dockerfile's location:
     - docker build . -t <image_name>
     - docker run -p 80:80 <image_name>

### Step3 Opening The App
- Copy the EC2 instances public ip address and paste it into your web browser.