[comment]: # "Auto-generated SOAR connector documentation"
# DigiCert

Publisher: Splunk Community  
Connector Version: 1\.0\.1  
Product Vendor: DigiCert  
Product Name: DigiCert Services API  
Product Version Supported (regex): "\.\*"  
Minimum Product Version: 4\.9\.39220  

This app uses the DigiCert automation API to manage ssl certificates

[comment]: # " File: readme.md"
[comment]: # "  Copyright (c) 2021 Splunk Inc."
[comment]: # "  Licensed under Apache 2.0 (https://www.apache.org/licenses/LICENSE-2.0.txt)"
[comment]: # ""
DigiCert Services is the API that gives you flexibility to simplify certificate management in a way
that works best for your organization.


### Configuration Variables
The below configuration variables are required for this Connector to operate.  These variables are specified when configuring a DigiCert Services API asset in SOAR.

VARIABLE | REQUIRED | TYPE | DESCRIPTION
-------- | -------- | ---- | -----------
**base\_url** |  required  | string | API Base URL
**verify\_server\_cert** |  optional  | boolean | Verify Sever Certificate
**org\_id** |  required  | string | Organization ID
**api\_key** |  required  | password | API Key

### Supported Actions  
[test connectivity](#action-test-connectivity) - Validate the asset configuration for connectivity using supplied configuration  
[request cert](#action-request-cert) - Order a new SSL certificate  
[update request status](#action-update-request-status) - Update the status of a request \(i\.e\. approve the request\)  
[download cert](#action-download-cert) - Download a certificate to the vault  
[get request info](#action-get-request-info) - Get details for a certificate request  

## action: 'test connectivity'
Validate the asset configuration for connectivity using supplied configuration

Type: **test**  
Read only: **True**

#### Action Parameters
No parameters are required for this action

#### Action Output
No Output  

## action: 'request cert'
Order a new SSL certificate

Type: **generic**  
Read only: **False**

Order a new SSL certificate\. By default, some parameters are extracted from the csr, but can be overriden if needed\.

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**csr** |  required  | Vault\_id OR vault\_name of the certificate signing request \(csr\) | string |  `vault id` 
**common\_name** |  optional  | Certificate common name \(default\: extracted from csr\) | string | 
**signature\_hash** |  optional  | The certificate's signing algorithm hash \(default\: extracted from csr\) | string | 
**server\_platform** |  required  | Server platform this certificate is for | string | 
**order\_validity** |  required  | How long the order should be valid for \(in years, max 6\) | numeric | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.common\_name | string | 
action\_result\.parameter\.csr | string |  `vault id` 
action\_result\.parameter\.order\_validity | numeric | 
action\_result\.parameter\.server\_platform | numeric | 
action\_result\.parameter\.signature\_hash | string | 
action\_result\.data\.\*\.certificate\_id | numeric |  `digicert certificate id` 
action\_result\.data\.\*\.domains\.\*\.id | numeric | 
action\_result\.data\.\*\.domains\.\*\.name | string | 
action\_result\.data\.\*\.id | numeric |  `digicert order id` 
action\_result\.data\.\*\.requests\.\*\.id | numeric |  `digicert request id` 
action\_result\.data\.\*\.requests\.\*\.status | string | 
action\_result\.summary\.common\_name | string | 
action\_result\.summary\.order\_id | numeric |  `digicert order id` 
action\_result\.summary\.request\_id | numeric |  `digicert request id` 
action\_result\.summary\.request\_status | string | 
action\_result\.summary\.signature\_hash | string | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'update request status'
Update the status of a request \(i\.e\. approve the request\)

Type: **generic**  
Read only: **False**

Approve or reject a certificate request \(requires proper permissions\)\.

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**request\_id** |  required  | The request id of a certificate request to update | string |  `digicert request id` 
**status** |  required  | Status to set for the order | string | 
**comment** |  optional  | Add comment to the order request that we update \(optional\) | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.comment | string | 
action\_result\.parameter\.request\_id | string |  `digicert request id` 
action\_result\.parameter\.status | string | 
action\_result\.data | string | 
action\_result\.summary\.comment | string | 
action\_result\.summary\.request\_id | string |  `digicert request id` 
action\_result\.summary\.status | string | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'download cert'
Download a certificate to the vault

Type: **generic**  
Read only: **True**

Download certificate and save it to the vault\.

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**certificate\_id** |  optional  | The certificate id to download | string |  `digicert certificate id` 
**order\_id** |  optional  | The order id to download the certificate for | string |  `digicert order id` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.certificate\_id | string |  `digicert certificate id` 
action\_result\.parameter\.order\_id | string |  `digicert order id` 
action\_result\.data | string | 
action\_result\.summary\.vault\_id | string |  `vault id` 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'get request info'
Get details for a certificate request

Type: **generic**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**order\_id** |  required  | Certificate order id | string |  `digicert order id` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.parameter\.order\_id | string |  `digicert order id` 
action\_result\.data\.\*\.auto\_reissue | numeric | 
action\_result\.data\.\*\.auto\_renew | numeric | 
action\_result\.data\.\*\.certificate\.ca\_cert\.id | string | 
action\_result\.data\.\*\.certificate\.ca\_cert\.name | string | 
action\_result\.data\.\*\.certificate\.common\_name | string | 
action\_result\.data\.\*\.certificate\.csr | string | 
action\_result\.data\.\*\.certificate\.date\_created | string | 
action\_result\.data\.\*\.certificate\.dns\_names | string | 
action\_result\.data\.\*\.certificate\.id | numeric |  `digicert certificate id` 
action\_result\.data\.\*\.certificate\.key\_size | numeric | 
action\_result\.data\.\*\.certificate\.organization\.id | numeric | 
action\_result\.data\.\*\.certificate\.organization\_units | string | 
action\_result\.data\.\*\.certificate\.server\_platform\.csr\_url | string | 
action\_result\.data\.\*\.certificate\.server\_platform\.id | numeric | 
action\_result\.data\.\*\.certificate\.server\_platform\.install\_url | string | 
action\_result\.data\.\*\.certificate\.server\_platform\.name | string | 
action\_result\.data\.\*\.certificate\.signature\_hash | string | 
action\_result\.data\.\*\.container\.id | numeric | 
action\_result\.data\.\*\.container\.is\_active | boolean | 
action\_result\.data\.\*\.container\.name | string | 
action\_result\.data\.\*\.custom\_fields\.\*\.label | string | 
action\_result\.data\.\*\.custom\_fields\.\*\.metadata\_id | numeric | 
action\_result\.data\.\*\.custom\_fields\.\*\.value | string | 
action\_result\.data\.\*\.date\_created | string | 
action\_result\.data\.\*\.disable\_issuance\_email | boolean | 
action\_result\.data\.\*\.disable\_renewal\_notifications | boolean | 
action\_result\.data\.\*\.id | numeric |  `digicert order id` 
action\_result\.data\.\*\.is\_guest\_access\_enabled | boolean | 
action\_result\.data\.\*\.is\_out\_of\_contract | boolean | 
action\_result\.data\.\*\.is\_renewal | boolean | 
action\_result\.data\.\*\.organization\.assumed\_name | string | 
action\_result\.data\.\*\.organization\.city | string | 
action\_result\.data\.\*\.organization\.country | string | 
action\_result\.data\.\*\.organization\.display\_name | string | 
action\_result\.data\.\*\.organization\.id | numeric | 
action\_result\.data\.\*\.organization\.name | string | 
action\_result\.data\.\*\.organization\.state | string | 
action\_result\.data\.\*\.organization\_contact\.email | string | 
action\_result\.data\.\*\.organization\_contact\.first\_name | string | 
action\_result\.data\.\*\.organization\_contact\.job\_title | string | 
action\_result\.data\.\*\.organization\_contact\.last\_name | string | 
action\_result\.data\.\*\.organization\_contact\.telephone | string | 
action\_result\.data\.\*\.organization\_contact\.telephone\_extension | string | 
action\_result\.data\.\*\.payment\_method | string | 
action\_result\.data\.\*\.product\.csr\_required | boolean | 
action\_result\.data\.\*\.product\.name | string | 
action\_result\.data\.\*\.product\.name\_id | string | 
action\_result\.data\.\*\.product\.type | string | 
action\_result\.data\.\*\.product\.validation\_description | string | 
action\_result\.data\.\*\.product\.validation\_name | string | 
action\_result\.data\.\*\.product\.validation\_type | string | 
action\_result\.data\.\*\.product\_name\_id | string | 
action\_result\.data\.\*\.public\_id | string | 
action\_result\.data\.\*\.purchased\_dns\_names | numeric | 
action\_result\.data\.\*\.requests\.\*\.comments | string | 
action\_result\.data\.\*\.requests\.\*\.date | string | 
action\_result\.data\.\*\.requests\.\*\.id | numeric |  `digicert request id` 
action\_result\.data\.\*\.requests\.\*\.status | string | 
action\_result\.data\.\*\.requests\.\*\.type | string | 
action\_result\.data\.\*\.status | string | 
action\_result\.data\.\*\.technical\_contact\.email | string | 
action\_result\.data\.\*\.technical\_contact\.first\_name | string | 
action\_result\.data\.\*\.technical\_contact\.job\_title | string | 
action\_result\.data\.\*\.technical\_contact\.last\_name | string | 
action\_result\.data\.\*\.technical\_contact\.telephone | string | 
action\_result\.data\.\*\.technical\_contact\.telephone\_extension | string | 
action\_result\.data\.\*\.user\.email | string | 
action\_result\.data\.\*\.user\.first\_name | string | 
action\_result\.data\.\*\.user\.id | numeric | 
action\_result\.data\.\*\.user\.last\_name | string | 
action\_result\.data\.\*\.validity\_years | numeric | 
action\_result\.summary\.common\_name | string | 
action\_result\.summary\.order\_id | numeric |  `digicert order id` 
action\_result\.summary\.order\_status | string | 
action\_result\.message | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric | 