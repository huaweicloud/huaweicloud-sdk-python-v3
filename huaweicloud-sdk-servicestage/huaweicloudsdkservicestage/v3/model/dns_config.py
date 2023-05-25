# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DnsConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'nameservers': 'list[str]',
        'searches': 'list[str]',
        'options': 'list[ComponentConfigEnvs]'
    }

    attribute_map = {
        'nameservers': 'nameservers',
        'searches': 'searches',
        'options': 'options'
    }

    def __init__(self, nameservers=None, searches=None, options=None):
        """DnsConfig

        The model defined in huaweicloud sdk

        :param nameservers: 将用作于 Pod 的 DNS 服务器的 IP 地址列表
        :type nameservers: list[str]
        :param searches: 用于在 Pod 中查找主机名的 DNS 搜索域的列表。此属性是可选的
        :type searches: list[str]
        :param options: 可选的对象列表，其中每个对象可能具有 name 属性（必需）和 value 属性（可选）。 此属性中的内容将合并到从指定的 DNS 策略生成的选项。 重复的条目将被删除。
        :type options: list[:class:`huaweicloudsdkservicestage.v3.ComponentConfigEnvs`]
        """
        
        

        self._nameservers = None
        self._searches = None
        self._options = None
        self.discriminator = None

        if nameservers is not None:
            self.nameservers = nameservers
        if searches is not None:
            self.searches = searches
        if options is not None:
            self.options = options

    @property
    def nameservers(self):
        """Gets the nameservers of this DnsConfig.

        将用作于 Pod 的 DNS 服务器的 IP 地址列表

        :return: The nameservers of this DnsConfig.
        :rtype: list[str]
        """
        return self._nameservers

    @nameservers.setter
    def nameservers(self, nameservers):
        """Sets the nameservers of this DnsConfig.

        将用作于 Pod 的 DNS 服务器的 IP 地址列表

        :param nameservers: The nameservers of this DnsConfig.
        :type nameservers: list[str]
        """
        self._nameservers = nameservers

    @property
    def searches(self):
        """Gets the searches of this DnsConfig.

        用于在 Pod 中查找主机名的 DNS 搜索域的列表。此属性是可选的

        :return: The searches of this DnsConfig.
        :rtype: list[str]
        """
        return self._searches

    @searches.setter
    def searches(self, searches):
        """Sets the searches of this DnsConfig.

        用于在 Pod 中查找主机名的 DNS 搜索域的列表。此属性是可选的

        :param searches: The searches of this DnsConfig.
        :type searches: list[str]
        """
        self._searches = searches

    @property
    def options(self):
        """Gets the options of this DnsConfig.

        可选的对象列表，其中每个对象可能具有 name 属性（必需）和 value 属性（可选）。 此属性中的内容将合并到从指定的 DNS 策略生成的选项。 重复的条目将被删除。

        :return: The options of this DnsConfig.
        :rtype: list[:class:`huaweicloudsdkservicestage.v3.ComponentConfigEnvs`]
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this DnsConfig.

        可选的对象列表，其中每个对象可能具有 name 属性（必需）和 value 属性（可选）。 此属性中的内容将合并到从指定的 DNS 策略生成的选项。 重复的条目将被删除。

        :param options: The options of this DnsConfig.
        :type options: list[:class:`huaweicloudsdkservicestage.v3.ComponentConfigEnvs`]
        """
        self._options = options

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
        if not isinstance(other, DnsConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
