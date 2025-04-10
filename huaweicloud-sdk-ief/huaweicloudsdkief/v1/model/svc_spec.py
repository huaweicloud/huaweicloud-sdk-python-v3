# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SvcSpec:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster_ip': 'str',
        'external_ips': 'list[str]',
        'external_name': 'str',
        'ports': 'list[SvcPort]',
        'selector': 'dict(str, str)',
        'type': 'str'
    }

    attribute_map = {
        'cluster_ip': 'cluster_ip',
        'external_ips': 'external_ips',
        'external_name': 'external_name',
        'ports': 'ports',
        'selector': 'selector',
        'type': 'type'
    }

    def __init__(self, cluster_ip=None, external_ips=None, external_name=None, ports=None, selector=None, type=None):
        r"""SvcSpec

        The model defined in huaweicloud sdk

        :param cluster_ip: 虚拟服务IP地址
        :type cluster_ip: str
        :param external_ips: 外部IP列表 --- 暂不支持
        :type external_ips: list[str]
        :param external_name: 外部域名 --- 暂不支持
        :type external_name: str
        :param ports: 服务需要暴露的端口列表
        :type ports: list[:class:`huaweicloudsdkief.v1.SvcPort`]
        :param selector: 标签选择器，将选择具有指定Label标签的Pod作为管理范围
        :type selector: dict(str, str)
        :param type: 服务的类型
        :type type: str
        """
        
        

        self._cluster_ip = None
        self._external_ips = None
        self._external_name = None
        self._ports = None
        self._selector = None
        self._type = None
        self.discriminator = None

        if cluster_ip is not None:
            self.cluster_ip = cluster_ip
        if external_ips is not None:
            self.external_ips = external_ips
        if external_name is not None:
            self.external_name = external_name
        if ports is not None:
            self.ports = ports
        self.selector = selector
        if type is not None:
            self.type = type

    @property
    def cluster_ip(self):
        r"""Gets the cluster_ip of this SvcSpec.

        虚拟服务IP地址

        :return: The cluster_ip of this SvcSpec.
        :rtype: str
        """
        return self._cluster_ip

    @cluster_ip.setter
    def cluster_ip(self, cluster_ip):
        r"""Sets the cluster_ip of this SvcSpec.

        虚拟服务IP地址

        :param cluster_ip: The cluster_ip of this SvcSpec.
        :type cluster_ip: str
        """
        self._cluster_ip = cluster_ip

    @property
    def external_ips(self):
        r"""Gets the external_ips of this SvcSpec.

        外部IP列表 --- 暂不支持

        :return: The external_ips of this SvcSpec.
        :rtype: list[str]
        """
        return self._external_ips

    @external_ips.setter
    def external_ips(self, external_ips):
        r"""Sets the external_ips of this SvcSpec.

        外部IP列表 --- 暂不支持

        :param external_ips: The external_ips of this SvcSpec.
        :type external_ips: list[str]
        """
        self._external_ips = external_ips

    @property
    def external_name(self):
        r"""Gets the external_name of this SvcSpec.

        外部域名 --- 暂不支持

        :return: The external_name of this SvcSpec.
        :rtype: str
        """
        return self._external_name

    @external_name.setter
    def external_name(self, external_name):
        r"""Sets the external_name of this SvcSpec.

        外部域名 --- 暂不支持

        :param external_name: The external_name of this SvcSpec.
        :type external_name: str
        """
        self._external_name = external_name

    @property
    def ports(self):
        r"""Gets the ports of this SvcSpec.

        服务需要暴露的端口列表

        :return: The ports of this SvcSpec.
        :rtype: list[:class:`huaweicloudsdkief.v1.SvcPort`]
        """
        return self._ports

    @ports.setter
    def ports(self, ports):
        r"""Sets the ports of this SvcSpec.

        服务需要暴露的端口列表

        :param ports: The ports of this SvcSpec.
        :type ports: list[:class:`huaweicloudsdkief.v1.SvcPort`]
        """
        self._ports = ports

    @property
    def selector(self):
        r"""Gets the selector of this SvcSpec.

        标签选择器，将选择具有指定Label标签的Pod作为管理范围

        :return: The selector of this SvcSpec.
        :rtype: dict(str, str)
        """
        return self._selector

    @selector.setter
    def selector(self, selector):
        r"""Sets the selector of this SvcSpec.

        标签选择器，将选择具有指定Label标签的Pod作为管理范围

        :param selector: The selector of this SvcSpec.
        :type selector: dict(str, str)
        """
        self._selector = selector

    @property
    def type(self):
        r"""Gets the type of this SvcSpec.

        服务的类型

        :return: The type of this SvcSpec.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this SvcSpec.

        服务的类型

        :param type: The type of this SvcSpec.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, SvcSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
