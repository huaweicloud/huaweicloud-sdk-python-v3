# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DelegatedAdministratorDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'delegation_enabled_at': 'datetime',
        'account_id': 'str',
        'account_urn': 'str',
        'join_method': 'str',
        'joined_at': 'datetime',
        'account_name': 'str'
    }

    attribute_map = {
        'delegation_enabled_at': 'delegation_enabled_at',
        'account_id': 'account_id',
        'account_urn': 'account_urn',
        'join_method': 'join_method',
        'joined_at': 'joined_at',
        'account_name': 'account_name'
    }

    def __init__(self, delegation_enabled_at=None, account_id=None, account_urn=None, join_method=None, joined_at=None, account_name=None):
        """DelegatedAdministratorDto

        The model defined in huaweicloud sdk

        :param delegation_enabled_at: 将帐号设置为委托管理员的日期。
        :type delegation_enabled_at: datetime
        :param account_id: 帐号的唯一标识符（ID）。
        :type account_id: str
        :param account_urn: 帐号的统一资源名称。
        :type account_urn: str
        :param join_method: 帐号加入组织的方式,invited：邀请加入，created：创建加入。
        :type join_method: str
        :param joined_at: 帐号成为组织一部分的日期。
        :type joined_at: datetime
        :param account_name: 帐号名称。
        :type account_name: str
        """
        
        

        self._delegation_enabled_at = None
        self._account_id = None
        self._account_urn = None
        self._join_method = None
        self._joined_at = None
        self._account_name = None
        self.discriminator = None

        self.delegation_enabled_at = delegation_enabled_at
        self.account_id = account_id
        self.account_urn = account_urn
        self.join_method = join_method
        self.joined_at = joined_at
        self.account_name = account_name

    @property
    def delegation_enabled_at(self):
        """Gets the delegation_enabled_at of this DelegatedAdministratorDto.

        将帐号设置为委托管理员的日期。

        :return: The delegation_enabled_at of this DelegatedAdministratorDto.
        :rtype: datetime
        """
        return self._delegation_enabled_at

    @delegation_enabled_at.setter
    def delegation_enabled_at(self, delegation_enabled_at):
        """Sets the delegation_enabled_at of this DelegatedAdministratorDto.

        将帐号设置为委托管理员的日期。

        :param delegation_enabled_at: The delegation_enabled_at of this DelegatedAdministratorDto.
        :type delegation_enabled_at: datetime
        """
        self._delegation_enabled_at = delegation_enabled_at

    @property
    def account_id(self):
        """Gets the account_id of this DelegatedAdministratorDto.

        帐号的唯一标识符（ID）。

        :return: The account_id of this DelegatedAdministratorDto.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this DelegatedAdministratorDto.

        帐号的唯一标识符（ID）。

        :param account_id: The account_id of this DelegatedAdministratorDto.
        :type account_id: str
        """
        self._account_id = account_id

    @property
    def account_urn(self):
        """Gets the account_urn of this DelegatedAdministratorDto.

        帐号的统一资源名称。

        :return: The account_urn of this DelegatedAdministratorDto.
        :rtype: str
        """
        return self._account_urn

    @account_urn.setter
    def account_urn(self, account_urn):
        """Sets the account_urn of this DelegatedAdministratorDto.

        帐号的统一资源名称。

        :param account_urn: The account_urn of this DelegatedAdministratorDto.
        :type account_urn: str
        """
        self._account_urn = account_urn

    @property
    def join_method(self):
        """Gets the join_method of this DelegatedAdministratorDto.

        帐号加入组织的方式,invited：邀请加入，created：创建加入。

        :return: The join_method of this DelegatedAdministratorDto.
        :rtype: str
        """
        return self._join_method

    @join_method.setter
    def join_method(self, join_method):
        """Sets the join_method of this DelegatedAdministratorDto.

        帐号加入组织的方式,invited：邀请加入，created：创建加入。

        :param join_method: The join_method of this DelegatedAdministratorDto.
        :type join_method: str
        """
        self._join_method = join_method

    @property
    def joined_at(self):
        """Gets the joined_at of this DelegatedAdministratorDto.

        帐号成为组织一部分的日期。

        :return: The joined_at of this DelegatedAdministratorDto.
        :rtype: datetime
        """
        return self._joined_at

    @joined_at.setter
    def joined_at(self, joined_at):
        """Sets the joined_at of this DelegatedAdministratorDto.

        帐号成为组织一部分的日期。

        :param joined_at: The joined_at of this DelegatedAdministratorDto.
        :type joined_at: datetime
        """
        self._joined_at = joined_at

    @property
    def account_name(self):
        """Gets the account_name of this DelegatedAdministratorDto.

        帐号名称。

        :return: The account_name of this DelegatedAdministratorDto.
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        """Sets the account_name of this DelegatedAdministratorDto.

        帐号名称。

        :param account_name: The account_name of this DelegatedAdministratorDto.
        :type account_name: str
        """
        self._account_name = account_name

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
        if not isinstance(other, DelegatedAdministratorDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
