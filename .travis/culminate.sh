#!/usr/bin/env sh
# Purge Web Caches

# purge CloudFlare caches
# https://api.cloudflare.com/#zone-purge-files-by-url
curl --silent \
  --show-error \
  --data "@.artifacts" \
  --write-out "\n" \
  --header "X-Auth-Email: ${CLOUDFLARE_USER}" \
  --header "X-Auth-Key: ${CLOUDFLARE_TOKEN}" \
  --header "Content-Type: application/json" \
  --url "https://api.cloudflare.com/client/v4/zones/${CLOUDFLARE_ZONE_ID}/purge_cache"
