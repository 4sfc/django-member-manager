"""MemberManagerUtils class"""

class MemberManagerUtils:
    """Helper functions for MemberManager"""

    @staticmethod
    def valid_period(start, end, hours, minutes):
        """
        Return True if start-end period is valid.

        :param start int: Start time in military time * 100
        :param end int: End time in military time * 100
        :param hours int: Valid hours
        :param minutes int: Valid minutes

        :return bool: Valid start-end period
        """
        period = hours * 100 + minutes
        return (end - start) >= period
