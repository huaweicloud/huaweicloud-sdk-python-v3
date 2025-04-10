# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class KeystoneCreateUserResult:

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
        'name': 'str',
        'description': 'str',
        'pwd_status': 'bool',
        'password_expires_at': 'str',
        'links': 'LinksSelf',
        'id': 'str',
        'enabled': 'bool'
    }

    attribute_map = {
        'domain_id': 'domain_id',
        'name': 'name',
        'description': 'description',
        'pwd_status': 'pwd_status',
        'password_expires_at': 'password_expires_at',
        'links': 'links',
        'id': 'id',
        'enabled': 'enabled'
    }

    def __init__(self, domain_id=None, name=None, description=None, pwd_status=None, password_expires_at=None, links=None, id=None, enabled=None):
        r"""KeystoneCreateUserResult

        The model defined in huaweicloud sdk

        :param domain_id: IAM用户所属账号ID。
        :type domain_id: str
        :param name: IAM用户名。
        :type name: str
        :param description: IAM用户描述信息。
        :type description: str
        :param pwd_status: IAM用户密码状态。true：需要修改密码，false：正常；如果密码未设置，此字段可能不返回。
        :type pwd_status: bool
        :param password_expires_at: IAM用户密码过期时间（UTC时间），“null”表示密码不过期。
        :type password_expires_at: str
        :param links: 
        :type links: :class:`huaweicloudsdkiam.v3.LinksSelf`
        :param id: IAM用户ID。
        :type id: str
        :param enabled: IAM用户是否启用。true表示启用，false表示停用，默认为true。
        :type enabled: bool
        """
        
        

        self._domain_id = None
        self._name = None
        self._description = None
        self._pwd_status = None
        self._password_expires_at = None
        self._links = None
        self._id = None
        self._enabled = None
        self.discriminator = None

        self.domain_id = domain_id
        self.name = name
        if description is not None:
            self.description = description
        if pwd_status is not None:
            self.pwd_status = pwd_status
        self.password_expires_at = password_expires_at
        self.links = links
        self.id = id
        self.enabled = enabled

    @property
    def domain_id(self):
        r"""Gets the domain_id of this KeystoneCreateUserResult.

        IAM用户所属账号ID。

        :return: The domain_id of this KeystoneCreateUserResult.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this KeystoneCreateUserResult.

        IAM用户所属账号ID。

        :param domain_id: The domain_id of this KeystoneCreateUserResult.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def name(self):
        r"""Gets the name of this KeystoneCreateUserResult.

        IAM用户名。

        :return: The name of this KeystoneCreateUserResult.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this KeystoneCreateUserResult.

        IAM用户名。

        :param name: The name of this KeystoneCreateUserResult.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this KeystoneCreateUserResult.

        IAM用户描述信息。

        :return: The description of this KeystoneCreateUserResult.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this KeystoneCreateUserResult.

        IAM用户描述信息。

        :param description: The description of this KeystoneCreateUserResult.
        :type description: str
        """
        self._description = description

    @property
    def pwd_status(self):
        r"""Gets the pwd_status of this KeystoneCreateUserResult.

        IAM用户密码状态。true：需要修改密码，false：正常；如果密码未设置，此字段可能不返回。

        :return: The pwd_status of this KeystoneCreateUserResult.
        :rtype: bool
        """
        return self._pwd_status

    @pwd_status.setter
    def pwd_status(self, pwd_status):
        r"""Sets the pwd_status of this KeystoneCreateUserResult.

        IAM用户密码状态。true：需要修改密码，false：正常；如果密码未设置，此字段可能不返回。

        :param pwd_status: The pwd_status of this KeystoneCreateUserResult.
        :type pwd_status: bool
        """
        self._pwd_status = pwd_status

    @property
    def password_expires_at(self):
        r"""Gets the password_expires_at of this KeystoneCreateUserResult.

        IAM用户密码过期时间（UTC时间），“null”表示密码不过期。

        :return: The password_expires_at of this KeystoneCreateUserResult.
        :rtype: str
        """
        return self._password_expires_at

    @password_expires_at.setter
    def password_expires_at(self, password_expires_at):
        r"""Sets the password_expires_at of this KeystoneCreateUserResult.

        IAM用户密码过期时间（UTC时间），“null”表示密码不过期。

        :param password_expires_at: The password_expires_at of this KeystoneCreateUserResult.
        :type password_expires_at: str
        """
        self._password_expires_at = password_expires_at

    @property
    def links(self):
        r"""Gets the links of this KeystoneCreateUserResult.

        :return: The links of this KeystoneCreateUserResult.
        :rtype: :class:`huaweicloudsdkiam.v3.LinksSelf`
        """
        return self._links

    @links.setter
    def links(self, links):
        r"""Sets the links of this KeystoneCreateUserResult.

        :param links: The links of this KeystoneCreateUserResult.
        :type links: :class:`huaweicloudsdkiam.v3.LinksSelf`
        """
        self._links = links

    @property
    def id(self):
        r"""Gets the id of this KeystoneCreateUserResult.

        IAM用户ID。

        :return: The id of this KeystoneCreateUserResult.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this KeystoneCreateUserResult.

        IAM用户ID。

        :param id: The id of this KeystoneCreateUserResult.
        :type id: str
        """
        self._id = id

    @property
    def enabled(self):
        r"""Gets the enabled of this KeystoneCreateUserResult.

        IAM用户是否启用。true表示启用，false表示停用，默认为true。

        :return: The enabled of this KeystoneCreateUserResult.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this KeystoneCreateUserResult.

        IAM用户是否启用。true表示启用，false表示停用，默认为true。

        :param enabled: The enabled of this KeystoneCreateUserResult.
        :type enabled: bool
        """
        self._enabled = enabled

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
        if not isinstance(other, KeystoneCreateUserResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
