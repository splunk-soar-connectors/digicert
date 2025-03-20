# DigiCert

Publisher: Splunk Community \
Connector Version: 1.0.2 \
Product Vendor: DigiCert \
Product Name: DigiCert Services API \
Minimum Product Version: 5.1.0

This app uses the DigiCert automation API to manage ssl certificates

### Configuration variables

This table lists the configuration variables required to operate DigiCert. These variables are specified when configuring a DigiCert Services API asset in Splunk SOAR.

VARIABLE | REQUIRED | TYPE | DESCRIPTION
-------- | -------- | ---- | -----------
**base_url** | required | string | API Base URL |
**verify_server_cert** | optional | boolean | Verify Sever Certificate |
**org_id** | required | string | Organization ID |
**api_key** | required | password | API Key |

### Supported Actions

[test connectivity](#action-test-connectivity) - Validate the asset configuration for connectivity using supplied configuration \
[request cert](#action-request-cert) - Order a new SSL certificate \
[update request status](#action-update-request-status) - Update the status of a request (i.e. approve the request) \
[download cert](#action-download-cert) - Download a certificate to the vault \
[get request info](#action-get-request-info) - Get details for a certificate request

## action: 'test connectivity'

Validate the asset configuration for connectivity using supplied configuration

Type: **test** \
Read only: **True**

#### Action Parameters

No parameters are required for this action

#### Action Output

No Output

## action: 'request cert'

Order a new SSL certificate

Type: **generic** \
Read only: **False**

Order a new SSL certificate. By default, some parameters are extracted from the csr, but can be overriden if needed.

#### Action Parameters

PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**csr** | required | Vault_id OR vault_name of the certificate signing request (csr) | string | `vault id` |
**common_name** | optional | Certificate common name (default: extracted from csr) | string | |
**signature_hash** | optional | The certificate's signing algorithm hash (default: extracted from csr) | string | |
**server_platform** | required | Server platform this certificate is for | string | |
**order_validity** | required | How long the order should be valid for (in years, max 6) | numeric | |

#### Action Output

DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.status | string | | success failed |
action_result.parameter.common_name | string | | |
action_result.parameter.csr | string | `vault id` | |
action_result.parameter.order_validity | numeric | | |
action_result.parameter.server_platform | numeric | | |
action_result.parameter.signature_hash | string | | |
action_result.data.\*.certificate_id | numeric | `digicert certificate id` | |
action_result.data.\*.domains.\*.id | numeric | | |
action_result.data.\*.domains.\*.name | string | | |
action_result.data.\*.id | numeric | `digicert order id` | |
action_result.data.\*.requests.\*.id | numeric | `digicert request id` | |
action_result.data.\*.requests.\*.status | string | | |
action_result.summary.common_name | string | | |
action_result.summary.order_id | numeric | `digicert order id` | |
action_result.summary.request_id | numeric | `digicert request id` | |
action_result.summary.request_status | string | | |
action_result.summary.signature_hash | string | | |
action_result.message | string | | |
summary.total_objects | numeric | | |
summary.total_objects_successful | numeric | | |

## action: 'update request status'

Update the status of a request (i.e. approve the request)

Type: **generic** \
Read only: **False**

Approve or reject a certificate request (requires proper permissions).

#### Action Parameters

PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**request_id** | required | The request id of a certificate request to update | string | `digicert request id` |
**status** | required | Status to set for the order | string | |
**comment** | optional | Add comment to the order request that we update (optional) | string | |

#### Action Output

DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.status | string | | success failed |
action_result.parameter.comment | string | | |
action_result.parameter.request_id | string | `digicert request id` | |
action_result.parameter.status | string | | |
action_result.data | string | | |
action_result.summary.comment | string | | |
action_result.summary.request_id | string | `digicert request id` | |
action_result.summary.status | string | | |
action_result.message | string | | |
summary.total_objects | numeric | | |
summary.total_objects_successful | numeric | | |

## action: 'download cert'

Download a certificate to the vault

Type: **generic** \
Read only: **True**

Download certificate and save it to the vault.

#### Action Parameters

PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**certificate_id** | optional | The certificate id to download | string | `digicert certificate id` |
**order_id** | optional | The order id to download the certificate for | string | `digicert order id` |

#### Action Output

DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.status | string | | success failed |
action_result.parameter.certificate_id | string | `digicert certificate id` | |
action_result.parameter.order_id | string | `digicert order id` | |
action_result.data | string | | |
action_result.summary.vault_id | string | `vault id` | |
action_result.message | string | | |
summary.total_objects | numeric | | |
summary.total_objects_successful | numeric | | |

## action: 'get request info'

Get details for a certificate request

Type: **generic** \
Read only: **True**

#### Action Parameters

PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**order_id** | required | Certificate order id | string | `digicert order id` |

#### Action Output

DATA PATH | TYPE | CONTAINS | EXAMPLE VALUES
--------- | ---- | -------- | --------------
action_result.status | string | | success failed |
action_result.parameter.order_id | string | `digicert order id` | |
action_result.data.\*.auto_reissue | numeric | | |
action_result.data.\*.auto_renew | numeric | | |
action_result.data.\*.certificate.ca_cert.id | string | | |
action_result.data.\*.certificate.ca_cert.name | string | | |
action_result.data.\*.certificate.common_name | string | | |
action_result.data.\*.certificate.csr | string | | |
action_result.data.\*.certificate.date_created | string | | |
action_result.data.\*.certificate.dns_names | string | | |
action_result.data.\*.certificate.id | numeric | `digicert certificate id` | |
action_result.data.\*.certificate.key_size | numeric | | |
action_result.data.\*.certificate.organization.id | numeric | | |
action_result.data.\*.certificate.organization_units | string | | |
action_result.data.\*.certificate.server_platform.csr_url | string | | |
action_result.data.\*.certificate.server_platform.id | numeric | | |
action_result.data.\*.certificate.server_platform.install_url | string | | |
action_result.data.\*.certificate.server_platform.name | string | | |
action_result.data.\*.certificate.signature_hash | string | | |
action_result.data.\*.container.id | numeric | | |
action_result.data.\*.container.is_active | boolean | | |
action_result.data.\*.container.name | string | | |
action_result.data.\*.custom_fields.\*.label | string | | |
action_result.data.\*.custom_fields.\*.metadata_id | numeric | | |
action_result.data.\*.custom_fields.\*.value | string | | |
action_result.data.\*.date_created | string | | |
action_result.data.\*.disable_issuance_email | boolean | | |
action_result.data.\*.disable_renewal_notifications | boolean | | |
action_result.data.\*.id | numeric | `digicert order id` | |
action_result.data.\*.is_guest_access_enabled | boolean | | |
action_result.data.\*.is_out_of_contract | boolean | | |
action_result.data.\*.is_renewal | boolean | | |
action_result.data.\*.organization.assumed_name | string | | |
action_result.data.\*.organization.city | string | | |
action_result.data.\*.organization.country | string | | |
action_result.data.\*.organization.display_name | string | | |
action_result.data.\*.organization.id | numeric | | |
action_result.data.\*.organization.name | string | | |
action_result.data.\*.organization.state | string | | |
action_result.data.\*.organization_contact.email | string | | |
action_result.data.\*.organization_contact.first_name | string | | |
action_result.data.\*.organization_contact.job_title | string | | |
action_result.data.\*.organization_contact.last_name | string | | |
action_result.data.\*.organization_contact.telephone | string | | |
action_result.data.\*.organization_contact.telephone_extension | string | | |
action_result.data.\*.payment_method | string | | |
action_result.data.\*.product.csr_required | boolean | | |
action_result.data.\*.product.name | string | | |
action_result.data.\*.product.name_id | string | | |
action_result.data.\*.product.type | string | | |
action_result.data.\*.product.validation_description | string | | |
action_result.data.\*.product.validation_name | string | | |
action_result.data.\*.product.validation_type | string | | |
action_result.data.\*.product_name_id | string | | |
action_result.data.\*.public_id | string | | |
action_result.data.\*.purchased_dns_names | numeric | | |
action_result.data.\*.requests.\*.comments | string | | |
action_result.data.\*.requests.\*.date | string | | |
action_result.data.\*.requests.\*.id | numeric | `digicert request id` | |
action_result.data.\*.requests.\*.status | string | | |
action_result.data.\*.requests.\*.type | string | | |
action_result.data.\*.status | string | | |
action_result.data.\*.technical_contact.email | string | | |
action_result.data.\*.technical_contact.first_name | string | | |
action_result.data.\*.technical_contact.job_title | string | | |
action_result.data.\*.technical_contact.last_name | string | | |
action_result.data.\*.technical_contact.telephone | string | | |
action_result.data.\*.technical_contact.telephone_extension | string | | |
action_result.data.\*.user.email | string | | |
action_result.data.\*.user.first_name | string | | |
action_result.data.\*.user.id | numeric | | |
action_result.data.\*.user.last_name | string | | |
action_result.data.\*.validity_years | numeric | | |
action_result.summary.common_name | string | | |
action_result.summary.order_id | numeric | `digicert order id` | |
action_result.summary.order_status | string | | |
action_result.message | string | | |
summary.total_objects | numeric | | |
summary.total_objects_successful | numeric | | |

______________________________________________________________________

Auto-generated Splunk SOAR Connector documentation.

Copyright 2025 Splunk Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations under the License.
