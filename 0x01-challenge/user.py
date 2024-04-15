#!/usr/bin/python3
"""
User class
"""

class User:
    """ Represents a user with an email address. """

    def __init__(self):
        """ Initializes a user with no email set. """
        self.__email = None

    @property
    def email(self):
        """ Returns the user's email address. """
        return self.__email

    @email.setter
    def email(self, value):
        """ Sets the user's email address.

        Args:
            value: The new email address (must be a string).

        Raises:
            TypeError: If the provided value is not a string.
        """
        if not isinstance(value, str):
            raise TypeError("email must be a string")
        self.__email = value

if __name__ == "__main__":
    u = User()
    u.email = "john@snow.com"
    print(u.email)
