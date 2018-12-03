# Cloud and Data Privacy :smiley: fa18-516-08


| Varun Joshi
| vajoshi@iu.edu
| Indiana University
| hid: fa18-516-08
| github: [:cloud:](https://github.com/cloudmesh-community/fa18-516-08/blob/master/paper/paper.md)

**:mortar_board: Learning Objectives**

* Learn about data privacy in Cloud infrastructure
* European Union's General Data Protection Regulation and how it effects Cloud computing for data Privacy
* Learn about major cloud vendors data privacy readiness
* Shift in choice of cloud infrastructure with data privacy as priority

## Introduction

In this chapter we discuss the problem of data privacy in multitenant cloud infrastructure. The personal data of cloud users and data from businesses which deal in personal user data and use cloud technology, is stored and processed in cloud infrastructure. How this data is transferred between entities, how it is exposed to be used and retained, the policies for data purging and how users can control their personal data has become a mandatory policy decision for cloud vendors. With the advent of GDPR for European Union's personal data protection, the cloud computing usage for storing and processing personal user data is changing. Data privacy in general has become the driving decision for many businesses in choosing and opearting on cloud. In subsequent sections, we will learn about cloud data privacy in the wake of GDPR and how it effects businesses across the globe.

### GDPR Compliance

European Union's General Data Protection Regulation (GDPR) came in to
effect on May 25, 2018.

The core of the GDPR comliance is to protect EU citizens from privacy
and data breaches [@www-GDPRKeyChanges]. It aims to give back the
control of personal data to citizens and residents.

We may wonder that GDPR is applicable only for protecting EU citizens
and the organizations based outside of EU need not be GDPR compliant.
However, GDPR applies to any organization with business in EU and
collect,store and process data of EU citizens. With the digital age
and the organizations moving towards cloud computing, the GDPR brings
new challenges both for cloud computing vendors who have data centers
in EU as well as for organizations like Uber, Visa, Apple and many
more who are ubiquitous in their business models and deal with EU
citizens personal data.

[@www-GDPRDefinitions] lists personal data as defined in Article 4 of
GDPR:

> "*personal data* means any information relating to an identified or
> identifiable natural person (*data subject*); an identifiable
> natural person is one who can be identified, directly or indirectly,
> in particular by reference to an identifier such as a name, an
> identification number, location data, an online identifier or to one
> or more factors specific to the physical, physiological, genetic,
> mental, economic, cultural or social identity of that natural
> person;"

In simpler language it could be any information like identification
number (US equivalent for SSN),phone number, address, birth date, IP
address etc. which can uniquely identify a person.

GDPR compliance poses strict fines for any personal data breach. Fines
are either up to EUR 20 million or 4% of annual revenue, which ever
is higher.

To summarize, GDPR compliance will protect EU citizens personal data
and will enforce organizations worldwide to be GDPR compliant. Under
GDPR, it is mandatory for organizations to disclose how and when
personal data is collected and where it is stored, what it is used for
and how the data will be erased when the data subject is no longer
needed or chosses to opt out. Organizations need to explain in
simplest terms to the data subject about usage of their personal
information and give them option to opt out if they choose to do so.
In case of data hack, the data subjects should be notified immediately
when the hack happens.

In technical terms to be GDPR compliant, specifically for cloud
computing use case, cloud users and cloud providers will collectively
be responsible for encryption of data (both at rest and in transit),
should have ability to monitor the usage,authorized access control of
data, choose data storage - geolocation/type of storage/data access,
dedicated data protection officers and industry certifications for
data security. Privacy by design is now a legal obligation.

Now that we are familiar with the GDPR compliance, in next sections we
will look into it's impact specifically for cloud computing platform
and data privacy in cloud data centers. Before that, let's define Data
Processor and Data controller with respect to cloud and as related to
GDPR.


### Data Processor vs Data Controller

Cloud solutions like AWS, Azure, GCP are all considered data
processors because they offer resources and infrastructure to porcess
the data.

Organizations,authority or agency which collect and direct the
personal data and define mandate on how the collected personal data is
processed are known as data controllers.

For example an organization like Airbnb collects personal data of its
users and customers and controls the usage of the personal data like
how and where it is stored, how it is used - such as providing rental
suggestions or generating analytics on usage statistics. Airbnb uses
AWS as it's operation infrastructure. In this example AWS is data
controller where as AWS acts as data processor.

AWS also acts as data controller for the data it collects like user
account registration information of its customers, administration,
service access etc.

Collection, storage, recording, organizing, structuring, alteration,
consultation, retrieval, sharing, restriction and erasing and
destruction all come under personal data processing.

GDPR defines collective responsibility for both data processors and
data controllers for safeguarding personal data.

The defining of roles extends further if there is a third-party
involved between cloud solution vendors and cloud users. For example
if a company is using services of a third-party and the third-party is
using cloud solution vendors directly then the roles should be
understood clearly for being GDPR compliant and avoiding audit and
fines.

Now we have understood the difference between data processors and data
controllers, let's look in to its impact on cloud computing by
relating it to GDPR.

### Impact On Cloud Computing

GDPR imposes collective responsibility on data controllers and data
processors for personal data protection. Organizations or cloud users
who deal with the personal data of their customers or consumers of
their applications should be careful in choosing a cloud solution
which is GDPR compliant and provides infrastructure and services
options which are GDPR compliant. Data controllers should have options
to define data privacy and security operations within the cloud
infrastructure. Taking example of AWS as data processor, the resources
like EC2, EBS, Amazon VPC all offer operations mechanism for a data
controller to configure for robust data privacy and security. At the
same time, AWS as a data processor needs to disclose in its contract
with the data controller the options it provides for data storage and
region and site for each chosen services.

Since data protection is a collective responsibility and design by
principle, the data controller will have to keep the following check
list [@www-aws] when choosing a cloud solution provider:

* Options to configure resources and desired settings as related to
  the data Privacy
* Ability to get snapshot of the current configurations in cloud
* On demand retrieval of configurations
* Historical logging
* Ability to get automatically notified of any changes in configuration
* View how resources communicate in cloud infrastructure
* Ability of cloud provider to encrypt the data either in transit or rest
* Options to set data access controls - granular access to data, multi
  factor authentication, geo-restrictions on data access

In summary, data controllers should define and are responsible for
defining all data privacy and security rules when using a cloud
infrastructure and resources. Data processors are responsible for
providing resources and services to be GDPR compliant. If the
processing happens with a third-party, the information needs to be
disclosed and again the responsibility is collective.

Complexity the compliance may cause changes to how the cloud computing
infrastructure is used by the organizations. The debate would be
between private or public cloud for services which deal with the
personal data. Let's look more in detail in next section.


### Public or Private Cloud

The definition of Private and Public cloud as defined by NIST:

* Private cloud : The cloud infrastructure is operated solely for an organization. It may be
managed by the organization or a third party and may exist on premise or off
premise [@www-NIST]. The enterprise is solely
  responsible for managing and scaling the infrastructure as needed.
  Examples are AT&T, Cisco, T-Mobile have their own private cloud hosted
  in their own data centers.

* Public cloud : The cloud infrastructure is made available to the general public or a large
industry group and is owned by an organization selling cloud services [@www-NIST].
  The enterprises
  and
  their data are virtually separated in the data center and
  enterprises have their own virtual private cloud network (example
  Amazon VPC). The cloud provider is responsible for managing and
  scaling the infrastructure at the data center. The enterprises can
  choose to individually upgrade and update the resources for patching,
  security etc. Examples are AWS, GCP, Azure.

Based on the above concepts, there could be multiple iterations of the
cloud solution.

* Hybrid cloud is one such solution where there is a mix usage of on
  premise data center and public cloud data center. The use case could
  be based on mission critical applications, data privacy, need for on
  demand scalability, high availability etc.
  NIST defines hybrid cloud as :
  The cloud infrastructure is a composition of two or more clouds (private,community, or public) that remain unique entities but are bound together by standardized or proprietary technology that enables data and application portability (e.g., cloud bursting for load-balancing between clouds) [@www-NIST].
* Managed cloud services provides enterprise an option to outsource
  the management of the cloud infrastructure and services to a
  third-party company like Rackspace or Expedient. Again the managed
  cloud service option depends on the need of usage. Managed services
  can be leveraged on private cloud, public cloud or companies like
  Rackspace, Expedient provide their own data centers which can be
  dedicated completely to an enterprise for their infrastructure needs
  and managed by the providers. Rackspace, for example, uses Openstack
  software for their managed cloud services solution.

Now with the knowledge of above concepts, it's clear to define the
cloud strategy. Keeping in mind the requirements of GDPR compliance
and the responsibility of data controllers and data processors, a
cloud solution can be chosen which is secured, robust, optimized and
cost-effective.

Highly secured and sensitive data, for example HIPAA, can be managed
in a private cloud or hybrid cloud. Other sensitive personal data
which requires services of third-party for analytics generation like
movie recommendation apps, shopping recommendation, election surveys,
likes, social mining etc. can leverage public cloud scaling in a
virtual private network utilizing GDPR compliant cloud data processor
and rules and security defined by data controllers.

One important consideration is while using opensource solution like
Openstack. Openstack can be used in a managed cloud service setting or
independently for private cloud solution. The key is to use open
source resources and their configurations which provide robust data
security for compute, storage, network etc. which are integrated in
Openstack software[@www-openstack].

How GDPR and other data privacy compliances will shift the revenue
model of major cloud vendors will be an interesting trend to observer.
The trend will also relfect choice of enterprises for cloud solution
provider in their journey to achieve less overhead of maintaining data
centers, achieving scalability and at the same time protecting the
interests of data subjects.

### Common Vendors GDPR Readiness

Major cloud solution vendors like AWS, GCP and Azure are GDPR
compliant and offer resources, services and configurations which are
GDPR ready. Other vendors offering specifically SaaS and PaaS are also
GDPR compliant. Privacy statements of vendors has also been updated to
reflect their GDPR readiness. Refer the following for major vendors
GDPR readiness:

* AWS [@www-AWSGDPR]
* GCP [@www-GCPGDPR]
* Azure [@www-AzureGDPR]

Example of updated privacy policy in the wake of GDPR:

* Redhat [@www-RedHat]

Important takeaways from the RedHat privacy statement [@www-RedHat] is
that Redhat claims the following rights:

* The right to access your personal data;
* The right to rectify the personal data we hold about you;
* The right to erase your personal data;
* The right to restrict our use of your personal data;
* The right to object to our use of your personal data;
* The right to receive your personal data in a usable electronic
  format and transmit it to a third party (also known as the right of
  data portability); and
* The right to lodge a complaint with your local data protection authority;

Above privacy statement example shows how RedHat provides users with control and rights to access their data stored in cloud which RedHat collects through its website and any other website owned by RedHat. This is the direct effect of GDPR and mandating data privacy policy in general.

## Conclusion

With businesses moving their IT infrastructure to cloud and data privacy becoming a driving decision in choosing appropriate cloud strategy, the introduction of GDPR compliance is a benchmark to change the usage and selection of cloud computing solution. As more and more personal data is stored and processed in cloud, we may see new regulations or enhancemnet to existing ones improving data privacy and introducing more flexibility for cloud infrastructure.
