from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six

class EmailVerifyTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, project, timestamp):
        return (
            six.text_type(project.pk) + 
            six.text_type(timestamp) + 
            six.text_type(project.status)
        )

email_verification_token = EmailVerifyTokenGenerator()