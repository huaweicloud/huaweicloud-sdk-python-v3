# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModifyLoginCommonIpRequestInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ip_addr': 'str',
        'host_id_list': 'list[str]'
    }

    attribute_map = {
        'ip_addr': 'ip_addr',
        'host_id_list': 'host_id_list'
    }

    def __init__(self, ip_addr=None, host_id_list=None):
        r"""ModifyLoginCommonIpRequestInfo

        The model defined in huaweicloud sdk

        :param ip_addr: 登录IP或登录网段,登录网段由IP地址和掩码组成,以&#39;/&#39;连接。
        :type ip_addr: str
        :param host_id_list: 服务器ID列表,不可为NULL,删除常用登录IP时,需要将服务器ID列表置为空列表[]。
        :type host_id_list: list[str]
        """
        
        

        self._ip_addr = None
        self._host_id_list = None
        self.discriminator = None

        self.ip_addr = ip_addr
        self.host_id_list = host_id_list

    @property
    def ip_addr(self):
        r"""Gets the ip_addr of this ModifyLoginCommonIpRequestInfo.

        登录IP或登录网段,登录网段由IP地址和掩码组成,以'/'连接。

        :return: The ip_addr of this ModifyLoginCommonIpRequestInfo.
        :rtype: str
        """
        return self._ip_addr

    @ip_addr.setter
    def ip_addr(self, ip_addr):
        r"""Sets the ip_addr of this ModifyLoginCommonIpRequestInfo.

        登录IP或登录网段,登录网段由IP地址和掩码组成,以'/'连接。

        :param ip_addr: The ip_addr of this ModifyLoginCommonIpRequestInfo.
        :type ip_addr: str
        """
        self._ip_addr = ip_addr

    @property
    def host_id_list(self):
        r"""Gets the host_id_list of this ModifyLoginCommonIpRequestInfo.

        服务器ID列表,不可为NULL,删除常用登录IP时,需要将服务器ID列表置为空列表[]。

        :return: The host_id_list of this ModifyLoginCommonIpRequestInfo.
        :rtype: list[str]
        """
        return self._host_id_list

    @host_id_list.setter
    def host_id_list(self, host_id_list):
        r"""Sets the host_id_list of this ModifyLoginCommonIpRequestInfo.

        服务器ID列表,不可为NULL,删除常用登录IP时,需要将服务器ID列表置为空列表[]。

        :param host_id_list: The host_id_list of this ModifyLoginCommonIpRequestInfo.
        :type host_id_list: list[str]
        """
        self._host_id_list = host_id_list

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
        if not isinstance(other, ModifyLoginCommonIpRequestInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
