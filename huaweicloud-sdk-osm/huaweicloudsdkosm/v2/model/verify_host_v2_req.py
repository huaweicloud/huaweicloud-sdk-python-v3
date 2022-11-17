# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VerifyHostV2Req:

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
        'group_id': 'str'
    }

    attribute_map = {
        'port': 'port',
        'account': 'account',
        'password': 'password',
        'group_id': 'group_id'
    }

    def __init__(self, port=None, account=None, password=None, group_id=None):
        """VerifyHostV2Req

        The model defined in huaweicloud sdk

        :param port: 主机端口
        :type port: int
        :param account: 主机账号
        :type account: str
        :param password: 主机密码
        :type password: str
        :param group_id: 组id
        :type group_id: str
        """
        
        

        self._port = None
        self._account = None
        self._password = None
        self._group_id = None
        self.discriminator = None

        self.port = port
        self.account = account
        self.password = password
        if group_id is not None:
            self.group_id = group_id

    @property
    def port(self):
        """Gets the port of this VerifyHostV2Req.

        主机端口

        :return: The port of this VerifyHostV2Req.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this VerifyHostV2Req.

        主机端口

        :param port: The port of this VerifyHostV2Req.
        :type port: int
        """
        self._port = port

    @property
    def account(self):
        """Gets the account of this VerifyHostV2Req.

        主机账号

        :return: The account of this VerifyHostV2Req.
        :rtype: str
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this VerifyHostV2Req.

        主机账号

        :param account: The account of this VerifyHostV2Req.
        :type account: str
        """
        self._account = account

    @property
    def password(self):
        """Gets the password of this VerifyHostV2Req.

        主机密码

        :return: The password of this VerifyHostV2Req.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this VerifyHostV2Req.

        主机密码

        :param password: The password of this VerifyHostV2Req.
        :type password: str
        """
        self._password = password

    @property
    def group_id(self):
        """Gets the group_id of this VerifyHostV2Req.

        组id

        :return: The group_id of this VerifyHostV2Req.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this VerifyHostV2Req.

        组id

        :param group_id: The group_id of this VerifyHostV2Req.
        :type group_id: str
        """
        self._group_id = group_id

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
        if not isinstance(other, VerifyHostV2Req):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
