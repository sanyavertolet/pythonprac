"""Monster class implementation."""


class Monster:
    """Monster class implementation."""

    def __init__(self, name, hp):
        """Construct Monster instance.
        
        :param name: new monster's name
        :param hp: new monster's health points
        :type name: str
        :type hp: int
        :return: None
        :rtype: None
        """
        self.name = name
        self.hp = hp

    def __str__(self):
        """Get string representation of Monster object.

        :return: formatted string that shows monster info
        :rtype: str
        """
        return '{} {} hp'.format(self.name, self.hp)
