"""Monster class implementation."""


class Monster:
    """Monster class implementation."""

    def __init__(self, name, hp):
        """Construct Monster instance."""
        self.name = name
        self.hp = hp

    def __str__(self):
        """Get string representation of Monster object."""
        return '{} {} hp'.format(self.name, self.hp)
