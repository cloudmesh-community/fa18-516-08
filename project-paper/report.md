# Text search utility using AWS Lambda exposed as REST :hand:fa18-516-08

| Varun Joshi | vajoshi@iu.edu | Indiana University | hid: fa18-516-08 | github:
[:cloud:](https://github.com/cloudmesh-community/fa18-516-08/blob/master/project-paper/report.md)

---

Keywords: FaaS, Lambda, search, text search, REST,OpenAPI example

---

## Abstract

Amazon's Function as Service offering, AWS Lambda, provides serverless computing and eliminates the overhead of provisioning and managing servers. Lambda scales automatically for performing high demanding compute tasks.
AWS Lambda can also integrate with other AWS services like S3 and Dynamo DB, extending it's capabilities for building high scale applications. Once such application could be a text search utility which searches for a specific user provided text  in a user provided file which is stored as an object in Amazon S3. The aim of this project is to build a text search utility application and provide users a simple REST service to view the search results.

## Introduction

The goal of this project is to build a search utility by invoking AWS Lambda function which reads a file object in Amazon S3 and directs the search results to a REST webservice. The project attempts to showcase the AWS Lambda, FaaS and REST learning and implementation for building a text search utility.

## Design

1. Setup AWS free tier account
2. Launch an EC2 instance
3. Install required tools for generating Swagger server side stub for building REST API
4. Import all Python packages required on EC2 - boto3 for invoking AWS Lambda Function
5. Create AWS S3 bucket and configure required permissions. Upload a test file required for demonstrating the project implementation.
6. Create IAM role for allowing Lambda to access S3
6. Create AWS Lambda function
7. Host REST API on EC2
8. Test the utility
9. Automate all tasks performed on AWS console


## Architecture

## Dataset

## Implementation

## Benchmark

## Conclusion

## Acknowledgement
