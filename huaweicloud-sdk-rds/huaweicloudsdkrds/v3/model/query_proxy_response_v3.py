# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryProxyResponseV3:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'proxy': 'ProxyInfo',
        'master_instance': 'InstanceInfo',
        'readonly_instances': 'list[InstanceInfo]',
        'proxy_security_group_check_result': 'bool'
    }

    attribute_map = {
        'proxy': 'proxy',
        'master_instance': 'master_instance',
        'readonly_instances': 'readonly_instances',
        'proxy_security_group_check_result': 'proxy_security_group_check_result'
    }

    def __init__(self, proxy=None, master_instance=None, readonly_instances=None, proxy_security_group_check_result=None):
        r"""QueryProxyResponseV3

        The model defined in huaweicloud sdk

        :param proxy: 
        :type proxy: :class:`huaweicloudsdkrds.v3.ProxyInfo`
        :param master_instance: 
        :type master_instance: :class:`huaweicloudsdkrds.v3.InstanceInfo`
        :param readonly_instances: 数据库只读实例信息。
        :type readonly_instances: list[:class:`huaweicloudsdkrds.v3.InstanceInfo`]
        :param proxy_security_group_check_result: 安全组是否放通该数据库代理到数据库的网络地址。
        :type proxy_security_group_check_result: bool
        """
        
        

        self._proxy = None
        self._master_instance = None
        self._readonly_instances = None
        self._proxy_security_group_check_result = None
        self.discriminator = None

        if proxy is not None:
            self.proxy = proxy
        if master_instance is not None:
            self.master_instance = master_instance
        if readonly_instances is not None:
            self.readonly_instances = readonly_instances
        if proxy_security_group_check_result is not None:
            self.proxy_security_group_check_result = proxy_security_group_check_result

    @property
    def proxy(self):
        r"""Gets the proxy of this QueryProxyResponseV3.

        :return: The proxy of this QueryProxyResponseV3.
        :rtype: :class:`huaweicloudsdkrds.v3.ProxyInfo`
        """
        return self._proxy

    @proxy.setter
    def proxy(self, proxy):
        r"""Sets the proxy of this QueryProxyResponseV3.

        :param proxy: The proxy of this QueryProxyResponseV3.
        :type proxy: :class:`huaweicloudsdkrds.v3.ProxyInfo`
        """
        self._proxy = proxy

    @property
    def master_instance(self):
        r"""Gets the master_instance of this QueryProxyResponseV3.

        :return: The master_instance of this QueryProxyResponseV3.
        :rtype: :class:`huaweicloudsdkrds.v3.InstanceInfo`
        """
        return self._master_instance

    @master_instance.setter
    def master_instance(self, master_instance):
        r"""Sets the master_instance of this QueryProxyResponseV3.

        :param master_instance: The master_instance of this QueryProxyResponseV3.
        :type master_instance: :class:`huaweicloudsdkrds.v3.InstanceInfo`
        """
        self._master_instance = master_instance

    @property
    def readonly_instances(self):
        r"""Gets the readonly_instances of this QueryProxyResponseV3.

        数据库只读实例信息。

        :return: The readonly_instances of this QueryProxyResponseV3.
        :rtype: list[:class:`huaweicloudsdkrds.v3.InstanceInfo`]
        """
        return self._readonly_instances

    @readonly_instances.setter
    def readonly_instances(self, readonly_instances):
        r"""Sets the readonly_instances of this QueryProxyResponseV3.

        数据库只读实例信息。

        :param readonly_instances: The readonly_instances of this QueryProxyResponseV3.
        :type readonly_instances: list[:class:`huaweicloudsdkrds.v3.InstanceInfo`]
        """
        self._readonly_instances = readonly_instances

    @property
    def proxy_security_group_check_result(self):
        r"""Gets the proxy_security_group_check_result of this QueryProxyResponseV3.

        安全组是否放通该数据库代理到数据库的网络地址。

        :return: The proxy_security_group_check_result of this QueryProxyResponseV3.
        :rtype: bool
        """
        return self._proxy_security_group_check_result

    @proxy_security_group_check_result.setter
    def proxy_security_group_check_result(self, proxy_security_group_check_result):
        r"""Sets the proxy_security_group_check_result of this QueryProxyResponseV3.

        安全组是否放通该数据库代理到数据库的网络地址。

        :param proxy_security_group_check_result: The proxy_security_group_check_result of this QueryProxyResponseV3.
        :type proxy_security_group_check_result: bool
        """
        self._proxy_security_group_check_result = proxy_security_group_check_result

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
        if not isinstance(other, QueryProxyResponseV3):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
