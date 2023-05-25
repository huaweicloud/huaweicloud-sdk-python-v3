# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NetworkRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'security_groups': 'list[SecurityGroup]',
        'nics': 'list[Nics]',
        'server_id': 'str'
    }

    attribute_map = {
        'type': 'type',
        'security_groups': 'security_groups',
        'nics': 'nics',
        'server_id': 'server_id'
    }

    def __init__(self, type=None, security_groups=None, nics=None, server_id=None):
        """NetworkRequestBody

        The model defined in huaweicloud sdk

        :param type: 云堡垒机实例状态，枚举值如下： - create  创建 - renewals  更新 - change  变更 状态为renewals或change时server_id必传。
        :type type: str
        :param security_groups: 云堡垒升级实例所在安全组信息。
        :type security_groups: list[:class:`huaweicloudsdkcbh.v1.SecurityGroup`]
        :param nics: 云堡垒机实例的网卡信息。
        :type nics: list[:class:`huaweicloudsdkcbh.v1.Nics`]
        :param server_id: 云堡垒机实例ID。
        :type server_id: str
        """
        
        

        self._type = None
        self._security_groups = None
        self._nics = None
        self._server_id = None
        self.discriminator = None

        self.type = type
        self.security_groups = security_groups
        self.nics = nics
        if server_id is not None:
            self.server_id = server_id

    @property
    def type(self):
        """Gets the type of this NetworkRequestBody.

        云堡垒机实例状态，枚举值如下： - create  创建 - renewals  更新 - change  变更 状态为renewals或change时server_id必传。

        :return: The type of this NetworkRequestBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this NetworkRequestBody.

        云堡垒机实例状态，枚举值如下： - create  创建 - renewals  更新 - change  变更 状态为renewals或change时server_id必传。

        :param type: The type of this NetworkRequestBody.
        :type type: str
        """
        self._type = type

    @property
    def security_groups(self):
        """Gets the security_groups of this NetworkRequestBody.

        云堡垒升级实例所在安全组信息。

        :return: The security_groups of this NetworkRequestBody.
        :rtype: list[:class:`huaweicloudsdkcbh.v1.SecurityGroup`]
        """
        return self._security_groups

    @security_groups.setter
    def security_groups(self, security_groups):
        """Sets the security_groups of this NetworkRequestBody.

        云堡垒升级实例所在安全组信息。

        :param security_groups: The security_groups of this NetworkRequestBody.
        :type security_groups: list[:class:`huaweicloudsdkcbh.v1.SecurityGroup`]
        """
        self._security_groups = security_groups

    @property
    def nics(self):
        """Gets the nics of this NetworkRequestBody.

        云堡垒机实例的网卡信息。

        :return: The nics of this NetworkRequestBody.
        :rtype: list[:class:`huaweicloudsdkcbh.v1.Nics`]
        """
        return self._nics

    @nics.setter
    def nics(self, nics):
        """Sets the nics of this NetworkRequestBody.

        云堡垒机实例的网卡信息。

        :param nics: The nics of this NetworkRequestBody.
        :type nics: list[:class:`huaweicloudsdkcbh.v1.Nics`]
        """
        self._nics = nics

    @property
    def server_id(self):
        """Gets the server_id of this NetworkRequestBody.

        云堡垒机实例ID。

        :return: The server_id of this NetworkRequestBody.
        :rtype: str
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        """Sets the server_id of this NetworkRequestBody.

        云堡垒机实例ID。

        :param server_id: The server_id of this NetworkRequestBody.
        :type server_id: str
        """
        self._server_id = server_id

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
        if not isinstance(other, NetworkRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
