import hmac
import hashlib

key = b'secret-key'
message = b'Important message'

# Create HMAC
hmac_digest = hmac.new(key, message, hashlib.sha256).hexdigest()
print(f"HMAC-SHA256: {hmac_digest}")

# Verify HMAC
received_hmac = hmac_digest
new_hmac = hmac.new(key, message, hashlib.sha256).hexdigest()
print(f"HMAC Verified: {hmac.compare_digest(received_hmac, new_hmac)}")
