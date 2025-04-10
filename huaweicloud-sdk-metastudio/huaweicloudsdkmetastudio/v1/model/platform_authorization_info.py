# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PlatformAuthorizationInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'authorize_state': 'str',
        'authorized_time': 'str',
        'expire_time': 'str',
        'account': 'str'
    }

    attribute_map = {
        'authorize_state': 'authorize_state',
        'authorized_time': 'authorized_time',
        'expire_time': 'expire_time',
        'account': 'account'
    }

    def __init__(self, authorize_state=None, authorized_time=None, expire_time=None, account=None):
        r"""PlatformAuthorizationInfo

        The model defined in huaweicloud sdk

        :param authorize_state: 授权状态。 * AUTHORIZED: 已授权 * UNAUTHORIZED: 未授权
        :type authorize_state: str
        :param authorized_time: 授权时间
        :type authorized_time: str
        :param expire_time: 过期时间
        :type expire_time: str
        :param account: 授权账号信息。 美团平台对应：opBizCode
        :type account: str
        """
        
        

        self._authorize_state = None
        self._authorized_time = None
        self._expire_time = None
        self._account = None
        self.discriminator = None

        if authorize_state is not None:
            self.authorize_state = authorize_state
        if authorized_time is not None:
            self.authorized_time = authorized_time
        if expire_time is not None:
            self.expire_time = expire_time
        if account is not None:
            self.account = account

    @property
    def authorize_state(self):
        r"""Gets the authorize_state of this PlatformAuthorizationInfo.

        授权状态。 * AUTHORIZED: 已授权 * UNAUTHORIZED: 未授权

        :return: The authorize_state of this PlatformAuthorizationInfo.
        :rtype: str
        """
        return self._authorize_state

    @authorize_state.setter
    def authorize_state(self, authorize_state):
        r"""Sets the authorize_state of this PlatformAuthorizationInfo.

        授权状态。 * AUTHORIZED: 已授权 * UNAUTHORIZED: 未授权

        :param authorize_state: The authorize_state of this PlatformAuthorizationInfo.
        :type authorize_state: str
        """
        self._authorize_state = authorize_state

    @property
    def authorized_time(self):
        r"""Gets the authorized_time of this PlatformAuthorizationInfo.

        授权时间

        :return: The authorized_time of this PlatformAuthorizationInfo.
        :rtype: str
        """
        return self._authorized_time

    @authorized_time.setter
    def authorized_time(self, authorized_time):
        r"""Sets the authorized_time of this PlatformAuthorizationInfo.

        授权时间

        :param authorized_time: The authorized_time of this PlatformAuthorizationInfo.
        :type authorized_time: str
        """
        self._authorized_time = authorized_time

    @property
    def expire_time(self):
        r"""Gets the expire_time of this PlatformAuthorizationInfo.

        过期时间

        :return: The expire_time of this PlatformAuthorizationInfo.
        :rtype: str
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        r"""Sets the expire_time of this PlatformAuthorizationInfo.

        过期时间

        :param expire_time: The expire_time of this PlatformAuthorizationInfo.
        :type expire_time: str
        """
        self._expire_time = expire_time

    @property
    def account(self):
        r"""Gets the account of this PlatformAuthorizationInfo.

        授权账号信息。 美团平台对应：opBizCode

        :return: The account of this PlatformAuthorizationInfo.
        :rtype: str
        """
        return self._account

    @account.setter
    def account(self, account):
        r"""Sets the account of this PlatformAuthorizationInfo.

        授权账号信息。 美团平台对应：opBizCode

        :param account: The account of this PlatformAuthorizationInfo.
        :type account: str
        """
        self._account = account

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
        if not isinstance(other, PlatformAuthorizationInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
