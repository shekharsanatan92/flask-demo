# Flask-demo
**Tech Stack**: _Python, Flask, AWS and Docker_

`This is a dockerized solution, hence can be used with any of the container orchestration tools like AWS EKS,ECS etc.`

This solution has two parts:

1. Display Instance Metadata `['Instance-Id', 'Subnet-Id', 'Hostname', 'Public-Ip', 'Private-Ip', 'AMI-Id']` in two formats (Horizontal and Vertical Tables)
2. Display EMR Metadata `['EMR_ID', 'Creation_Date', 'Elapsed_Time']` in tabular format

Steps to Run locally:
1. docker image build -t flask-demo
2. docker run -e AWS_ACCESS_KEY_ID=XXXXXXX -e AWS_SECRET_ACCESS_KEY=XXXXXXX -p 8080:8080 -d flask-demo
3. Access the application at http://localhost:8080 :+1: 
