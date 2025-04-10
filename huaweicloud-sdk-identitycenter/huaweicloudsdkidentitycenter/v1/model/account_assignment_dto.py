# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AccountAssignmentDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'account_id': 'str',
        'permission_set_id': 'str',
        'principal_id': 'str',
        'principal_type': 'str'
    }

    attribute_map = {
        'account_id': 'account_id',
        'permission_set_id': 'permission_set_id',
        'principal_id': 'principal_id',
        'principal_type': 'principal_type'
    }

    def __init__(self, account_id=None, permission_set_id=None, principal_id=None, principal_type=None):
        r"""AccountAssignmentDto

        The model defined in huaweicloud sdk

        :param account_id: 账号的唯一标识
        :type account_id: str
        :param permission_set_id: 权限集唯一标识.
        :type permission_set_id: str
        :param principal_id: IAM身份中心中的一个实体身份唯一标识，例如用户或用户组
        :type principal_id: str
        :param principal_type: 绑定的实体类型
        :type principal_type: str
        """
        
        

        self._account_id = None
        self._permission_set_id = None
        self._principal_id = None
        self._principal_type = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        if permission_set_id is not None:
            self.permission_set_id = permission_set_id
        if principal_id is not None:
            self.principal_id = principal_id
        if principal_type is not None:
            self.principal_type = principal_type

    @property
    def account_id(self):
        r"""Gets the account_id of this AccountAssignmentDto.

        账号的唯一标识

        :return: The account_id of this AccountAssignmentDto.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        r"""Sets the account_id of this AccountAssignmentDto.

        账号的唯一标识

        :param account_id: The account_id of this AccountAssignmentDto.
        :type account_id: str
        """
        self._account_id = account_id

    @property
    def permission_set_id(self):
        r"""Gets the permission_set_id of this AccountAssignmentDto.

        权限集唯一标识.

        :return: The permission_set_id of this AccountAssignmentDto.
        :rtype: str
        """
        return self._permission_set_id

    @permission_set_id.setter
    def permission_set_id(self, permission_set_id):
        r"""Sets the permission_set_id of this AccountAssignmentDto.

        权限集唯一标识.

        :param permission_set_id: The permission_set_id of this AccountAssignmentDto.
        :type permission_set_id: str
        """
        self._permission_set_id = permission_set_id

    @property
    def principal_id(self):
        r"""Gets the principal_id of this AccountAssignmentDto.

        IAM身份中心中的一个实体身份唯一标识，例如用户或用户组

        :return: The principal_id of this AccountAssignmentDto.
        :rtype: str
        """
        return self._principal_id

    @principal_id.setter
    def principal_id(self, principal_id):
        r"""Sets the principal_id of this AccountAssignmentDto.

        IAM身份中心中的一个实体身份唯一标识，例如用户或用户组

        :param principal_id: The principal_id of this AccountAssignmentDto.
        :type principal_id: str
        """
        self._principal_id = principal_id

    @property
    def principal_type(self):
        r"""Gets the principal_type of this AccountAssignmentDto.

        绑定的实体类型

        :return: The principal_type of this AccountAssignmentDto.
        :rtype: str
        """
        return self._principal_type

    @principal_type.setter
    def principal_type(self, principal_type):
        r"""Sets the principal_type of this AccountAssignmentDto.

        绑定的实体类型

        :param principal_type: The principal_type of this AccountAssignmentDto.
        :type principal_type: str
        """
        self._principal_type = principal_type

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
        if not isinstance(other, AccountAssignmentDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
