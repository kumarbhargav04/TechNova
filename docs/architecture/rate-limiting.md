# API Rate Limiting Architecture

## Algorithm
Token bucket algorithm implemented at reverse-proxy and middleware layer.

## Tier Limits
- Anonymous: 30 requests / minute.
- Standard User: 120 requests / minute.
- Verified Enterprise Agent: 1,000 requests / minute.
