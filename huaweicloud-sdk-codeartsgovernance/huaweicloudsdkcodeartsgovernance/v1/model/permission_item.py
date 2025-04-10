# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PermissionItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'perm_name': 'str',
        'desc': 'str',
        'pro_level_name': 'str',
        'perm_type_name': 'str'
    }

    attribute_map = {
        'perm_name': 'perm_name',
        'desc': 'desc',
        'pro_level_name': 'pro_level_name',
        'perm_type_name': 'perm_type_name'
    }

    def __init__(self, perm_name=None, desc=None, pro_level_name=None, perm_type_name=None):
        r"""PermissionItem

        The model defined in huaweicloud sdk

        :param perm_name: 权限名称
        :type perm_name: str
        :param desc: 权限描述
        :type desc: str
        :param pro_level_name: 权限保护级别
        :type pro_level_name: str
        :param perm_type_name: 权限类型
        :type perm_type_name: str
        """
        
        

        self._perm_name = None
        self._desc = None
        self._pro_level_name = None
        self._perm_type_name = None
        self.discriminator = None

        if perm_name is not None:
            self.perm_name = perm_name
        if desc is not None:
            self.desc = desc
        if pro_level_name is not None:
            self.pro_level_name = pro_level_name
        if perm_type_name is not None:
            self.perm_type_name = perm_type_name

    @property
    def perm_name(self):
        r"""Gets the perm_name of this PermissionItem.

        权限名称

        :return: The perm_name of this PermissionItem.
        :rtype: str
        """
        return self._perm_name

    @perm_name.setter
    def perm_name(self, perm_name):
        r"""Sets the perm_name of this PermissionItem.

        权限名称

        :param perm_name: The perm_name of this PermissionItem.
        :type perm_name: str
        """
        self._perm_name = perm_name

    @property
    def desc(self):
        r"""Gets the desc of this PermissionItem.

        权限描述

        :return: The desc of this PermissionItem.
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        r"""Sets the desc of this PermissionItem.

        权限描述

        :param desc: The desc of this PermissionItem.
        :type desc: str
        """
        self._desc = desc

    @property
    def pro_level_name(self):
        r"""Gets the pro_level_name of this PermissionItem.

        权限保护级别

        :return: The pro_level_name of this PermissionItem.
        :rtype: str
        """
        return self._pro_level_name

    @pro_level_name.setter
    def pro_level_name(self, pro_level_name):
        r"""Sets the pro_level_name of this PermissionItem.

        权限保护级别

        :param pro_level_name: The pro_level_name of this PermissionItem.
        :type pro_level_name: str
        """
        self._pro_level_name = pro_level_name

    @property
    def perm_type_name(self):
        r"""Gets the perm_type_name of this PermissionItem.

        权限类型

        :return: The perm_type_name of this PermissionItem.
        :rtype: str
        """
        return self._perm_type_name

    @perm_type_name.setter
    def perm_type_name(self, perm_type_name):
        r"""Sets the perm_type_name of this PermissionItem.

        权限类型

        :param perm_type_name: The perm_type_name of this PermissionItem.
        :type perm_type_name: str
        """
        self._perm_type_name = perm_type_name

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
        if not isinstance(other, PermissionItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
