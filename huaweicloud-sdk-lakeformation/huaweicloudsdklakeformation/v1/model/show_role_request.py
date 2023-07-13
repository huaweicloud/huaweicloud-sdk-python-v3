# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowRoleRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'role_name': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'role_name': 'role_name'
    }

    def __init__(self, instance_id=None, role_name=None):
        """ShowRoleRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例Id
        :type instance_id: str
        :param role_name: 角色名称
        :type role_name: str
        """
        
        

        self._instance_id = None
        self._role_name = None
        self.discriminator = None

        self.instance_id = instance_id
        self.role_name = role_name

    @property
    def instance_id(self):
        """Gets the instance_id of this ShowRoleRequest.

        实例Id

        :return: The instance_id of this ShowRoleRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ShowRoleRequest.

        实例Id

        :param instance_id: The instance_id of this ShowRoleRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def role_name(self):
        """Gets the role_name of this ShowRoleRequest.

        角色名称

        :return: The role_name of this ShowRoleRequest.
        :rtype: str
        """
        return self._role_name

    @role_name.setter
    def role_name(self, role_name):
        """Sets the role_name of this ShowRoleRequest.

        角色名称

        :param role_name: The role_name of this ShowRoleRequest.
        :type role_name: str
        """
        self._role_name = role_name

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
        if not isinstance(other, ShowRoleRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
