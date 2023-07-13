# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApigRoleVo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'role_id': 'str',
        'role_code': 'str',
        'role_name': 'str',
        'description': 'str'
    }

    attribute_map = {
        'role_id': 'role_id',
        'role_code': 'role_code',
        'role_name': 'role_name',
        'description': 'description'
    }

    def __init__(self, role_id=None, role_code=None, role_name=None, description=None):
        """ApigRoleVo

        The model defined in huaweicloud sdk

        :param role_id: 角色id
        :type role_id: str
        :param role_code: 角色编码
        :type role_code: str
        :param role_name: 角色名称
        :type role_name: str
        :param description: 描述
        :type description: str
        """
        
        

        self._role_id = None
        self._role_code = None
        self._role_name = None
        self._description = None
        self.discriminator = None

        if role_id is not None:
            self.role_id = role_id
        if role_code is not None:
            self.role_code = role_code
        if role_name is not None:
            self.role_name = role_name
        if description is not None:
            self.description = description

    @property
    def role_id(self):
        """Gets the role_id of this ApigRoleVo.

        角色id

        :return: The role_id of this ApigRoleVo.
        :rtype: str
        """
        return self._role_id

    @role_id.setter
    def role_id(self, role_id):
        """Sets the role_id of this ApigRoleVo.

        角色id

        :param role_id: The role_id of this ApigRoleVo.
        :type role_id: str
        """
        self._role_id = role_id

    @property
    def role_code(self):
        """Gets the role_code of this ApigRoleVo.

        角色编码

        :return: The role_code of this ApigRoleVo.
        :rtype: str
        """
        return self._role_code

    @role_code.setter
    def role_code(self, role_code):
        """Sets the role_code of this ApigRoleVo.

        角色编码

        :param role_code: The role_code of this ApigRoleVo.
        :type role_code: str
        """
        self._role_code = role_code

    @property
    def role_name(self):
        """Gets the role_name of this ApigRoleVo.

        角色名称

        :return: The role_name of this ApigRoleVo.
        :rtype: str
        """
        return self._role_name

    @role_name.setter
    def role_name(self, role_name):
        """Sets the role_name of this ApigRoleVo.

        角色名称

        :param role_name: The role_name of this ApigRoleVo.
        :type role_name: str
        """
        self._role_name = role_name

    @property
    def description(self):
        """Gets the description of this ApigRoleVo.

        描述

        :return: The description of this ApigRoleVo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ApigRoleVo.

        描述

        :param description: The description of this ApigRoleVo.
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
        if not isinstance(other, ApigRoleVo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
