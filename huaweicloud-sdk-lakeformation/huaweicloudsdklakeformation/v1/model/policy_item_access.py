# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PolicyItemAccess:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_allowed': 'bool',
        'type': 'str'
    }

    attribute_map = {
        'is_allowed': 'is_allowed',
        'type': 'type'
    }

    def __init__(self, is_allowed=None, type=None):
        """PolicyItemAccess

        The model defined in huaweicloud sdk

        :param is_allowed: 是否允许
        :type is_allowed: bool
        :param type: 类型
        :type type: str
        """
        
        

        self._is_allowed = None
        self._type = None
        self.discriminator = None

        if is_allowed is not None:
            self.is_allowed = is_allowed
        if type is not None:
            self.type = type

    @property
    def is_allowed(self):
        """Gets the is_allowed of this PolicyItemAccess.

        是否允许

        :return: The is_allowed of this PolicyItemAccess.
        :rtype: bool
        """
        return self._is_allowed

    @is_allowed.setter
    def is_allowed(self, is_allowed):
        """Sets the is_allowed of this PolicyItemAccess.

        是否允许

        :param is_allowed: The is_allowed of this PolicyItemAccess.
        :type is_allowed: bool
        """
        self._is_allowed = is_allowed

    @property
    def type(self):
        """Gets the type of this PolicyItemAccess.

        类型

        :return: The type of this PolicyItemAccess.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PolicyItemAccess.

        类型

        :param type: The type of this PolicyItemAccess.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, PolicyItemAccess):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
