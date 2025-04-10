# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProxyInfoFlavorInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_type': 'str',
        'code': 'str'
    }

    attribute_map = {
        'group_type': 'group_type',
        'code': 'code'
    }

    def __init__(self, group_type=None, code=None):
        r"""ProxyInfoFlavorInfo

        The model defined in huaweicloud sdk

        :param group_type: 规格类型。
        :type group_type: str
        :param code: 规格码。
        :type code: str
        """
        
        

        self._group_type = None
        self._code = None
        self.discriminator = None

        if group_type is not None:
            self.group_type = group_type
        if code is not None:
            self.code = code

    @property
    def group_type(self):
        r"""Gets the group_type of this ProxyInfoFlavorInfo.

        规格类型。

        :return: The group_type of this ProxyInfoFlavorInfo.
        :rtype: str
        """
        return self._group_type

    @group_type.setter
    def group_type(self, group_type):
        r"""Sets the group_type of this ProxyInfoFlavorInfo.

        规格类型。

        :param group_type: The group_type of this ProxyInfoFlavorInfo.
        :type group_type: str
        """
        self._group_type = group_type

    @property
    def code(self):
        r"""Gets the code of this ProxyInfoFlavorInfo.

        规格码。

        :return: The code of this ProxyInfoFlavorInfo.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this ProxyInfoFlavorInfo.

        规格码。

        :param code: The code of this ProxyInfoFlavorInfo.
        :type code: str
        """
        self._code = code

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
        if not isinstance(other, ProxyInfoFlavorInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
