# coding: utf-8

import re
import six





class PremiumWafPoolOption:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'body_limit': 'int',
        'header_limit': 'int',
        'connect_timeout': 'int',
        'send_timeout': 'int',
        'read_timeout': 'int'
    }

    attribute_map = {
        'body_limit': 'body_limit',
        'header_limit': 'header_limit',
        'connect_timeout': 'connect_timeout',
        'send_timeout': 'send_timeout',
        'read_timeout': 'read_timeout'
    }

    def __init__(self, body_limit=None, header_limit=None, connect_timeout=None, send_timeout=None, read_timeout=None):
        """PremiumWafPoolOption - a model defined in huaweicloud sdk"""
        
        

        self._body_limit = None
        self._header_limit = None
        self._connect_timeout = None
        self._send_timeout = None
        self._read_timeout = None
        self.discriminator = None

        if body_limit is not None:
            self.body_limit = body_limit
        if header_limit is not None:
            self.header_limit = header_limit
        if connect_timeout is not None:
            self.connect_timeout = connect_timeout
        if send_timeout is not None:
            self.send_timeout = send_timeout
        if read_timeout is not None:
            self.read_timeout = read_timeout

    @property
    def body_limit(self):
        """Gets the body_limit of this PremiumWafPoolOption.

        body限制值

        :return: The body_limit of this PremiumWafPoolOption.
        :rtype: int
        """
        return self._body_limit

    @body_limit.setter
    def body_limit(self, body_limit):
        """Sets the body_limit of this PremiumWafPoolOption.

        body限制值

        :param body_limit: The body_limit of this PremiumWafPoolOption.
        :type: int
        """
        self._body_limit = body_limit

    @property
    def header_limit(self):
        """Gets the header_limit of this PremiumWafPoolOption.

        header限制值

        :return: The header_limit of this PremiumWafPoolOption.
        :rtype: int
        """
        return self._header_limit

    @header_limit.setter
    def header_limit(self, header_limit):
        """Sets the header_limit of this PremiumWafPoolOption.

        header限制值

        :param header_limit: The header_limit of this PremiumWafPoolOption.
        :type: int
        """
        self._header_limit = header_limit

    @property
    def connect_timeout(self):
        """Gets the connect_timeout of this PremiumWafPoolOption.

        连接超时配置

        :return: The connect_timeout of this PremiumWafPoolOption.
        :rtype: int
        """
        return self._connect_timeout

    @connect_timeout.setter
    def connect_timeout(self, connect_timeout):
        """Sets the connect_timeout of this PremiumWafPoolOption.

        连接超时配置

        :param connect_timeout: The connect_timeout of this PremiumWafPoolOption.
        :type: int
        """
        self._connect_timeout = connect_timeout

    @property
    def send_timeout(self):
        """Gets the send_timeout of this PremiumWafPoolOption.

        发送超时配置

        :return: The send_timeout of this PremiumWafPoolOption.
        :rtype: int
        """
        return self._send_timeout

    @send_timeout.setter
    def send_timeout(self, send_timeout):
        """Sets the send_timeout of this PremiumWafPoolOption.

        发送超时配置

        :param send_timeout: The send_timeout of this PremiumWafPoolOption.
        :type: int
        """
        self._send_timeout = send_timeout

    @property
    def read_timeout(self):
        """Gets the read_timeout of this PremiumWafPoolOption.

        接收超时配置

        :return: The read_timeout of this PremiumWafPoolOption.
        :rtype: int
        """
        return self._read_timeout

    @read_timeout.setter
    def read_timeout(self, read_timeout):
        """Sets the read_timeout of this PremiumWafPoolOption.

        接收超时配置

        :param read_timeout: The read_timeout of this PremiumWafPoolOption.
        :type: int
        """
        self._read_timeout = read_timeout

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        import simplejson as json
        return json.dumps(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PremiumWafPoolOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
