# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ContainerExtraRdpInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'proto_env': 'str',
        'system': 'str'
    }

    attribute_map = {
        'proto_env': 'proto_env',
        'system': 'system'
    }

    def __init__(self, proto_env=None, system=None):
        r"""ContainerExtraRdpInfo

        The model defined in huaweicloud sdk

        :param proto_env: 协议类型: - 0 : 协议模拟 - 1 : 系统模拟
        :type proto_env: str
        :param system: 系统类型，系统模拟时使用: - win7 : win 7 - win8 : win 8 - win10 : win 10 - win-server2012 : win-server 2012 - win-server2016 : win-server 2016
        :type system: str
        """
        
        

        self._proto_env = None
        self._system = None
        self.discriminator = None

        if proto_env is not None:
            self.proto_env = proto_env
        if system is not None:
            self.system = system

    @property
    def proto_env(self):
        r"""Gets the proto_env of this ContainerExtraRdpInfo.

        协议类型: - 0 : 协议模拟 - 1 : 系统模拟

        :return: The proto_env of this ContainerExtraRdpInfo.
        :rtype: str
        """
        return self._proto_env

    @proto_env.setter
    def proto_env(self, proto_env):
        r"""Sets the proto_env of this ContainerExtraRdpInfo.

        协议类型: - 0 : 协议模拟 - 1 : 系统模拟

        :param proto_env: The proto_env of this ContainerExtraRdpInfo.
        :type proto_env: str
        """
        self._proto_env = proto_env

    @property
    def system(self):
        r"""Gets the system of this ContainerExtraRdpInfo.

        系统类型，系统模拟时使用: - win7 : win 7 - win8 : win 8 - win10 : win 10 - win-server2012 : win-server 2012 - win-server2016 : win-server 2016

        :return: The system of this ContainerExtraRdpInfo.
        :rtype: str
        """
        return self._system

    @system.setter
    def system(self, system):
        r"""Sets the system of this ContainerExtraRdpInfo.

        系统类型，系统模拟时使用: - win7 : win 7 - win8 : win 8 - win10 : win 10 - win-server2012 : win-server 2012 - win-server2016 : win-server 2016

        :param system: The system of this ContainerExtraRdpInfo.
        :type system: str
        """
        self._system = system

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
        if not isinstance(other, ContainerExtraRdpInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
