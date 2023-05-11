# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TenantAgreeAuthDetailV2:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'port': 'int',
        'account': 'str',
        'password': 'str',
        'auth_detail_id': 'int'
    }

    attribute_map = {
        'port': 'port',
        'account': 'account',
        'password': 'password',
        'auth_detail_id': 'auth_detail_id'
    }

    def __init__(self, port=None, account=None, password=None, auth_detail_id=None):
        """TenantAgreeAuthDetailV2

        The model defined in huaweicloud sdk

        :param port: 端口
        :type port: int
        :param account: 账号
        :type account: str
        :param password: 密码
        :type password: str
        :param auth_detail_id: 授权详情id
        :type auth_detail_id: int
        """
        
        

        self._port = None
        self._account = None
        self._password = None
        self._auth_detail_id = None
        self.discriminator = None

        if port is not None:
            self.port = port
        if account is not None:
            self.account = account
        if password is not None:
            self.password = password
        self.auth_detail_id = auth_detail_id

    @property
    def port(self):
        """Gets the port of this TenantAgreeAuthDetailV2.

        端口

        :return: The port of this TenantAgreeAuthDetailV2.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this TenantAgreeAuthDetailV2.

        端口

        :param port: The port of this TenantAgreeAuthDetailV2.
        :type port: int
        """
        self._port = port

    @property
    def account(self):
        """Gets the account of this TenantAgreeAuthDetailV2.

        账号

        :return: The account of this TenantAgreeAuthDetailV2.
        :rtype: str
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this TenantAgreeAuthDetailV2.

        账号

        :param account: The account of this TenantAgreeAuthDetailV2.
        :type account: str
        """
        self._account = account

    @property
    def password(self):
        """Gets the password of this TenantAgreeAuthDetailV2.

        密码

        :return: The password of this TenantAgreeAuthDetailV2.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this TenantAgreeAuthDetailV2.

        密码

        :param password: The password of this TenantAgreeAuthDetailV2.
        :type password: str
        """
        self._password = password

    @property
    def auth_detail_id(self):
        """Gets the auth_detail_id of this TenantAgreeAuthDetailV2.

        授权详情id

        :return: The auth_detail_id of this TenantAgreeAuthDetailV2.
        :rtype: int
        """
        return self._auth_detail_id

    @auth_detail_id.setter
    def auth_detail_id(self, auth_detail_id):
        """Sets the auth_detail_id of this TenantAgreeAuthDetailV2.

        授权详情id

        :param auth_detail_id: The auth_detail_id of this TenantAgreeAuthDetailV2.
        :type auth_detail_id: int
        """
        self._auth_detail_id = auth_detail_id

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
        if not isinstance(other, TenantAgreeAuthDetailV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
