#!/bin/bash

set -eoux pipefail

# Variables
EMAIL="imyjer@gmail.com"

# List of subdomains to update
SUBDOMAINS=("dev.ianmyjer.com")

# Get the public IP
public_ip=$(http https://checkip.amazonaws.com)

# Loop through each subdomain
for subdomain in "${SUBDOMAINS[@]}"; do
  echo "Processing subdomain: $subdomain"

  # Get the DNS record ID for the subdomain
  dns_record_id=$(http GET "https://api.cloudflare.com/client/v4/zones/${ZONE_ID}/dns_records" \
    Content-Type:application/json \
    X-Auth-Email:"${EMAIL}" \
    Authorization:"Bearer ${TOKEN}" | \
    jq -r --arg SUBDOMAIN "$subdomain" '.result[] | select(.name == $SUBDOMAIN) | .id')

  if [ -z "$dns_record_id" ]; then
    echo "Error: No DNS record found for $subdomain"
    continue
  fi

  # Update the DNS record with the new public IP
  response=$(echo '{
    "content": "'"${public_ip}"'"
  }' | \
    http PATCH "https://api.cloudflare.com/client/v4/zones/${ZONE_ID}/dns_records/${dns_record_id}" \
    Content-Type:application/json \
    X-Auth-Email:"${EMAIL}" \
    Authorization:"Bearer ${TOKEN}")

  # Check if the update was successful
  if echo "$response" | grep -q '"success":true'; then
    echo "Successfully updated $subdomain to IP $public_ip"
  else
    echo "Failed to update $subdomain. Response: $response"
  fi
done
