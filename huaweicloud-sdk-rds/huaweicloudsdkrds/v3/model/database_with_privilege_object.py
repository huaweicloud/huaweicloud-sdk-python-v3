# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DatabaseWithPrivilegeObject:

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
        'readonly': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'readonly': 'readonly'
    }

    def __init__(self, name=None, readonly=None):
        """DatabaseWithPrivilegeObject

        The model defined in huaweicloud sdk

        :param name: 已有数据库名称。
        :type name: str
        :param readonly: 是否为只读权限。
        :type readonly: bool
        """
        
        

        self._name = None
        self._readonly = None
        self.discriminator = None

        self.name = name
        if readonly is not None:
            self.readonly = readonly

    @property
    def name(self):
        """Gets the name of this DatabaseWithPrivilegeObject.

        已有数据库名称。

        :return: The name of this DatabaseWithPrivilegeObject.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DatabaseWithPrivilegeObject.

        已有数据库名称。

        :param name: The name of this DatabaseWithPrivilegeObject.
        :type name: str
        """
        self._name = name

    @property
    def readonly(self):
        """Gets the readonly of this DatabaseWithPrivilegeObject.

        是否为只读权限。

        :return: The readonly of this DatabaseWithPrivilegeObject.
        :rtype: bool
        """
        return self._readonly

    @readonly.setter
    def readonly(self, readonly):
        """Sets the readonly of this DatabaseWithPrivilegeObject.

        是否为只读权限。

        :param readonly: The readonly of this DatabaseWithPrivilegeObject.
        :type readonly: bool
        """
        self._readonly = readonly

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
        if not isinstance(other, DatabaseWithPrivilegeObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
