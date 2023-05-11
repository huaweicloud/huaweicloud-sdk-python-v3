# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AccountDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'urn': 'str',
        'join_method': 'str',
        'joined_at': 'datetime',
        'name': 'str'
    }

    attribute_map = {
        'id': 'id',
        'urn': 'urn',
        'join_method': 'join_method',
        'joined_at': 'joined_at',
        'name': 'name'
    }

    def __init__(self, id=None, urn=None, join_method=None, joined_at=None, name=None):
        """AccountDto

        The model defined in huaweicloud sdk

        :param id: 帐号的唯一标识符（ID）。
        :type id: str
        :param urn: 帐号的统一资源名称。
        :type urn: str
        :param join_method: 帐号加入组织的方式,invited：邀请加入，created：创建加入。
        :type join_method: str
        :param joined_at: 帐号加入组织的日期。
        :type joined_at: datetime
        :param name: 帐号名称。
        :type name: str
        """
        
        

        self._id = None
        self._urn = None
        self._join_method = None
        self._joined_at = None
        self._name = None
        self.discriminator = None

        self.id = id
        self.urn = urn
        self.join_method = join_method
        self.joined_at = joined_at
        self.name = name

    @property
    def id(self):
        """Gets the id of this AccountDto.

        帐号的唯一标识符（ID）。

        :return: The id of this AccountDto.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AccountDto.

        帐号的唯一标识符（ID）。

        :param id: The id of this AccountDto.
        :type id: str
        """
        self._id = id

    @property
    def urn(self):
        """Gets the urn of this AccountDto.

        帐号的统一资源名称。

        :return: The urn of this AccountDto.
        :rtype: str
        """
        return self._urn

    @urn.setter
    def urn(self, urn):
        """Sets the urn of this AccountDto.

        帐号的统一资源名称。

        :param urn: The urn of this AccountDto.
        :type urn: str
        """
        self._urn = urn

    @property
    def join_method(self):
        """Gets the join_method of this AccountDto.

        帐号加入组织的方式,invited：邀请加入，created：创建加入。

        :return: The join_method of this AccountDto.
        :rtype: str
        """
        return self._join_method

    @join_method.setter
    def join_method(self, join_method):
        """Sets the join_method of this AccountDto.

        帐号加入组织的方式,invited：邀请加入，created：创建加入。

        :param join_method: The join_method of this AccountDto.
        :type join_method: str
        """
        self._join_method = join_method

    @property
    def joined_at(self):
        """Gets the joined_at of this AccountDto.

        帐号加入组织的日期。

        :return: The joined_at of this AccountDto.
        :rtype: datetime
        """
        return self._joined_at

    @joined_at.setter
    def joined_at(self, joined_at):
        """Sets the joined_at of this AccountDto.

        帐号加入组织的日期。

        :param joined_at: The joined_at of this AccountDto.
        :type joined_at: datetime
        """
        self._joined_at = joined_at

    @property
    def name(self):
        """Gets the name of this AccountDto.

        帐号名称。

        :return: The name of this AccountDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AccountDto.

        帐号名称。

        :param name: The name of this AccountDto.
        :type name: str
        """
        self._name = name

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
        if not isinstance(other, AccountDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
