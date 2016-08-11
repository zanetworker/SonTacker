__author__ = 'zanetworker'


class SonatackerException(Exception):
    """
    This is a custom ViperPy Exception class to better handle
    errors that ViPR can return in HTML format rather than JSON
    """

    def __init__(self, message=None, http_status_code=None, error_message=None):
        """
        This is a custom ViperPy Exception class to handle

        :param message: A custom
        :param http_status_code:
        :param vipr_message:
        :return:
        """
        if message is None:
            self.message = 'The Tacker endpoint has thrown an error, check ' \
                           'the http_status_code and Tacker attributes ' \
                           'of this exception for more details.'
        else:
            self.message = message

        self.http_status_code = http_status_code
        self.error_message = error_message

        super(SonatackerException, self).__init__(message, http_status_code, error_message)
