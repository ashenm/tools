#!/usr/bin/env sh
# Purge Web Caches

# list artifacts for cache purging
find _site -type f -printf 'https://tools.ashenm.ml/%P\n' \
  | jq --raw-input --slurp 'split("\n") | { files: .[:-1] }' \
  | tee '.artifacts'

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
