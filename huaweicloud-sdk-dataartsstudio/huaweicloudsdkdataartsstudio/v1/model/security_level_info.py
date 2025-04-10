# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SecurityLevelInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'level': 'str'
    }

    attribute_map = {
        'name': 'name',
        'level': 'level'
    }

    def __init__(self, name=None, level=None):
        r"""SecurityLevelInfo

        The model defined in huaweicloud sdk

        :param name: 密级名称
        :type name: str
        :param level: 密级等级
        :type level: str
        """
        
        

        self._name = None
        self._level = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if level is not None:
            self.level = level

    @property
    def name(self):
        r"""Gets the name of this SecurityLevelInfo.

        密级名称

        :return: The name of this SecurityLevelInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this SecurityLevelInfo.

        密级名称

        :param name: The name of this SecurityLevelInfo.
        :type name: str
        """
        self._name = name

    @property
    def level(self):
        r"""Gets the level of this SecurityLevelInfo.

        密级等级

        :return: The level of this SecurityLevelInfo.
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        r"""Sets the level of this SecurityLevelInfo.

        密级等级

        :param level: The level of this SecurityLevelInfo.
        :type level: str
        """
        self._level = level

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
        if not isinstance(other, SecurityLevelInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
