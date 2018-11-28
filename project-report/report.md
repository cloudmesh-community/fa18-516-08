# Managing AWS Lambda Using REST API :hand:fa18-516-08

| Varun Joshi | vajoshi@iu.edu | Indiana University | hid: fa18-516-08 | github:
[:cloud:](https://github.com/cloudmesh-community/fa18-516-08/blob/master/project-paper/report.md)

**:mortar_board: Learning Objectives**

* Understand RESTful APIs and explore basic CRUD operations
* Apply REST understanding to Amazon's FaaS offering - AWS Lambda
* Learn AWS SDK for Python - boto3
* Use boto3 and Python Flask framework for building RESTful API with AWS Lambda as the resource

---

Keywords: FaaS, AWS Lambda,serverless,REST,OpenAPI example,Swagger

---


## Abstract

Amazon's Function as Service offering, AWS Lambda, provides serverless computing and eliminates the overhead of provisioning and managing servers.
AWS Lambda can also integrate with other AWS services like S3 and Dynamo DB, extending it's capabilities for building highly scalable applications. AWS Lambda can be triggered by other AWS resource events, HTTP endpoints, mobile applications etc. giving the flexibility for serverless computing. This project explores managing AWS Lambda by providing a solution for basic CRUD operations through REST API build using OpenAPI (Swagger 2.0) specification.

## Introduction

The goal of this project is to build a solution utilizing REST APIs to manage AWS Lambda service. The solution focuses on providing basic REST CRUD operations with AWS Lambda as resource. Python and Python flask framework is used for constructing REST service and AWS SDK for Python (boto3) is used for managing AWS Lambda.

## Architecture

The project is build of three components (see +@fig:Architecture).

* Swagger 2.0 is used for writing API specification.The specification describes endpoints for AWS Lambda CRUD operations and defines operation for each endpoint.
* Python flask framework consumes the OpenAPI specification and directs the endpoints to Python functions by building a RESTful app.
* AWS SDK for Python (boto3) is used to define Python functions which operate on endpoints and expose the resource, which is AWS Lambda , over REST API.

## Implementation

## Results

## Steps To Reproduce

## Conclusion

## Acknowledgement
