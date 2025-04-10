# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChangeInstanceNetwork:

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
        r"""ChangeInstanceNetwork

        The model defined in huaweicloud sdk

        :param type: 云堡垒机实例状态，枚举值如下： - create  创建 - renewals  续费 - change  扩容
        :type type: str
        :param security_groups: 云堡垒机实例修改后的安全组信息。
        :type security_groups: list[:class:`huaweicloudsdkcbh.v1.SecurityGroup`]
        :param nics: 云堡垒机实例修改后的网卡信息。
        :type nics: list[:class:`huaweicloudsdkcbh.v1.Nics`]
        :param server_id: 云堡垒机实例ID。云堡垒机实例状态为renewals或change时必传。
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
        r"""Gets the type of this ChangeInstanceNetwork.

        云堡垒机实例状态，枚举值如下： - create  创建 - renewals  续费 - change  扩容

        :return: The type of this ChangeInstanceNetwork.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ChangeInstanceNetwork.

        云堡垒机实例状态，枚举值如下： - create  创建 - renewals  续费 - change  扩容

        :param type: The type of this ChangeInstanceNetwork.
        :type type: str
        """
        self._type = type

    @property
    def security_groups(self):
        r"""Gets the security_groups of this ChangeInstanceNetwork.

        云堡垒机实例修改后的安全组信息。

        :return: The security_groups of this ChangeInstanceNetwork.
        :rtype: list[:class:`huaweicloudsdkcbh.v1.SecurityGroup`]
        """
        return self._security_groups

    @security_groups.setter
    def security_groups(self, security_groups):
        r"""Sets the security_groups of this ChangeInstanceNetwork.

        云堡垒机实例修改后的安全组信息。

        :param security_groups: The security_groups of this ChangeInstanceNetwork.
        :type security_groups: list[:class:`huaweicloudsdkcbh.v1.SecurityGroup`]
        """
        self._security_groups = security_groups

    @property
    def nics(self):
        r"""Gets the nics of this ChangeInstanceNetwork.

        云堡垒机实例修改后的网卡信息。

        :return: The nics of this ChangeInstanceNetwork.
        :rtype: list[:class:`huaweicloudsdkcbh.v1.Nics`]
        """
        return self._nics

    @nics.setter
    def nics(self, nics):
        r"""Sets the nics of this ChangeInstanceNetwork.

        云堡垒机实例修改后的网卡信息。

        :param nics: The nics of this ChangeInstanceNetwork.
        :type nics: list[:class:`huaweicloudsdkcbh.v1.Nics`]
        """
        self._nics = nics

    @property
    def server_id(self):
        r"""Gets the server_id of this ChangeInstanceNetwork.

        云堡垒机实例ID。云堡垒机实例状态为renewals或change时必传。

        :return: The server_id of this ChangeInstanceNetwork.
        :rtype: str
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        r"""Sets the server_id of this ChangeInstanceNetwork.

        云堡垒机实例ID。云堡垒机实例状态为renewals或change时必传。

        :param server_id: The server_id of this ChangeInstanceNetwork.
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
        if not isinstance(other, ChangeInstanceNetwork):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
