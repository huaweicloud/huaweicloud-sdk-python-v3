# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class KeystoneCheckDomainPermissionForGroupRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain_id': 'str',
        'group_id': 'str',
        'role_id': 'str'
    }

    attribute_map = {
        'domain_id': 'domain_id',
        'group_id': 'group_id',
        'role_id': 'role_id'
    }

    def __init__(self, domain_id=None, group_id=None, role_id=None):
        r"""KeystoneCheckDomainPermissionForGroupRequest

        The model defined in huaweicloud sdk

        :param domain_id: 用户组所属账号ID，获取方式请参见：[获取账号ID](https://support.huaweicloud.com/api-iam/iam_17_0002.html)。
        :type domain_id: str
        :param group_id: 用户组ID，获取方式请参见：[获取用户组ID](https://support.huaweicloud.com/api-iam/iam_17_0002.html)。
        :type group_id: str
        :param role_id: 权限ID，获取方式请参见：[获取权限名、权限ID](https://support.huaweicloud.com/api-iam/iam_10_0001.html)。
        :type role_id: str
        """
        
        

        self._domain_id = None
        self._group_id = None
        self._role_id = None
        self.discriminator = None

        self.domain_id = domain_id
        self.group_id = group_id
        self.role_id = role_id

    @property
    def domain_id(self):
        r"""Gets the domain_id of this KeystoneCheckDomainPermissionForGroupRequest.

        用户组所属账号ID，获取方式请参见：[获取账号ID](https://support.huaweicloud.com/api-iam/iam_17_0002.html)。

        :return: The domain_id of this KeystoneCheckDomainPermissionForGroupRequest.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this KeystoneCheckDomainPermissionForGroupRequest.

        用户组所属账号ID，获取方式请参见：[获取账号ID](https://support.huaweicloud.com/api-iam/iam_17_0002.html)。

        :param domain_id: The domain_id of this KeystoneCheckDomainPermissionForGroupRequest.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def group_id(self):
        r"""Gets the group_id of this KeystoneCheckDomainPermissionForGroupRequest.

        用户组ID，获取方式请参见：[获取用户组ID](https://support.huaweicloud.com/api-iam/iam_17_0002.html)。

        :return: The group_id of this KeystoneCheckDomainPermissionForGroupRequest.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this KeystoneCheckDomainPermissionForGroupRequest.

        用户组ID，获取方式请参见：[获取用户组ID](https://support.huaweicloud.com/api-iam/iam_17_0002.html)。

        :param group_id: The group_id of this KeystoneCheckDomainPermissionForGroupRequest.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def role_id(self):
        r"""Gets the role_id of this KeystoneCheckDomainPermissionForGroupRequest.

        权限ID，获取方式请参见：[获取权限名、权限ID](https://support.huaweicloud.com/api-iam/iam_10_0001.html)。

        :return: The role_id of this KeystoneCheckDomainPermissionForGroupRequest.
        :rtype: str
        """
        return self._role_id

    @role_id.setter
    def role_id(self, role_id):
        r"""Sets the role_id of this KeystoneCheckDomainPermissionForGroupRequest.

        权限ID，获取方式请参见：[获取权限名、权限ID](https://support.huaweicloud.com/api-iam/iam_10_0001.html)。

        :param role_id: The role_id of this KeystoneCheckDomainPermissionForGroupRequest.
        :type role_id: str
        """
        self._role_id = role_id

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
        if not isinstance(other, KeystoneCheckDomainPermissionForGroupRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
