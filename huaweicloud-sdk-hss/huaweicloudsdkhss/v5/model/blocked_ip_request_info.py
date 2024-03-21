# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BlockedIpRequestInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'host_id': 'str',
        'src_ip': 'str',
        'login_type': 'str'
    }

    attribute_map = {
        'host_id': 'host_id',
        'src_ip': 'src_ip',
        'login_type': 'login_type'
    }

    def __init__(self, host_id=None, src_ip=None, login_type=None):
        """BlockedIpRequestInfo

        The model defined in huaweicloud sdk

        :param host_id: 主机ID
        :type host_id: str
        :param src_ip: 攻击源IP
        :type src_ip: str
        :param login_type: 登录类型，包含如下: - \&quot;mysql\&quot; # mysql服务 - \&quot;rdp\&quot; # rdp服务服务 - \&quot;ssh\&quot; # ssh服务 - \&quot;vsftp\&quot; # vsftp服务
        :type login_type: str
        """
        
        

        self._host_id = None
        self._src_ip = None
        self._login_type = None
        self.discriminator = None

        self.host_id = host_id
        self.src_ip = src_ip
        self.login_type = login_type

    @property
    def host_id(self):
        """Gets the host_id of this BlockedIpRequestInfo.

        主机ID

        :return: The host_id of this BlockedIpRequestInfo.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        """Sets the host_id of this BlockedIpRequestInfo.

        主机ID

        :param host_id: The host_id of this BlockedIpRequestInfo.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def src_ip(self):
        """Gets the src_ip of this BlockedIpRequestInfo.

        攻击源IP

        :return: The src_ip of this BlockedIpRequestInfo.
        :rtype: str
        """
        return self._src_ip

    @src_ip.setter
    def src_ip(self, src_ip):
        """Sets the src_ip of this BlockedIpRequestInfo.

        攻击源IP

        :param src_ip: The src_ip of this BlockedIpRequestInfo.
        :type src_ip: str
        """
        self._src_ip = src_ip

    @property
    def login_type(self):
        """Gets the login_type of this BlockedIpRequestInfo.

        登录类型，包含如下: - \"mysql\" # mysql服务 - \"rdp\" # rdp服务服务 - \"ssh\" # ssh服务 - \"vsftp\" # vsftp服务

        :return: The login_type of this BlockedIpRequestInfo.
        :rtype: str
        """
        return self._login_type

    @login_type.setter
    def login_type(self, login_type):
        """Sets the login_type of this BlockedIpRequestInfo.

        登录类型，包含如下: - \"mysql\" # mysql服务 - \"rdp\" # rdp服务服务 - \"ssh\" # ssh服务 - \"vsftp\" # vsftp服务

        :param login_type: The login_type of this BlockedIpRequestInfo.
        :type login_type: str
        """
        self._login_type = login_type

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
        if not isinstance(other, BlockedIpRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
