# flask-demo
Python,Flask, AWS &amp; Docker

This is a dockerized solution, hence can be used with any of the container orchestration tools like AWS EKS,ECS etc.

This solution has two parts:

+ Display Instance Metadata ['Instance-Id', 'Subnet-Id', 'Hostname', 'Public-Ip', 'Private-Ip', 'AMI-Id'] in two formats (Horizontal and Vertical Tables)
+ Display EMR Metadata ['EMR_ID', 'Creation_Date', 'Elapsed_Time'] in tabular format

Steps to Run locally:
    Run following commands in order
        + docker image build -t flask-demo
        + docker run -e AWS_ACCESS_KEY_ID=XXXXXXX -e AWS_SECRET_ACCESS_KEY=XXXXXXX -p 8080:8080 -d flask-demo
        + Access the application at http://localhost:8080