# ETL Using FaaS and Comparing Performance Across Cloud Platforms :hand:fa18-516-08

| Varun Joshi | vajoshi@iu.edu | Indiana University | hid: fa18-516-08 | github:
[:cloud:](https://github.com/cloudmesh-community/fa18-516-08/blob/master/project-paper/report.md)

---

Keywords: FaaS, ETL, ETL Performance

---

## Abstract

The goal of this project is to explore the FaaS for Extract Transform and Load (ETL) operations. Serverless computing eliminates the overhead of provisioning and managing servers. This project is also an attempt to evaluate FaaS offerings of major cloud providers namely AWS, Azure and Google Cloud against similar set of ETL tasks and operations. The end goal will be to compare side by side FaaS runtime statistics. The benchmark will be set by provisioning an EC2 instance and performing ETL without using FaaS.

## Introduction

This project attempts to evaluate ETL tasks and performance across AWS, Azure and GCP using FaaS. The project utilizes all three cloud platforms, Python runtime environment for FaaS, similar sized Linux instances for hosting MongoDb as the source Database and publicly available Twitter dataset for tweets during Hurricane Harvey. The Python function will extract data from MongoDb based on keywords and export the results in CSV which can be used for further processing.

## Design

. Setup Linux Instance on Cloud platforms
. Install MongoDb
. Built FaaS on each Cloud Platform
. Configure network security for FaaS to communicate with MongoDb
. Use HTTP trigger for Keywords to call FaaS and generate CSV
. Generate runtime statistics

## Architecture

## Dataset

## Implementation

## Benchmark

## Conclusion

## Acknowledgement
