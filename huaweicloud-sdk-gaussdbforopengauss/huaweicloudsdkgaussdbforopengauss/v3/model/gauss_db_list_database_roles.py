# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GaussDBListDatabaseRoles:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'memberof': 'str',
        'lock_status': 'bool',
        'attribute': 'GaussDBListDatabaseRolesPriv'
    }

    attribute_map = {
        'name': 'name',
        'memberof': 'memberof',
        'lock_status': 'lock_status',
        'attribute': 'attribute'
    }

    def __init__(self, name=None, memberof=None, lock_status=None, attribute=None):
        r"""GaussDBListDatabaseRoles

        The model defined in huaweicloud sdk

        :param name: 数据库用户/角色名。
        :type name: str
        :param memberof: 用户/角色的默认权限。
        :type memberof: str
        :param lock_status: 用户/角色是否被锁。
        :type lock_status: bool
        :param attribute: 
        :type attribute: :class:`huaweicloudsdkgaussdbforopengauss.v3.GaussDBListDatabaseRolesPriv`
        """
        
        

        self._name = None
        self._memberof = None
        self._lock_status = None
        self._attribute = None
        self.discriminator = None

        self.name = name
        if memberof is not None:
            self.memberof = memberof
        if lock_status is not None:
            self.lock_status = lock_status
        if attribute is not None:
            self.attribute = attribute

    @property
    def name(self):
        r"""Gets the name of this GaussDBListDatabaseRoles.

        数据库用户/角色名。

        :return: The name of this GaussDBListDatabaseRoles.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this GaussDBListDatabaseRoles.

        数据库用户/角色名。

        :param name: The name of this GaussDBListDatabaseRoles.
        :type name: str
        """
        self._name = name

    @property
    def memberof(self):
        r"""Gets the memberof of this GaussDBListDatabaseRoles.

        用户/角色的默认权限。

        :return: The memberof of this GaussDBListDatabaseRoles.
        :rtype: str
        """
        return self._memberof

    @memberof.setter
    def memberof(self, memberof):
        r"""Sets the memberof of this GaussDBListDatabaseRoles.

        用户/角色的默认权限。

        :param memberof: The memberof of this GaussDBListDatabaseRoles.
        :type memberof: str
        """
        self._memberof = memberof

    @property
    def lock_status(self):
        r"""Gets the lock_status of this GaussDBListDatabaseRoles.

        用户/角色是否被锁。

        :return: The lock_status of this GaussDBListDatabaseRoles.
        :rtype: bool
        """
        return self._lock_status

    @lock_status.setter
    def lock_status(self, lock_status):
        r"""Sets the lock_status of this GaussDBListDatabaseRoles.

        用户/角色是否被锁。

        :param lock_status: The lock_status of this GaussDBListDatabaseRoles.
        :type lock_status: bool
        """
        self._lock_status = lock_status

    @property
    def attribute(self):
        r"""Gets the attribute of this GaussDBListDatabaseRoles.

        :return: The attribute of this GaussDBListDatabaseRoles.
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.GaussDBListDatabaseRolesPriv`
        """
        return self._attribute

    @attribute.setter
    def attribute(self, attribute):
        r"""Sets the attribute of this GaussDBListDatabaseRoles.

        :param attribute: The attribute of this GaussDBListDatabaseRoles.
        :type attribute: :class:`huaweicloudsdkgaussdbforopengauss.v3.GaussDBListDatabaseRolesPriv`
        """
        self._attribute = attribute

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
        if not isinstance(other, GaussDBListDatabaseRoles):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
