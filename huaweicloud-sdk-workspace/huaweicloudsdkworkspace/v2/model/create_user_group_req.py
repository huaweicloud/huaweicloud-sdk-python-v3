# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateUserGroupReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_name': 'str',
        'platform_type': 'str',
        'description': 'str'
    }

    attribute_map = {
        'group_name': 'group_name',
        'platform_type': 'platform_type',
        'description': 'description'
    }

    def __init__(self, group_name=None, platform_type=None, description=None):
        """CreateUserGroupReq

        The model defined in huaweicloud sdk

        :param group_name: 用户组名称。
        :type group_name: str
        :param platform_type: 用户组类型。 * AD： AD域用户组 * LOCAL： 本地liteAs用户组
        :type platform_type: str
        :param description: 用户组描述。
        :type description: str
        """
        
        

        self._group_name = None
        self._platform_type = None
        self._description = None
        self.discriminator = None

        self.group_name = group_name
        self.platform_type = platform_type
        if description is not None:
            self.description = description

    @property
    def group_name(self):
        """Gets the group_name of this CreateUserGroupReq.

        用户组名称。

        :return: The group_name of this CreateUserGroupReq.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this CreateUserGroupReq.

        用户组名称。

        :param group_name: The group_name of this CreateUserGroupReq.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def platform_type(self):
        """Gets the platform_type of this CreateUserGroupReq.

        用户组类型。 * AD： AD域用户组 * LOCAL： 本地liteAs用户组

        :return: The platform_type of this CreateUserGroupReq.
        :rtype: str
        """
        return self._platform_type

    @platform_type.setter
    def platform_type(self, platform_type):
        """Sets the platform_type of this CreateUserGroupReq.

        用户组类型。 * AD： AD域用户组 * LOCAL： 本地liteAs用户组

        :param platform_type: The platform_type of this CreateUserGroupReq.
        :type platform_type: str
        """
        self._platform_type = platform_type

    @property
    def description(self):
        """Gets the description of this CreateUserGroupReq.

        用户组描述。

        :return: The description of this CreateUserGroupReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateUserGroupReq.

        用户组描述。

        :param description: The description of this CreateUserGroupReq.
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
        if not isinstance(other, CreateUserGroupReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
