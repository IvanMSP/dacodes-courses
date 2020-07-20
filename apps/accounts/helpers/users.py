# Django Core

def get_username(email: str) -> str:
    """
        Function for get username from a email
    """
    username = email.split('@')
    return username[0]