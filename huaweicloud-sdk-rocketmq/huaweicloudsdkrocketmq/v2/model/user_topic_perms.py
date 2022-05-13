# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UserTopicPerms:

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
        'perm': 'str'
    }

    attribute_map = {
        'name': 'name',
        'perm': 'perm'
    }

    def __init__(self, name=None, perm=None):
        """UserTopicPerms

        The model defined in huaweicloud sdk

        :param name: 主题名称。
        :type name: str
        :param perm: 权限。
        :type perm: str
        """
        
        

        self._name = None
        self._perm = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if perm is not None:
            self.perm = perm

    @property
    def name(self):
        """Gets the name of this UserTopicPerms.

        主题名称。

        :return: The name of this UserTopicPerms.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UserTopicPerms.

        主题名称。

        :param name: The name of this UserTopicPerms.
        :type name: str
        """
        self._name = name

    @property
    def perm(self):
        """Gets the perm of this UserTopicPerms.

        权限。

        :return: The perm of this UserTopicPerms.
        :rtype: str
        """
        return self._perm

    @perm.setter
    def perm(self, perm):
        """Sets the perm of this UserTopicPerms.

        权限。

        :param perm: The perm of this UserTopicPerms.
        :type perm: str
        """
        self._perm = perm

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
        if not isinstance(other, UserTopicPerms):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
