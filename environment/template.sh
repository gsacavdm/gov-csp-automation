#!/bin/bash

# Run this using "sourcing": 
# https://stackoverflow.com/questions/496702/can-a-shell-script-set-environment-variables-of-the-calling-shell
# COMMAND:
# . ./tmp/govhackfests_env.sh
export AUTHORITY="<MyTenant>.onmicrosoft.com"
export CLIENT_ID_PC="<ClientIDforPartnerCenter>"
export TENANT_HACKFEST="<TenantIDforHackfests>"
export INTERNAL_ACCOUNT_DOMAIN="@contoso.com"