# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class KeystoneListUsersRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []
    sensitive_list.append('password_expires_at')

    openapi_types = {
        'domain_id': 'str',
        'enabled': 'bool',
        'name': 'str',
        'password_expires_at': 'str'
    }

    attribute_map = {
        'domain_id': 'domain_id',
        'enabled': 'enabled',
        'name': 'name',
        'password_expires_at': 'password_expires_at'
    }

    def __init__(self, domain_id=None, enabled=None, name=None, password_expires_at=None):
        r"""KeystoneListUsersRequest

        The model defined in huaweicloud sdk

        :param domain_id: IAM用户所属账号ID，获取方式请参见：[获取账号ID](https://support.huaweicloud.com/api-iam/iam_17_0002.html)。
        :type domain_id: str
        :param enabled: 是否启IAM用户，true为启用，false为停用，默认为true。
        :type enabled: bool
        :param name: IAM用户名。
        :type name: str
        :param password_expires_at: 密码过期时间，格式为：password_expires_at&#x3D;{operator}:{timestamp}。timestamp格式为：YYYY-MM-DDTHH:mm:ssZ。示例：  &#x60;&#x60;&#x60; password_expires_at&#x3D;lt:2016-12-08T22:02:00Z &#x60;&#x60;&#x60; &gt; - operator取值范围：lt，lte，gt，gte，eq，neq。 &gt; - lt：过期时间小于timestamp。 &gt; - lte：过期时间小于等于timestamp。 &gt; - gt：过期时间大于timestamp。 &gt; - gte：过期时间大于等于timestamp。 &gt; - eq：过期时间等于timestamp。 &gt; - neq：过期时间不等于timestamp。
        :type password_expires_at: str
        """
        
        

        self._domain_id = None
        self._enabled = None
        self._name = None
        self._password_expires_at = None
        self.discriminator = None

        if domain_id is not None:
            self.domain_id = domain_id
        if enabled is not None:
            self.enabled = enabled
        if name is not None:
            self.name = name
        if password_expires_at is not None:
            self.password_expires_at = password_expires_at

    @property
    def domain_id(self):
        r"""Gets the domain_id of this KeystoneListUsersRequest.

        IAM用户所属账号ID，获取方式请参见：[获取账号ID](https://support.huaweicloud.com/api-iam/iam_17_0002.html)。

        :return: The domain_id of this KeystoneListUsersRequest.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this KeystoneListUsersRequest.

        IAM用户所属账号ID，获取方式请参见：[获取账号ID](https://support.huaweicloud.com/api-iam/iam_17_0002.html)。

        :param domain_id: The domain_id of this KeystoneListUsersRequest.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def enabled(self):
        r"""Gets the enabled of this KeystoneListUsersRequest.

        是否启IAM用户，true为启用，false为停用，默认为true。

        :return: The enabled of this KeystoneListUsersRequest.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        r"""Sets the enabled of this KeystoneListUsersRequest.

        是否启IAM用户，true为启用，false为停用，默认为true。

        :param enabled: The enabled of this KeystoneListUsersRequest.
        :type enabled: bool
        """
        self._enabled = enabled

    @property
    def name(self):
        r"""Gets the name of this KeystoneListUsersRequest.

        IAM用户名。

        :return: The name of this KeystoneListUsersRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this KeystoneListUsersRequest.

        IAM用户名。

        :param name: The name of this KeystoneListUsersRequest.
        :type name: str
        """
        self._name = name

    @property
    def password_expires_at(self):
        r"""Gets the password_expires_at of this KeystoneListUsersRequest.

        密码过期时间，格式为：password_expires_at={operator}:{timestamp}。timestamp格式为：YYYY-MM-DDTHH:mm:ssZ。示例：  ``` password_expires_at=lt:2016-12-08T22:02:00Z ``` > - operator取值范围：lt，lte，gt，gte，eq，neq。 > - lt：过期时间小于timestamp。 > - lte：过期时间小于等于timestamp。 > - gt：过期时间大于timestamp。 > - gte：过期时间大于等于timestamp。 > - eq：过期时间等于timestamp。 > - neq：过期时间不等于timestamp。

        :return: The password_expires_at of this KeystoneListUsersRequest.
        :rtype: str
        """
        return self._password_expires_at

    @password_expires_at.setter
    def password_expires_at(self, password_expires_at):
        r"""Sets the password_expires_at of this KeystoneListUsersRequest.

        密码过期时间，格式为：password_expires_at={operator}:{timestamp}。timestamp格式为：YYYY-MM-DDTHH:mm:ssZ。示例：  ``` password_expires_at=lt:2016-12-08T22:02:00Z ``` > - operator取值范围：lt，lte，gt，gte，eq，neq。 > - lt：过期时间小于timestamp。 > - lte：过期时间小于等于timestamp。 > - gt：过期时间大于timestamp。 > - gte：过期时间大于等于timestamp。 > - eq：过期时间等于timestamp。 > - neq：过期时间不等于timestamp。

        :param password_expires_at: The password_expires_at of this KeystoneListUsersRequest.
        :type password_expires_at: str
        """
        self._password_expires_at = password_expires_at

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
        if not isinstance(other, KeystoneListUsersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
