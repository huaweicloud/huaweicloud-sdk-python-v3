# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PackageUsage:

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
        'used_percent': 'int'
    }

    attribute_map = {
        'name': 'name',
        'used_percent': 'used_percent'
    }

    def __init__(self, name=None, used_percent=None):
        r"""PackageUsage

        The model defined in huaweicloud sdk

        :param name: 套餐类型
        :type name: str
        :param used_percent: 套餐用量
        :type used_percent: int
        """
        
        

        self._name = None
        self._used_percent = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if used_percent is not None:
            self.used_percent = used_percent

    @property
    def name(self):
        r"""Gets the name of this PackageUsage.

        套餐类型

        :return: The name of this PackageUsage.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this PackageUsage.

        套餐类型

        :param name: The name of this PackageUsage.
        :type name: str
        """
        self._name = name

    @property
    def used_percent(self):
        r"""Gets the used_percent of this PackageUsage.

        套餐用量

        :return: The used_percent of this PackageUsage.
        :rtype: int
        """
        return self._used_percent

    @used_percent.setter
    def used_percent(self, used_percent):
        r"""Sets the used_percent of this PackageUsage.

        套餐用量

        :param used_percent: The used_percent of this PackageUsage.
        :type used_percent: int
        """
        self._used_percent = used_percent

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
        if not isinstance(other, PackageUsage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
