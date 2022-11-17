# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddProtectAccessLevel:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'push_access_level': 'int',
        'merge_access_level': 'int'
    }

    attribute_map = {
        'push_access_level': 'push_access_level',
        'merge_access_level': 'merge_access_level'
    }

    def __init__(self, push_access_level=None, merge_access_level=None):
        """AddProtectAccessLevel

        The model defined in huaweicloud sdk

        :param push_access_level: 提交权限 0:任何人不允许提交，30:开发者及管理员可提交，40:管理员可提交
        :type push_access_level: int
        :param merge_access_level: 合并权限 0:任何人不允许合并，30:开发者及管理员可合并，40:管理员可合并,合并权限必须大于等于提交权限
        :type merge_access_level: int
        """
        
        

        self._push_access_level = None
        self._merge_access_level = None
        self.discriminator = None

        self.push_access_level = push_access_level
        self.merge_access_level = merge_access_level

    @property
    def push_access_level(self):
        """Gets the push_access_level of this AddProtectAccessLevel.

        提交权限 0:任何人不允许提交，30:开发者及管理员可提交，40:管理员可提交

        :return: The push_access_level of this AddProtectAccessLevel.
        :rtype: int
        """
        return self._push_access_level

    @push_access_level.setter
    def push_access_level(self, push_access_level):
        """Sets the push_access_level of this AddProtectAccessLevel.

        提交权限 0:任何人不允许提交，30:开发者及管理员可提交，40:管理员可提交

        :param push_access_level: The push_access_level of this AddProtectAccessLevel.
        :type push_access_level: int
        """
        self._push_access_level = push_access_level

    @property
    def merge_access_level(self):
        """Gets the merge_access_level of this AddProtectAccessLevel.

        合并权限 0:任何人不允许合并，30:开发者及管理员可合并，40:管理员可合并,合并权限必须大于等于提交权限

        :return: The merge_access_level of this AddProtectAccessLevel.
        :rtype: int
        """
        return self._merge_access_level

    @merge_access_level.setter
    def merge_access_level(self, merge_access_level):
        """Sets the merge_access_level of this AddProtectAccessLevel.

        合并权限 0:任何人不允许合并，30:开发者及管理员可合并，40:管理员可合并,合并权限必须大于等于提交权限

        :param merge_access_level: The merge_access_level of this AddProtectAccessLevel.
        :type merge_access_level: int
        """
        self._merge_access_level = merge_access_level

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
        if not isinstance(other, AddProtectAccessLevel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
