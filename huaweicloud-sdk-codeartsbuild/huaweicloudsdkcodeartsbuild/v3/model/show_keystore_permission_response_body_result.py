# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowKeystorePermissionResponseBodyResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'permission_list': 'list[AddKeystorePermissionResponseBody]'
    }

    attribute_map = {
        'total': 'total',
        'permission_list': 'permission_list'
    }

    def __init__(self, total=None, permission_list=None):
        r"""ShowKeystorePermissionResponseBodyResult

        The model defined in huaweicloud sdk

        :param total: 总数
        :type total: int
        :param permission_list: 权限结集合
        :type permission_list: list[:class:`huaweicloudsdkcodeartsbuild.v3.AddKeystorePermissionResponseBody`]
        """
        
        

        self._total = None
        self._permission_list = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if permission_list is not None:
            self.permission_list = permission_list

    @property
    def total(self):
        r"""Gets the total of this ShowKeystorePermissionResponseBodyResult.

        总数

        :return: The total of this ShowKeystorePermissionResponseBodyResult.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ShowKeystorePermissionResponseBodyResult.

        总数

        :param total: The total of this ShowKeystorePermissionResponseBodyResult.
        :type total: int
        """
        self._total = total

    @property
    def permission_list(self):
        r"""Gets the permission_list of this ShowKeystorePermissionResponseBodyResult.

        权限结集合

        :return: The permission_list of this ShowKeystorePermissionResponseBodyResult.
        :rtype: list[:class:`huaweicloudsdkcodeartsbuild.v3.AddKeystorePermissionResponseBody`]
        """
        return self._permission_list

    @permission_list.setter
    def permission_list(self, permission_list):
        r"""Sets the permission_list of this ShowKeystorePermissionResponseBodyResult.

        权限结集合

        :param permission_list: The permission_list of this ShowKeystorePermissionResponseBodyResult.
        :type permission_list: list[:class:`huaweicloudsdkcodeartsbuild.v3.AddKeystorePermissionResponseBody`]
        """
        self._permission_list = permission_list

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
        if not isinstance(other, ShowKeystorePermissionResponseBodyResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
