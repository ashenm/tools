#!/usr/bin/env sh
# Purge Web Caches

# purge CloudFlare caches
# https://api.cloudflare.com/#zone-purge-files-by-url
for PAYLOAD in $(cat .artifacts | jq --compact-output '.files |  _nwise(30) | { files: . }'); do

  echo "$PAYLOAD" | jq '.'

  curl --silent --show-error \
    --data "$PAYLOAD" --write-out "\n" \
    --header "X-Auth-Email: ${CLOUDFLARE_USER}" \
    --header "X-Auth-Key: ${CLOUDFLARE_TOKEN}" \
    --header "Content-Type: application/json" \
    --url "https://api.cloudflare.com/client/v4/zones/${CLOUDFLARE_ZONE_ID}/purge_cache"

done
