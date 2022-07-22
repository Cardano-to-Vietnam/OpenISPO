from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six

class EmailVerifyTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, register, timestamp):
        return (
            six.text_type(register.pk) + 
            six.text_type(timestamp) + 
            six.text_type(register.status)
        )

email_verification_token = EmailVerifyTokenGenerator()