# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class County:

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
        'name': 'str'
    }

    attribute_map = {
        'code': 'code',
        'name': 'name'
    }

    def __init__(self, code=None, name=None):
        """County

        The model defined in huaweicloud sdk

        :param code: 区县的编码。
        :type code: str
        :param name: 区县的名称，根据请求的语言会传递回对应的语言的名称，目前仅支持中文。
        :type name: str
        """
        
        

        self._code = None
        self._name = None
        self.discriminator = None

        self.code = code
        self.name = name

    @property
    def code(self):
        """Gets the code of this County.

        区县的编码。

        :return: The code of this County.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this County.

        区县的编码。

        :param code: The code of this County.
        :type code: str
        """
        self._code = code

    @property
    def name(self):
        """Gets the name of this County.

        区县的名称，根据请求的语言会传递回对应的语言的名称，目前仅支持中文。

        :return: The name of this County.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this County.

        区县的名称，根据请求的语言会传递回对应的语言的名称，目前仅支持中文。

        :param name: The name of this County.
        :type name: str
        """
        self._name = name

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
        if not isinstance(other, County):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
