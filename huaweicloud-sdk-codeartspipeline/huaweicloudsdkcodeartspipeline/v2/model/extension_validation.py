# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExtensionValidation:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'required_message': 'str',
        'regex': 'str',
        'regex_message': 'str',
        'max_length': 'int',
        'min_length': 'int'
    }

    attribute_map = {
        'required_message': 'required_message',
        'regex': 'regex',
        'regex_message': 'regex_message',
        'max_length': 'max_length',
        'min_length': 'min_length'
    }

    def __init__(self, required_message=None, regex=None, regex_message=None, max_length=None, min_length=None):
        """ExtensionValidation

        The model defined in huaweicloud sdk

        :param required_message: 消息
        :type required_message: str
        :param regex: 正则
        :type regex: str
        :param regex_message: 正则消息
        :type regex_message: str
        :param max_length: 最大长度
        :type max_length: int
        :param min_length: 最小长度
        :type min_length: int
        """
        
        

        self._required_message = None
        self._regex = None
        self._regex_message = None
        self._max_length = None
        self._min_length = None
        self.discriminator = None

        if required_message is not None:
            self.required_message = required_message
        if regex is not None:
            self.regex = regex
        if regex_message is not None:
            self.regex_message = regex_message
        if max_length is not None:
            self.max_length = max_length
        if min_length is not None:
            self.min_length = min_length

    @property
    def required_message(self):
        """Gets the required_message of this ExtensionValidation.

        消息

        :return: The required_message of this ExtensionValidation.
        :rtype: str
        """
        return self._required_message

    @required_message.setter
    def required_message(self, required_message):
        """Sets the required_message of this ExtensionValidation.

        消息

        :param required_message: The required_message of this ExtensionValidation.
        :type required_message: str
        """
        self._required_message = required_message

    @property
    def regex(self):
        """Gets the regex of this ExtensionValidation.

        正则

        :return: The regex of this ExtensionValidation.
        :rtype: str
        """
        return self._regex

    @regex.setter
    def regex(self, regex):
        """Sets the regex of this ExtensionValidation.

        正则

        :param regex: The regex of this ExtensionValidation.
        :type regex: str
        """
        self._regex = regex

    @property
    def regex_message(self):
        """Gets the regex_message of this ExtensionValidation.

        正则消息

        :return: The regex_message of this ExtensionValidation.
        :rtype: str
        """
        return self._regex_message

    @regex_message.setter
    def regex_message(self, regex_message):
        """Sets the regex_message of this ExtensionValidation.

        正则消息

        :param regex_message: The regex_message of this ExtensionValidation.
        :type regex_message: str
        """
        self._regex_message = regex_message

    @property
    def max_length(self):
        """Gets the max_length of this ExtensionValidation.

        最大长度

        :return: The max_length of this ExtensionValidation.
        :rtype: int
        """
        return self._max_length

    @max_length.setter
    def max_length(self, max_length):
        """Sets the max_length of this ExtensionValidation.

        最大长度

        :param max_length: The max_length of this ExtensionValidation.
        :type max_length: int
        """
        self._max_length = max_length

    @property
    def min_length(self):
        """Gets the min_length of this ExtensionValidation.

        最小长度

        :return: The min_length of this ExtensionValidation.
        :rtype: int
        """
        return self._min_length

    @min_length.setter
    def min_length(self, min_length):
        """Sets the min_length of this ExtensionValidation.

        最小长度

        :param min_length: The min_length of this ExtensionValidation.
        :type min_length: int
        """
        self._min_length = min_length

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
        """Returns the string representation of the model"""
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ExtensionValidation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
