from rest_framework_simplejwt.tokens import RefreshToken

def get_tokens_for_user(user):
    """
    Given a user instance, generate and return JWT refresh and access tokens.
    """
    refresh = RefreshToken.for_user(user)

    refresh['role'] = user.role
    refresh['email'] = user.email

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }