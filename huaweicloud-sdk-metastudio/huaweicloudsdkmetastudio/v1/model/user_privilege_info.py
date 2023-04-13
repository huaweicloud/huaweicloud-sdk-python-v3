# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UserPrivilegeInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tenant_id': 'str',
        'privilege': 'str',
        'expire_time': 'str'
    }

    attribute_map = {
        'tenant_id': 'tenant_id',
        'privilege': 'privilege',
        'expire_time': 'expire_time'
    }

    def __init__(self, tenant_id=None, privilege=None, expire_time=None):
        """UserPrivilegeInfo

        The model defined in huaweicloud sdk

        :param tenant_id: 租户ID
        :type tenant_id: str
        :param privilege: 租户权限 INTERNAL_TEST: 内测用户权限，有服务配额限制 SYSTEM_ADMIN：系统管理员权限，可加权限 PARTNER：伙伴权限，暂不做配额限制 ME_PRIVILEGE:ME白名单权限
        :type privilege: str
        :param expire_time: 配额过期时间，格式遵循：RFC 3339 如\&quot;2021-01-10T08:43:17Z\&quot;
        :type expire_time: str
        """
        
        

        self._tenant_id = None
        self._privilege = None
        self._expire_time = None
        self.discriminator = None

        self.tenant_id = tenant_id
        self.privilege = privilege
        if expire_time is not None:
            self.expire_time = expire_time

    @property
    def tenant_id(self):
        """Gets the tenant_id of this UserPrivilegeInfo.

        租户ID

        :return: The tenant_id of this UserPrivilegeInfo.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this UserPrivilegeInfo.

        租户ID

        :param tenant_id: The tenant_id of this UserPrivilegeInfo.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def privilege(self):
        """Gets the privilege of this UserPrivilegeInfo.

        租户权限 INTERNAL_TEST: 内测用户权限，有服务配额限制 SYSTEM_ADMIN：系统管理员权限，可加权限 PARTNER：伙伴权限，暂不做配额限制 ME_PRIVILEGE:ME白名单权限

        :return: The privilege of this UserPrivilegeInfo.
        :rtype: str
        """
        return self._privilege

    @privilege.setter
    def privilege(self, privilege):
        """Sets the privilege of this UserPrivilegeInfo.

        租户权限 INTERNAL_TEST: 内测用户权限，有服务配额限制 SYSTEM_ADMIN：系统管理员权限，可加权限 PARTNER：伙伴权限，暂不做配额限制 ME_PRIVILEGE:ME白名单权限

        :param privilege: The privilege of this UserPrivilegeInfo.
        :type privilege: str
        """
        self._privilege = privilege

    @property
    def expire_time(self):
        """Gets the expire_time of this UserPrivilegeInfo.

        配额过期时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"

        :return: The expire_time of this UserPrivilegeInfo.
        :rtype: str
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        """Sets the expire_time of this UserPrivilegeInfo.

        配额过期时间，格式遵循：RFC 3339 如\"2021-01-10T08:43:17Z\"

        :param expire_time: The expire_time of this UserPrivilegeInfo.
        :type expire_time: str
        """
        self._expire_time = expire_time

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
        if not isinstance(other, UserPrivilegeInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
