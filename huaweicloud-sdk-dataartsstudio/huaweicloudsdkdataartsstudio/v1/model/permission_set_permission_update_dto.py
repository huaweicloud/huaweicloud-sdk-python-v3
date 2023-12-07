# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PermissionSetPermissionUpdateDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dw_id': 'str',
        'permission_actions': 'list[str]'
    }

    attribute_map = {
        'dw_id': 'dw_id',
        'permission_actions': 'permission_actions'
    }

    def __init__(self, dw_id=None, permission_actions=None):
        """PermissionSetPermissionUpdateDTO

        The model defined in huaweicloud sdk

        :param dw_id: 数据连接id
        :type dw_id: str
        :param permission_actions: 权限操作列表
        :type permission_actions: list[str]
        """
        
        

        self._dw_id = None
        self._permission_actions = None
        self.discriminator = None

        if dw_id is not None:
            self.dw_id = dw_id
        if permission_actions is not None:
            self.permission_actions = permission_actions

    @property
    def dw_id(self):
        """Gets the dw_id of this PermissionSetPermissionUpdateDTO.

        数据连接id

        :return: The dw_id of this PermissionSetPermissionUpdateDTO.
        :rtype: str
        """
        return self._dw_id

    @dw_id.setter
    def dw_id(self, dw_id):
        """Sets the dw_id of this PermissionSetPermissionUpdateDTO.

        数据连接id

        :param dw_id: The dw_id of this PermissionSetPermissionUpdateDTO.
        :type dw_id: str
        """
        self._dw_id = dw_id

    @property
    def permission_actions(self):
        """Gets the permission_actions of this PermissionSetPermissionUpdateDTO.

        权限操作列表

        :return: The permission_actions of this PermissionSetPermissionUpdateDTO.
        :rtype: list[str]
        """
        return self._permission_actions

    @permission_actions.setter
    def permission_actions(self, permission_actions):
        """Sets the permission_actions of this PermissionSetPermissionUpdateDTO.

        权限操作列表

        :param permission_actions: The permission_actions of this PermissionSetPermissionUpdateDTO.
        :type permission_actions: list[str]
        """
        self._permission_actions = permission_actions

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
        if not isinstance(other, PermissionSetPermissionUpdateDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
