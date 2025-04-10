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
        'status': 'str',
        'joined_at': 'datetime',
        'name': 'str',
        'mobile_phone': 'str',
        'intl_number_prefix': 'str',
        'email': 'str',
        'description': 'str'
    }

    attribute_map = {
        'id': 'id',
        'urn': 'urn',
        'join_method': 'join_method',
        'status': 'status',
        'joined_at': 'joined_at',
        'name': 'name',
        'mobile_phone': 'mobile_phone',
        'intl_number_prefix': 'intl_number_prefix',
        'email': 'email',
        'description': 'description'
    }

    def __init__(self, id=None, urn=None, join_method=None, status=None, joined_at=None, name=None, mobile_phone=None, intl_number_prefix=None, email=None, description=None):
        r"""AccountDto

        The model defined in huaweicloud sdk

        :param id: 账号的唯一标识符（ID）。
        :type id: str
        :param urn: 账号的统一资源名称。
        :type urn: str
        :param join_method: 账号加入组织的方式。invited：邀请加入，created：创建加入。
        :type join_method: str
        :param status: 账号当前的状态。active：有效； suspended：已关闭； pending_closure：关闭中。
        :type status: str
        :param joined_at: 账号加入组织的日期。
        :type joined_at: datetime
        :param name: 账号名称
        :type name: str
        :param mobile_phone: 手机号码
        :type mobile_phone: str
        :param intl_number_prefix: 手机号前缀。
        :type intl_number_prefix: str
        :param email: 与此账号关联的电子邮件地址。
        :type email: str
        :param description: 描述信息。
        :type description: str
        """
        
        

        self._id = None
        self._urn = None
        self._join_method = None
        self._status = None
        self._joined_at = None
        self._name = None
        self._mobile_phone = None
        self._intl_number_prefix = None
        self._email = None
        self._description = None
        self.discriminator = None

        self.id = id
        self.urn = urn
        self.join_method = join_method
        self.status = status
        self.joined_at = joined_at
        self.name = name
        if mobile_phone is not None:
            self.mobile_phone = mobile_phone
        if intl_number_prefix is not None:
            self.intl_number_prefix = intl_number_prefix
        if email is not None:
            self.email = email
        if description is not None:
            self.description = description

    @property
    def id(self):
        r"""Gets the id of this AccountDto.

        账号的唯一标识符（ID）。

        :return: The id of this AccountDto.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this AccountDto.

        账号的唯一标识符（ID）。

        :param id: The id of this AccountDto.
        :type id: str
        """
        self._id = id

    @property
    def urn(self):
        r"""Gets the urn of this AccountDto.

        账号的统一资源名称。

        :return: The urn of this AccountDto.
        :rtype: str
        """
        return self._urn

    @urn.setter
    def urn(self, urn):
        r"""Sets the urn of this AccountDto.

        账号的统一资源名称。

        :param urn: The urn of this AccountDto.
        :type urn: str
        """
        self._urn = urn

    @property
    def join_method(self):
        r"""Gets the join_method of this AccountDto.

        账号加入组织的方式。invited：邀请加入，created：创建加入。

        :return: The join_method of this AccountDto.
        :rtype: str
        """
        return self._join_method

    @join_method.setter
    def join_method(self, join_method):
        r"""Sets the join_method of this AccountDto.

        账号加入组织的方式。invited：邀请加入，created：创建加入。

        :param join_method: The join_method of this AccountDto.
        :type join_method: str
        """
        self._join_method = join_method

    @property
    def status(self):
        r"""Gets the status of this AccountDto.

        账号当前的状态。active：有效； suspended：已关闭； pending_closure：关闭中。

        :return: The status of this AccountDto.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this AccountDto.

        账号当前的状态。active：有效； suspended：已关闭； pending_closure：关闭中。

        :param status: The status of this AccountDto.
        :type status: str
        """
        self._status = status

    @property
    def joined_at(self):
        r"""Gets the joined_at of this AccountDto.

        账号加入组织的日期。

        :return: The joined_at of this AccountDto.
        :rtype: datetime
        """
        return self._joined_at

    @joined_at.setter
    def joined_at(self, joined_at):
        r"""Sets the joined_at of this AccountDto.

        账号加入组织的日期。

        :param joined_at: The joined_at of this AccountDto.
        :type joined_at: datetime
        """
        self._joined_at = joined_at

    @property
    def name(self):
        r"""Gets the name of this AccountDto.

        账号名称

        :return: The name of this AccountDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this AccountDto.

        账号名称

        :param name: The name of this AccountDto.
        :type name: str
        """
        self._name = name

    @property
    def mobile_phone(self):
        r"""Gets the mobile_phone of this AccountDto.

        手机号码

        :return: The mobile_phone of this AccountDto.
        :rtype: str
        """
        return self._mobile_phone

    @mobile_phone.setter
    def mobile_phone(self, mobile_phone):
        r"""Sets the mobile_phone of this AccountDto.

        手机号码

        :param mobile_phone: The mobile_phone of this AccountDto.
        :type mobile_phone: str
        """
        self._mobile_phone = mobile_phone

    @property
    def intl_number_prefix(self):
        r"""Gets the intl_number_prefix of this AccountDto.

        手机号前缀。

        :return: The intl_number_prefix of this AccountDto.
        :rtype: str
        """
        return self._intl_number_prefix

    @intl_number_prefix.setter
    def intl_number_prefix(self, intl_number_prefix):
        r"""Sets the intl_number_prefix of this AccountDto.

        手机号前缀。

        :param intl_number_prefix: The intl_number_prefix of this AccountDto.
        :type intl_number_prefix: str
        """
        self._intl_number_prefix = intl_number_prefix

    @property
    def email(self):
        r"""Gets the email of this AccountDto.

        与此账号关联的电子邮件地址。

        :return: The email of this AccountDto.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        r"""Sets the email of this AccountDto.

        与此账号关联的电子邮件地址。

        :param email: The email of this AccountDto.
        :type email: str
        """
        self._email = email

    @property
    def description(self):
        r"""Gets the description of this AccountDto.

        描述信息。

        :return: The description of this AccountDto.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this AccountDto.

        描述信息。

        :param description: The description of this AccountDto.
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
        if not isinstance(other, AccountDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
