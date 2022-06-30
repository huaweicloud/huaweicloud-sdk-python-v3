# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EdgeNodeUpdate:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'description': 'str',
        'log_configs': 'list[LogConfigs]',
        'ntp_servers': 'list[str]',
        'attributes': 'list[Attributes]'
    }

    attribute_map = {
        'description': 'description',
        'log_configs': 'log_configs',
        'ntp_servers': 'ntp_servers',
        'attributes': 'attributes'
    }

    def __init__(self, description=None, log_configs=None, ntp_servers=None, attributes=None):
        """EdgeNodeUpdate

        The model defined in huaweicloud sdk

        :param description: 边缘节点描述，最大长度255，不允许^ ~ # $ % &amp; * &lt; &gt; ( ) [ ] { } &#39; \&quot; \\
        :type description: str
        :param log_configs: 边缘节点日志配置
        :type log_configs: list[:class:`huaweicloudsdkief.v1.LogConfigs`]
        :param ntp_servers: NTP服务器地址，每个节点最多仅能配置两个。D310表示D310类型；D910表示D910类型；不填表示为D310类型。
        :type ntp_servers: list[str]
        :param attributes: 边缘节点属性，关联属性个数最多为32个
        :type attributes: list[:class:`huaweicloudsdkief.v1.Attributes`]
        """
        
        

        self._description = None
        self._log_configs = None
        self._ntp_servers = None
        self._attributes = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if log_configs is not None:
            self.log_configs = log_configs
        if ntp_servers is not None:
            self.ntp_servers = ntp_servers
        if attributes is not None:
            self.attributes = attributes

    @property
    def description(self):
        """Gets the description of this EdgeNodeUpdate.

        边缘节点描述，最大长度255，不允许^ ~ # $ % & * < > ( ) [ ] { } ' \" \\

        :return: The description of this EdgeNodeUpdate.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this EdgeNodeUpdate.

        边缘节点描述，最大长度255，不允许^ ~ # $ % & * < > ( ) [ ] { } ' \" \\

        :param description: The description of this EdgeNodeUpdate.
        :type description: str
        """
        self._description = description

    @property
    def log_configs(self):
        """Gets the log_configs of this EdgeNodeUpdate.

        边缘节点日志配置

        :return: The log_configs of this EdgeNodeUpdate.
        :rtype: list[:class:`huaweicloudsdkief.v1.LogConfigs`]
        """
        return self._log_configs

    @log_configs.setter
    def log_configs(self, log_configs):
        """Sets the log_configs of this EdgeNodeUpdate.

        边缘节点日志配置

        :param log_configs: The log_configs of this EdgeNodeUpdate.
        :type log_configs: list[:class:`huaweicloudsdkief.v1.LogConfigs`]
        """
        self._log_configs = log_configs

    @property
    def ntp_servers(self):
        """Gets the ntp_servers of this EdgeNodeUpdate.

        NTP服务器地址，每个节点最多仅能配置两个。D310表示D310类型；D910表示D910类型；不填表示为D310类型。

        :return: The ntp_servers of this EdgeNodeUpdate.
        :rtype: list[str]
        """
        return self._ntp_servers

    @ntp_servers.setter
    def ntp_servers(self, ntp_servers):
        """Sets the ntp_servers of this EdgeNodeUpdate.

        NTP服务器地址，每个节点最多仅能配置两个。D310表示D310类型；D910表示D910类型；不填表示为D310类型。

        :param ntp_servers: The ntp_servers of this EdgeNodeUpdate.
        :type ntp_servers: list[str]
        """
        self._ntp_servers = ntp_servers

    @property
    def attributes(self):
        """Gets the attributes of this EdgeNodeUpdate.

        边缘节点属性，关联属性个数最多为32个

        :return: The attributes of this EdgeNodeUpdate.
        :rtype: list[:class:`huaweicloudsdkief.v1.Attributes`]
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this EdgeNodeUpdate.

        边缘节点属性，关联属性个数最多为32个

        :param attributes: The attributes of this EdgeNodeUpdate.
        :type attributes: list[:class:`huaweicloudsdkief.v1.Attributes`]
        """
        self._attributes = attributes

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
        if not isinstance(other, EdgeNodeUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
