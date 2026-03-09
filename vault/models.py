from django.db import models
from django.contrib.auth.models import User
from cryptography.fernet import Fernet
from django.conf import settings
import base64
import hashlib

def get_cipher():
    key = hashlib.sha256(settings.SECRET_KEY.encode()).digest()
    return Fernet(base64.urlsafe_b64encode(key))

class VaultItem(models.Model):
    user             = models.ForeignKey(User, on_delete=models.CASCADE)
    title            = models.CharField(max_length=200)
    encrypted_username = models.TextField(blank=True, default='')
    encrypted_password = models.TextField(blank=True, default='')
    encrypted_notes    = models.TextField(blank=True, default='')
    created_at       = models.DateTimeField(auto_now_add=True)

    # --- username ---
    def set_username(self, raw):
        if raw:
            self.encrypted_username = get_cipher().encrypt(raw.encode()).decode()

    def get_username(self):
        if not self.encrypted_username:
            return ''
        return get_cipher().decrypt(self.encrypted_username.encode()).decode()

    # --- password ---
    def set_password(self, raw):
        if raw:
            self.encrypted_password = get_cipher().encrypt(raw.encode()).decode()

    def get_password(self):
        if not self.encrypted_password:
            return ''
        return get_cipher().decrypt(self.encrypted_password.encode()).decode()

    # --- notes ---
    def set_notes(self, raw):
        if raw:
            self.encrypted_notes = get_cipher().encrypt(raw.encode()).decode()

    def get_notes(self):
        if not self.encrypted_notes:
            return ''
        return get_cipher().decrypt(self.encrypted_notes.encode()).decode()

    def __str__(self):
        return self.title


class VaultFile(models.Model):
    ALLOWED_TYPES = [
        ('pdf', 'PDF'), ('doc', 'Word Doc'), ('xlsx', 'Excel'),
        ('jpg', 'Image'), ('png', 'Image'), ('mp4', 'Video'),
    ]
    vault_item  = models.ForeignKey(VaultItem, on_delete=models.CASCADE, related_name='files')
    file        = models.FileField(upload_to='vault_files/%Y/%m/')
    filename    = models.CharField(max_length=255)
    file_type   = models.CharField(max_length=10)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.filename} → {self.vault_item.title}"