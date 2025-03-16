import requests
import datetime
import base64
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

class WebhookVerifier:
    def __init__(self,
                 public_key_url: str = "https://api.starcommunity.app/.well-known/webhooks.key",
                 expiry_seconds: int = 3600):
        self._public_key_url: str = public_key_url
        self._expiry_seconds: int = expiry_seconds
        self._public_key_pem: str = ''
        self._updated_at: datetime.datetime = datetime.datetime.now()

        self._update_key()

    def _should_update_key(self) -> bool:
        now = datetime.datetime.now()
        diff = now - self._updated_at
        seconds = diff.total_seconds()
        return seconds > self._expiry_seconds

    def _update_key(self):
        response = requests.get(self._public_key_url)
        response.raise_for_status()

        self._public_key_pem = response.text
        self._updated_at = datetime.datetime.now()


    def signature_valid(self, json_body: bytes, signature_header: str) -> bool:
        if self._should_update_key():
            self._update_key()

        # Get the public key
        public_key = RSA.import_key(self._public_key_pem)

        # Compute the SHA256 hash of the JSON body
        hashed_body = SHA256.new(json_body)

        try:
            # Decode the Base64 signature
            decoded_signature = base64.b64decode(signature_header)

            # Verify the signature
            pkcs1_15.new(public_key).verify(hashed_body, decoded_signature)
            return True
        except (ValueError, TypeError):
            return False
