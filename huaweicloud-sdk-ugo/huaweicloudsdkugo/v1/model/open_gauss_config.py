# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpenGaussConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'permission_check_type': 'str'
    }

    attribute_map = {
        'permission_check_type': 'permission_check_type'
    }

    def __init__(self, permission_check_type=None):
        r"""OpenGaussConfig

        The model defined in huaweicloud sdk

        :param permission_check_type: 权限检查类型。
        :type permission_check_type: str
        """
        
        

        self._permission_check_type = None
        self.discriminator = None

        if permission_check_type is not None:
            self.permission_check_type = permission_check_type

    @property
    def permission_check_type(self):
        r"""Gets the permission_check_type of this OpenGaussConfig.

        权限检查类型。

        :return: The permission_check_type of this OpenGaussConfig.
        :rtype: str
        """
        return self._permission_check_type

    @permission_check_type.setter
    def permission_check_type(self, permission_check_type):
        r"""Sets the permission_check_type of this OpenGaussConfig.

        权限检查类型。

        :param permission_check_type: The permission_check_type of this OpenGaussConfig.
        :type permission_check_type: str
        """
        self._permission_check_type = permission_check_type

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
        if not isinstance(other, OpenGaussConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
