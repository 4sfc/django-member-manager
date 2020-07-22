'''MemberManagerUtils class'''

class MemberManagerUtils:
    '''Helper functions for MemberManager'''

    @staticmethod
    def valid_period(start, end, hours, minutes):
        '''Return True if end - start >= hours + minutes'''
        period = hours * 100 + minutes
        return (end - start) >= period
