# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Error:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'code': 'str',
        'details': 'list[object]',
        'reason': 'str',
        'url': 'str'
    }

    attribute_map = {
        'code': 'code',
        'details': 'details',
        'reason': 'reason',
        'url': 'url'
    }

    def __init__(self, code=None, details=None, reason=None, url=None):
        r"""Error

        The model defined in huaweicloud sdk

        :param code: 
        :type code: str
        :param details: 
        :type details: list[object]
        :param reason: 
        :type reason: str
        :param url: 
        :type url: str
        """
        
        

        self._code = None
        self._details = None
        self._reason = None
        self._url = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if details is not None:
            self.details = details
        if reason is not None:
            self.reason = reason
        if url is not None:
            self.url = url

    @property
    def code(self):
        r"""Gets the code of this Error.

        :return: The code of this Error.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this Error.

        :param code: The code of this Error.
        :type code: str
        """
        self._code = code

    @property
    def details(self):
        r"""Gets the details of this Error.

        :return: The details of this Error.
        :rtype: list[object]
        """
        return self._details

    @details.setter
    def details(self, details):
        r"""Sets the details of this Error.

        :param details: The details of this Error.
        :type details: list[object]
        """
        self._details = details

    @property
    def reason(self):
        r"""Gets the reason of this Error.

        :return: The reason of this Error.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        r"""Sets the reason of this Error.

        :param reason: The reason of this Error.
        :type reason: str
        """
        self._reason = reason

    @property
    def url(self):
        r"""Gets the url of this Error.

        :return: The url of this Error.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this Error.

        :param url: The url of this Error.
        :type url: str
        """
        self._url = url

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        import simplejson as json
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Error):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
