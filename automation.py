"""Provides automation for the Azure Gov Team CSP tenant"""
# API Reference:
# https://docs.microsoft.com/en-us/partner-center/develop/partner-center-rest-resources
# https://msdn.microsoft.com/en-us/library/partnercenter/mt651644.aspx

import json
import os
import adal
import requests

def create_tenant(tenant_name, domain, owner_email):
    """Creates a tenant via the Partner Center API"""
    tenant = {
        "companyProfile": {
            "domain": domain + ".onmicrosoft.com",
        },
        "billingProfile": {
            "email": owner_email,
            "culture": "en-US",
            "language": "en",
            "companyName": tenant_name,
            "defaultAddress": {
                "country": "US",
                "city": "Redmond",
                "state": "WA",
                "addressLine1": "1 Microsoft Way",
                "postalCode": "98052",
                "firstName": "test",
                "lastName": "test"
            }
        }
    }

    response = pc_api("v1/customers", json.dumps(tenant))
    customer = response.json()
    return customer["companyProfile"]["tenantId"]

def create_subscription():
    """Creates a subscription via the Partner Center API"""
    return

def create_user():
    """Creates a user via the Azure AD Graph"""
    return

def create_resource_group():
    """Creates a resource group via the Azure Resource Manager API"""
    return

def assign_user_to_resource_group():
    """Assigns a user to a resource group via the Azure Resource Manager API"""
    return

def create_dod_policy():
    """Creates an ARM policy to prevent resource in DoD region via the Azure Resource Manager API"""
    return

def assign_pbi_licenses():
    """Assigns Power BI licenses to a user via the Azure AD Graph"""
    return

def create_spending_policy():
    """Creates an ARM policy to cap spending via the Azure Resource Manager API"""
    return

def get_token(resource, client_id):
    """Obtains an Azure AD token for the Partner Center API"""
    authority = "https://login.microsoftonline.us/" + AUTHORITY
    auth_context = adal.AuthenticationContext(authority)
    code = auth_context.acquire_user_code(resource, client_id)
    print code['message']
    token = auth_context.acquire_token_with_device_code(resource, code, client_id)
    return token["accessToken"]

def pc_api(api, data=None):
    """Sends a request to the Partner Center API. GET by default, POST if data is provided"""
    token = get_token("https://api.partnercenter.microsoft.com",
                      CLIENT_ID_PC)
    url = "https://api.partnercenter.microsoft.com/" + api
    headers = {
        "Authorization": "Bearer " + token,
        "Accept": "application/json"
    }

    if data != None:
        headers["Content-Type"] = "application/json"
        response = requests.post(url, data=data, headers=headers)
    else:
        response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise Exception("Unable to create tenant. Status code: "
                        + response.status_code + " | Reason: " + response.reason)
    return response

def setup_hackfest():
    """Sets up everything required for a Hackfest"""
#    tenant = TENANT_HACKFEST
#    subscription = create_subscription(tenant)
#    resource_group = create_resource_group(tenant, subscription)
#    user = create_user(tenant, subscription, resource_group)
#    assign_user_to_resource_group(user, subscription, resource_group)
#    create_dod_policy(subscription)
#    assign_pbi_license(tenant, user)

def setup_internal_account(user_alias):
    """Sets up everything required for a user to do dev/test/demos in Azure Gov"""
    print "Setting up internal account for " + user_alias
#    print "Creating tenant"
#    create_tenant(user_alias + " Gov Test Tenant",
#                  user_alias + 'gov', user_alias + INTERNAL_ACCOUNT_DOMAIN)
#    create_user()
    tenant = ""
    print "Creating subscription"
#    create_subscription(tenant)
#    create_dod_policy()
#    create_spending_policy()

print "Starting"
AUTHORITY = os.environ["AUTHORITY"]
CLIENT_ID_PC = os.environ["CLIENT_ID_PC"]
TENANT_HACKFEST = os.environ["TENANT_HACKFEST"]
INTERNAL_ACCOUNT_DOMAIN = os.environ["INTERNAL_ACCOUNT_DOMAIN"]

#setup_internal_account('someuser')
response = pc_api('v1/customers')
print json.dumps(response.text)
print "Done"
