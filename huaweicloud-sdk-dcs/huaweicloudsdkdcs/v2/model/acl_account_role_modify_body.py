# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AclAccountRoleModifyBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'account_role': 'str'
    }

    attribute_map = {
        'account_role': 'account_role'
    }

    def __init__(self, account_role=None):
        r"""AclAccountRoleModifyBody

        The model defined in huaweicloud sdk

        :param account_role: 账号权限
        :type account_role: str
        """
        
        

        self._account_role = None
        self.discriminator = None

        if account_role is not None:
            self.account_role = account_role

    @property
    def account_role(self):
        r"""Gets the account_role of this AclAccountRoleModifyBody.

        账号权限

        :return: The account_role of this AclAccountRoleModifyBody.
        :rtype: str
        """
        return self._account_role

    @account_role.setter
    def account_role(self, account_role):
        r"""Sets the account_role of this AclAccountRoleModifyBody.

        账号权限

        :param account_role: The account_role of this AclAccountRoleModifyBody.
        :type account_role: str
        """
        self._account_role = account_role

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
        if not isinstance(other, AclAccountRoleModifyBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
