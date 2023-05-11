# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RoleInput:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'role_name': 'str',
        'description': 'str'
    }

    attribute_map = {
        'role_name': 'role_name',
        'description': 'description'
    }

    def __init__(self, role_name=None, description=None):
        """RoleInput

        The model defined in huaweicloud sdk

        :param role_name: role名字
        :type role_name: str
        :param description: 描述信息
        :type description: str
        """
        
        

        self._role_name = None
        self._description = None
        self.discriminator = None

        self.role_name = role_name
        if description is not None:
            self.description = description

    @property
    def role_name(self):
        """Gets the role_name of this RoleInput.

        role名字

        :return: The role_name of this RoleInput.
        :rtype: str
        """
        return self._role_name

    @role_name.setter
    def role_name(self, role_name):
        """Sets the role_name of this RoleInput.

        role名字

        :param role_name: The role_name of this RoleInput.
        :type role_name: str
        """
        self._role_name = role_name

    @property
    def description(self):
        """Gets the description of this RoleInput.

        描述信息

        :return: The description of this RoleInput.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this RoleInput.

        描述信息

        :param description: The description of this RoleInput.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, RoleInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
