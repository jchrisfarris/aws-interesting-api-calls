# aws-interesting-api-calls
Inventory of AWS API Calls of Significance to Security 

This repository contains a yaml file that documents the AWS API calls that have some significance from a security standpoint. The file is intended to be human and machine readable.

Also included is a python library for parsing the file.

# Organization
The Calls are grouped by AWS Service, and should be sorted alphabetically. 
Under each API Call are attributes about it such as a description, link to AWS Documentation about the call and a Category, Severity and Risk

## Categories
The Categories for the calls are broken down into
* Compliance - Specific actions you might not want everyone taking. These include RI Purchases and MarketPlace EULA acceptance
* Audit - Actions related to the audit trail of your account. Think CloudTrail
* NetworkSecurity - VPC Related Actions
* HostSecurity - Actions related to the security of a specific EC2 Instance
* IdentityManagement - Actions related to IAM Management
* AccessControl - Actions related to EC2 KeyPairs 
* AccountManagement - Actions related to the management of the AWS Account. Organizations and global account settings fall into this category

## Severities
The Severities are
* critical - Actions that are super powerful and very rare. These shouldn't be used often.
* high - Actions that pose a risk to your enterprise security if mis-used. They're used more often than critical actions, but should be limited to a small group of trusted AWS Experts
* medium - Actions that are interesting, but maybe not wake-me-up-at-3am interesting
* low - Actions that are significant from a security standpoint. Some might be low-risk but rare, others might be very common and pose a risk in combination with other calls.

## Risk Types
This is an attempt to categorize the risks posed by the API Call. Risks currently documented are:
* FinancialControl - Risk to your financial controls if this API Call is mis-used
* LegalControl - Risk to your legal controls if this API Call is mis-used
* EvidenceDestruction - API Calls that could allow an attacker to destroy evidence or alter your audit trail
* NetworkSegmentationViolation - API Calls that could violate your network segmentation architecture. Might be bridging VPCs that should be isolated, or connecting AWS to on-prem networks. 
* NetworkExposure - Calls that could expose an EC2 Instance to networks it should be exposed to
* Idunno.
* AccountTakeOver - Calls that could allow an attacker to take control of your account. These risks were introduced via the AWS Organizations product launch
* DataLossPrevention - API Calls that could impact your DLP Architecture. 
* PrivilegeEscalation - API Calls that could allow an attacker to gain more privileges into your system than they should have
* NetworkAccessCircumvention - Merge with NetworkExposure
* PolicyCircumvention - Calls that could alter your AWS account to no longer be in compliance with company policies





# Contributions
My hope to to make this list a crowd-sourced effort and be useful to other organizations. Feel free to fork and use in your own policies and automations. If you see something I missed, fork and send me a pull request.

# Author
Chris Farris - chris@room17.com - http://www.chrisfarris.com
