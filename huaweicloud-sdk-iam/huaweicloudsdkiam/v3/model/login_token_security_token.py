# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LoginTokenSecurityToken:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'access': 'str',
        'secret': 'str',
        'id': 'str',
        'duration_seconds': 'int'
    }

    attribute_map = {
        'access': 'access',
        'secret': 'secret',
        'id': 'id',
        'duration_seconds': 'duration_seconds'
    }

    def __init__(self, access=None, secret=None, id=None, duration_seconds=None):
        """LoginTokenSecurityToken

        The model defined in huaweicloud sdk

        :param access: AK。
        :type access: str
        :param secret: SK。
        :type secret: str
        :param id: securitytoken，即临时身份的安全token。  支持使用自定义代理用户或普通用户获取的securitytoken换取logintoken，详情请参见：[通过token获取临时访问密钥和securitytoken](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product&#x3D;IAM&amp;api&#x3D;CreateTemporaryAccessKeyByToken)。  支持委托的方式，但获取securitytoken时，请求体中必须填写session_user.name参数，详情请参见：[通过委托获取临时访问密钥和securitytoken](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product&#x3D;IAM&amp;api&#x3D;CreateTemporaryAccessKeyByAgency)。
        :type id: str
        :param duration_seconds: 自定义代理登录票据logintoken的有效时间，时间单位为秒。默认10分钟，取值范围10min~12h，且取值不能大于临时安全凭证securitytoken的过期时间。
        :type duration_seconds: int
        """
        
        

        self._access = None
        self._secret = None
        self._id = None
        self._duration_seconds = None
        self.discriminator = None

        self.access = access
        self.secret = secret
        self.id = id
        if duration_seconds is not None:
            self.duration_seconds = duration_seconds

    @property
    def access(self):
        """Gets the access of this LoginTokenSecurityToken.

        AK。

        :return: The access of this LoginTokenSecurityToken.
        :rtype: str
        """
        return self._access

    @access.setter
    def access(self, access):
        """Sets the access of this LoginTokenSecurityToken.

        AK。

        :param access: The access of this LoginTokenSecurityToken.
        :type access: str
        """
        self._access = access

    @property
    def secret(self):
        """Gets the secret of this LoginTokenSecurityToken.

        SK。

        :return: The secret of this LoginTokenSecurityToken.
        :rtype: str
        """
        return self._secret

    @secret.setter
    def secret(self, secret):
        """Sets the secret of this LoginTokenSecurityToken.

        SK。

        :param secret: The secret of this LoginTokenSecurityToken.
        :type secret: str
        """
        self._secret = secret

    @property
    def id(self):
        """Gets the id of this LoginTokenSecurityToken.

        securitytoken，即临时身份的安全token。  支持使用自定义代理用户或普通用户获取的securitytoken换取logintoken，详情请参见：[通过token获取临时访问密钥和securitytoken](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product=IAM&api=CreateTemporaryAccessKeyByToken)。  支持委托的方式，但获取securitytoken时，请求体中必须填写session_user.name参数，详情请参见：[通过委托获取临时访问密钥和securitytoken](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product=IAM&api=CreateTemporaryAccessKeyByAgency)。

        :return: The id of this LoginTokenSecurityToken.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LoginTokenSecurityToken.

        securitytoken，即临时身份的安全token。  支持使用自定义代理用户或普通用户获取的securitytoken换取logintoken，详情请参见：[通过token获取临时访问密钥和securitytoken](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product=IAM&api=CreateTemporaryAccessKeyByToken)。  支持委托的方式，但获取securitytoken时，请求体中必须填写session_user.name参数，详情请参见：[通过委托获取临时访问密钥和securitytoken](https://apiexplorer.developer.huaweicloud.com/apiexplorer/doc?product=IAM&api=CreateTemporaryAccessKeyByAgency)。

        :param id: The id of this LoginTokenSecurityToken.
        :type id: str
        """
        self._id = id

    @property
    def duration_seconds(self):
        """Gets the duration_seconds of this LoginTokenSecurityToken.

        自定义代理登录票据logintoken的有效时间，时间单位为秒。默认10分钟，取值范围10min~12h，且取值不能大于临时安全凭证securitytoken的过期时间。

        :return: The duration_seconds of this LoginTokenSecurityToken.
        :rtype: int
        """
        return self._duration_seconds

    @duration_seconds.setter
    def duration_seconds(self, duration_seconds):
        """Sets the duration_seconds of this LoginTokenSecurityToken.

        自定义代理登录票据logintoken的有效时间，时间单位为秒。默认10分钟，取值范围10min~12h，且取值不能大于临时安全凭证securitytoken的过期时间。

        :param duration_seconds: The duration_seconds of this LoginTokenSecurityToken.
        :type duration_seconds: int
        """
        self._duration_seconds = duration_seconds

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
        if not isinstance(other, LoginTokenSecurityToken):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
