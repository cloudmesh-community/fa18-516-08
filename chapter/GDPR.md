# GDPR Compliance and Cloud Computing :hand: fa18-516-08

| Varun Joshi
| vajoshi@iu.edu
| Indiana University
| hid: fa18-516-08
| github: [:cloud:](https://github.com/cloudmesh-community/fa18-516-08/blob/master/chapter/GDPR.md)

# Introduction
European Union's General Data Protection Regulation (GDPR) came in to effect on May 25, 2018. In this chapter we will cover the general guidelines of GDPR in relation to cloud computing and how it applies to the businesses inside and outside Europen Union. We will touch upon the terms data processor and data controllers for cloud computing as related to GDPR compliance. We will also cover GDPR readiness and privacy statements of some common cloud vendors like Amazon, Microsoft and Google. We will also present geenral market outlook in the wake of GDPR for preference of public vs private cloud and finally talk about the open source platform Openstack and how community contribution can be GDPR compliant.

# GDPR Compliance
The core of the GDPR comliance is to protect EU citizens from privacy and data breaches ("GDPR Key Challenges",https://eugdpr.org/the-regulation/).
We may wonder that GDPR is applicable only for the protection of EU citizens and the organizations based outside of EU do not need to be GDPR compliant. However, GDPR is applicable to any organization with business in EU and collect,store and process data of EU citizens. With the digital age and the organizations moving towards cloud computing, the GDPR brings new challenges both for cloud computing vendors who have data centers in EU as well as for organizations like Uber, Visa, Apple and many more who are ubiquitous in their business models and deal with EU citizens personal data.
https://gdpr-info.eu/art-4-gdpr/  lists personal data as defined in Article 4 of GDPR - "‘personal data’ means any information relating to an identified or identifiable natural person (‘data subject’); an identifiable natural person is one who can be identified, directly or indirectly, in particular by reference to an identifier such as a name, an identification number, location data, an online identifier or to one or more factors specific to the physical, physiological, genetic, mental, economic, cultural or social identity of that natural person;" In simpler language it could be any information like identification number (US equivalent for SSN),phone number, address, birth date, IP address etc. which can uniquely identify a person.
GDPR compliance poses strict fines for any personal data breach. Fines are either upto EUR 20 million or 4 % of annual revenue, which ever is higher.
To summarize, GDPR compliance will protect EU citizens personal data and will enforce organizations worldwide to be GDPR compliant. Under GDPR, it is mandatory for organizations to disclose how and when personal data is collected and where it is stored, what it is used for and how the data will be erased when the data subject is no longer needed or chosses to opt out. Organizations need to explain in simplest terms to the data subject about usage of their personal information and give them option to opt out if they choose to do so. In case of data hack, the data subjects should be notified immediately when the hack happens.
In technical terms to be GDPR compliant, specifically for cloud computing use case, cloud users and cloud providers will collectively be responsible for encryption of data (both at rest and in transit), should have ability to monitor the usage,authorized access control of data, choose data storage - geolocation/type of storage/data access, dedicated data protection officers and industry certifications for data security. Privacy by design is now a legal obligation.
Now that we are familiar with the GDPR compliance, in next sections we will look into it's impact specifically for cloud computing platform and data privacy in cloud data centers. Before that, let's define Data Processor and Data controller with respect to cloud and as related to GDPR.

# Data Processor vs Data Controller
Cloud solutions like AWS, Azure, GCP are all considered data processors because they provide resources and infrastructure to porcess the data.
Organizations which collect and direct the personal data and define mandate on how the collected personal data will be processed are known as data controllers.
For example an organization like Airbnb collects personal data of it's users and customers and controls the usage of the personal data like how and where it will be stored, how it will be used - for example providing rental suggestions or generating analytics on usage statistics. Airbnb uses AWS as it's operation infrastructure. In this example AWS is data controller where as AWS acts as data processor.
AWS also acts as data controller for the data it collects like user account registration information of it's customers, administration, service access etc.
GDPR defines collective responsibility for both data processors and data controllers for safeguarding personal data.

# Impact On Cloud Computing

# Public or Private Cloud

# Common Vendors GDPR Readiness

# References
* https://eugdpr.org/the-regulation/
* https://gdpr-info.eu/art-4-gdpr/
* https://www.cloudsigma.com/gdpr-and-cloud-computing-challenges-and-opportunities/
* https://aws.amazon.com/compliance/gdpr-center/
* https://www.zdnet.com/article/gdpr-an-executive-guide-to-what-you-need-to-know/
