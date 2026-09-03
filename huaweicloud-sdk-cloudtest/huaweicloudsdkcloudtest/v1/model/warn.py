# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Warn:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'warn_code': 'str',
        'warn_msg': 'str'
    }

    attribute_map = {
        'warn_code': 'warn_code',
        'warn_msg': 'warn_msg'
    }

    def __init__(self, warn_code=None, warn_msg=None):
        r"""Warn

        The model defined in huaweicloud sdk

        :param warn_code: 
        :type warn_code: str
        :param warn_msg: 
        :type warn_msg: str
        """
        
        

        self._warn_code = None
        self._warn_msg = None
        self.discriminator = None

        if warn_code is not None:
            self.warn_code = warn_code
        if warn_msg is not None:
            self.warn_msg = warn_msg

    @property
    def warn_code(self):
        r"""Gets the warn_code of this Warn.

        :return: The warn_code of this Warn.
        :rtype: str
        """
        return self._warn_code

    @warn_code.setter
    def warn_code(self, warn_code):
        r"""Sets the warn_code of this Warn.

        :param warn_code: The warn_code of this Warn.
        :type warn_code: str
        """
        self._warn_code = warn_code

    @property
    def warn_msg(self):
        r"""Gets the warn_msg of this Warn.

        :return: The warn_msg of this Warn.
        :rtype: str
        """
        return self._warn_msg

    @warn_msg.setter
    def warn_msg(self, warn_msg):
        r"""Sets the warn_msg of this Warn.

        :param warn_msg: The warn_msg of this Warn.
        :type warn_msg: str
        """
        self._warn_msg = warn_msg

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
        if not isinstance(other, Warn):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
