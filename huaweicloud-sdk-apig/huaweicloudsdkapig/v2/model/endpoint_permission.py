# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EndpointPermission:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'permission': 'str',
        'created_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'permission': 'permission',
        'created_at': 'created_at'
    }

    def __init__(self, id=None, permission=None, created_at=None):
        r"""EndpointPermission

        The model defined in huaweicloud sdk

        :param id: 记录编号
        :type id: str
        :param permission: 权限规则
        :type permission: str
        :param created_at: 创建时间
        :type created_at: datetime
        """
        
        

        self._id = None
        self._permission = None
        self._created_at = None
        self.discriminator = None

        self.id = id
        self.permission = permission
        self.created_at = created_at

    @property
    def id(self):
        r"""Gets the id of this EndpointPermission.

        记录编号

        :return: The id of this EndpointPermission.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this EndpointPermission.

        记录编号

        :param id: The id of this EndpointPermission.
        :type id: str
        """
        self._id = id

    @property
    def permission(self):
        r"""Gets the permission of this EndpointPermission.

        权限规则

        :return: The permission of this EndpointPermission.
        :rtype: str
        """
        return self._permission

    @permission.setter
    def permission(self, permission):
        r"""Sets the permission of this EndpointPermission.

        权限规则

        :param permission: The permission of this EndpointPermission.
        :type permission: str
        """
        self._permission = permission

    @property
    def created_at(self):
        r"""Gets the created_at of this EndpointPermission.

        创建时间

        :return: The created_at of this EndpointPermission.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this EndpointPermission.

        创建时间

        :param created_at: The created_at of this EndpointPermission.
        :type created_at: datetime
        """
        self._created_at = created_at

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
        if not isinstance(other, EndpointPermission):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
