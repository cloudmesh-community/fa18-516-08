# ETL and Comparing Performance  Across Cloud Platforms Using FaaS :hand:fa18-516-08

| Varun Joshi | vajoshi@iu.edu | Indiana University | hid: fa18-516-08 | github:
[:cloud:](https://github.com/cloudmesh-community/fa18-516-08/blob/master/project-paper/report.md)

---

Keywords: FaaS, ETL, ETL Performance

---

## Abstract

Extract, transform and load in simplest terms is extracting data from a source and then transforming that data into a desired format by applying business or formatting rules and then loading it in to a target for further processing or analysis.The goal of this project is to perform Extract Transform and Load (ETL) operations in cloud exploring Function As A Service. Serverless computing eliminates the overhead of provisioning and managing servers and scales automatically for performing tasks. As ETL can deal with huge sets of data, this project will explore FaaS for adhoc data queries which run ETL in the background. This project also attempts to evaluate FaaS offerings of major cloud providers namely AWS, Azure and Google Cloud against similar set of ETL tasks and operations. The end goal will be to compare side by side FaaS runtime statistics. The benchmark will be set by provisioning an EC2 instance and performing ETL without using FaaS.

## Introduction

This project attempts to evaluate ETL tasks and performance across AWS, Azure and GCP using FaaS. The project utilizes all three cloud platforms, Python runtime environment for FaaS, similar sized Linux instances for hosting MongoDb as the source Database and publicly available Twitter dataset for tweets during Hurricane Harvey. The Python function will extract data from MongoDb based on keywords and export the results in CSV which can be used for further processing.

## Design

1. Setup Linux Instance on Cloud platforms
2. Install MongoDb
3. Built FaaS on each Cloud Platform
4. Configure network security for FaaS to communicate with MongoDb
5. Use HTTP trigger for Keywords to call FaaS and generate CSV
6. Generate runtime statistics

## Architecture

## Dataset

## Implementation

## Benchmark

## Conclusion

## Acknowledgement
